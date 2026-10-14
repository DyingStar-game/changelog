"""
Shared changelog model (ADR 0001): component configuration, parsing of the
changelog block of a PR description, reading and writing CHANGELOG files.

An entry is a dict {"type": str | None, "area": str | None, "text": str}:
- type: a Keep a Changelog type key ("added", "fixed"…), None for entries
  written before types existed;
- area: an area key of the component (components.json), None for entries
  written before areas existed;
- text: the bullet text, its display lines joined by "\n".
"""
import difflib
import json
import os
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(REPO_ROOT, "components.json")

# Keep a Changelog types, in the order their sections appear. The section
# headings stay in English in both files, as Keep a Changelog's French text does.
TYPES = {
    "added": {"en": "Added", "fr": "Ajouts"},
    "changed": {"en": "Changed", "fr": "Modifications"},
    "deprecated": {"en": "Deprecated", "fr": "Obsolescences"},
    "removed": {"en": "Removed", "fr": "Suppressions"},
    "fixed": {"en": "Fixed", "fr": "Corrections"},
    "security": {"en": "Security", "fr": "Sécurité"},
}
# Used at merge time only, for an entry the PR check would have refused
FALLBACK_TYPE = "changed"
FALLBACK_AREA = "general"
FALLBACK_AREA_LABELS = {"en": "General", "fr": "Général"}

# Heading of the entries written before types existed, once a section also
# has typed entries (not a type: read back as None)
UNTYPED_HEADING = "Uncategorized"

LANGS = ("en", "fr")
FILES = {"en": "CHANGELOG.md", "fr": "CHANGELOG.fr.md"}
UNRELEASED_LABELS = {"en": "Unreleased", "fr": "Non publié"}
UNRELEASED_HEADERS = {f"## [{label}]" for label in UNRELEASED_LABELS.values()}
VERSION_HEADER_RE = re.compile(
    r"^## \[(?P<version>[^\]]+)\] - (?P<date>\d{4}-\d{2}-\d{2})(?P<yanked> \[YANKED\])?\s*$"
)
LINK_REF_RE = re.compile(r"^\[[^\]]+\]: \S+\s*$")
# A dev release, cut by a preprod build (ADR 0003): <next version>-dev.<stamp>
DEV_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+-dev\.")


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def is_dev(version: str) -> bool:
    return bool(DEV_VERSION_RE.match(version))


def area_labels(cfg: dict, area: str | None, lang: str) -> str | None:
    if area is None:
        return None
    if area == FALLBACK_AREA:
        return FALLBACK_AREA_LABELS[lang]
    labels = cfg["areas"].get(area)
    return labels[lang] if labels else area


def tag_for(cfg: dict, version: str) -> str | None:
    """Git tag of a version, None when the component has no tag convention."""
    if version in cfg.get("tag_overrides", {}):
        return cfg["tag_overrides"][version]
    fmt = cfg.get("tag_format")
    return fmt.format(version=version) if fmt else None


# --------------------------------------------------------------------------
# PR description block
# --------------------------------------------------------------------------

def extract_block(tag: str, body: str) -> str:
    """Text between <!-- TAG --> and <!-- /TAG --> in a PR description."""
    m = re.search(rf"<!--\s*{tag}\s*-->(.*?)<!--\s*/{tag}\s*-->", body, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


# List item marker: "-", "*", "+" or "1." / "1)", followed by a space or
# the end of the line (empty item).
LIST_ITEM_RE = re.compile(r"^( *)([-*+]|\d{1,9}[.)])(?: +|$)")
TASK_BOX_RE = re.compile(r"^\[[ xX]\] +")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?: +(.*?))?(?: +#+)? *$")
THEMATIC_BREAK_RE = re.compile(r"^ {0,3}(?:(?:- *){3,}|(?:\* *){3,}|(?:_ *){3,}|=+ *)$")
FENCE_RE = re.compile(r"^ *(```|~~~)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
BLOCKQUOTE_RE = re.compile(r"^(?: {0,3}> ?)+")
# "[vehicles] text"; not a Markdown link ("[x](url)", "[x][ref]", "[x]: url")
AREA_PREFIX_RE = re.compile(r"^\[([^\]\s]+)\](?![(\[:])\s*")


def split_items(text: str) -> list[dict]:
    """Split Markdown text into list items: [{"heading": str | None, "lines": [...]}].

    "heading" is the text of the last heading above the item. "lines" are the
    item's display lines:

    - a top-level list item ("-", "*", "+", "1.", "1)") opens a new item; a
      task box ("[ ]", "[x]") after the marker is dropped;
    - a nested list item becomes a line of the current item;
    - a wrapped line (no blank line before it) is joined to the line above with
      a space, as Markdown renders it, unless that line ends with a hard break
      (two spaces or a backslash);
    - after a blank line, an indented paragraph is a line of the current item,
      an unindented one a new item;
    - in text with no list item at all, every line is its own item;
    - blockquote markers (">"), thematic breaks, HTML comments and code fences
      are dropped; lines inside a code block become lines in inline code.
    """
    text = HTML_COMMENT_RE.sub("", text)
    raw_lines = [BLOCKQUOTE_RE.sub("", l.expandtabs(4).rstrip("\r")) for l in text.splitlines()]
    has_list = any(LIST_ITEM_RE.match(l) and l.strip() not in "-*+" for l in raw_lines
                   if not THEMATIC_BREAK_RE.match(l))

    items: list[dict] = []
    heading = None
    content_col = 0  # column where the current top-level item's text starts
    after_blank = False
    hard_break = False
    in_fence = False

    def new_item(lines: list[str]) -> None:
        items.append({"heading": heading, "lines": lines})

    for raw in raw_lines:
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            if raw.strip() and items and items[-1]:
                items[-1]["lines"].append(f"`{raw.strip()}`")
            continue

        if not raw.strip() or THEMATIC_BREAK_RE.match(raw):
            after_blank = True
            continue
        h = HEADING_RE.match(raw)
        if h:
            heading = (h.group(2) or "").strip()
            after_blank = True
            # A list below a heading starts afresh
            items.append(None)
            continue

        ends_hard = raw.endswith("  ") or raw.rstrip().endswith("\\")
        raw = raw.rstrip().removesuffix("\\").rstrip()
        line = raw.lstrip(" ")
        indent = len(raw) - len(line)
        current = items[-1] if items else None

        m = LIST_ITEM_RE.match(raw)
        if m:
            item = TASK_BOX_RE.sub("", raw[m.end():].strip())
            if current and indent >= content_col:
                if item:
                    current["lines"].append(item)
            else:
                content_col = m.end() if raw[m.end():].strip() else indent + 2
                new_item([item] if item else [])
        elif not current or not has_list or (after_blank and indent == 0):
            content_col = 1  # a list right below a paragraph is not nested in it
            new_item([line])
        elif after_blank or hard_break or not current["lines"]:
            current["lines"].append(line)
        else:
            current["lines"][-1] += " " + line

        after_blank = False
        hard_break = ends_hard

    return [i for i in items if i and i["lines"]]


def _type_key(heading: str) -> str | None:
    h = heading.strip().lower()
    for key, labels in TYPES.items():
        if h in (key, labels["en"].lower(), labels["fr"].lower()):
            return key
    return None


def _area_key(cfg: dict, name: str) -> str | None:
    n = name.strip().lower()
    for key, labels in cfg["areas"].items():
        if n in (key, labels["en"].lower(), labels["fr"].lower()):
            return key
    return None


def _excerpt(text: str) -> str:
    first = text.split("\n")[0]
    return first if len(first) <= 60 else first[:57] + "…"


def parse_block(text: str, cfg: dict, strict: bool) -> tuple[list[dict], list[str]]:
    """Parse a PR changelog block into entries.

    Items left as the PR template's placeholder ("[area]" alone) are skipped.
    Returns (entries, errors). Each error is a message for the PR author. With
    strict=False (merge time), entries with errors are still returned: unknown
    or missing type → FALLBACK_TYPE, missing area → FALLBACK_AREA, unknown
    area → its key as written.
    """
    entries: list[dict] = []
    errors: list[str] = []
    type_names = ", ".join(f"### {t['en']}" for t in TYPES.values())
    area_names = ", ".join(f"[{k}]" for k in cfg["areas"])

    for item in split_items(text):
        lines = list(item["lines"])
        where = f'"{_excerpt(lines[0])}"'
        m = AREA_PREFIX_RE.match(lines[0])
        # An item with an area and no text: the template's unfilled placeholder
        if m and not lines[0][m.end():].strip() and len(lines) == 1:
            continue

        if item["heading"] is None:
            errors.append(f"{where} is not under a type heading ({type_names}).")
            type_ = FALLBACK_TYPE
        else:
            type_ = _type_key(item["heading"])
            if type_ is None:
                close = difflib.get_close_matches(
                    item["heading"].strip().capitalize(), [t["en"] for t in TYPES.values()], n=1)
                hint = f' Did you mean "### {close[0]}"?' if close else ""
                errors.append(f'Unknown heading "### {item["heading"]}" above {where}.{hint} Use {type_names}.')
                type_ = FALLBACK_TYPE

        if m:
            area = _area_key(cfg, m.group(1))
            if area is None:
                names = list(cfg["areas"])
                close = difflib.get_close_matches(m.group(1).lower(), names, n=1)
                hint = f' Did you mean "[{close[0]}]"?' if close else ""
                errors.append(f'Unknown area "[{m.group(1)}]" in {where}.{hint} Areas: {area_names}.')
                area = m.group(1).lower()
            lines[0] = lines[0][m.end():]
        else:
            errors.append(f"{where} has no area: start it with one of {area_names}.")
            area = FALLBACK_AREA

        if not lines[0].strip():
            lines = lines[1:]
        entries.append({"type": type_, "area": area, "text": "\n".join(lines)})

    return entries, errors


def compare_languages(en: list[dict], fr: list[dict]) -> list[str]:
    """Errors when the FR entries do not match the EN ones (count, type, area)."""
    if len(en) != len(fr):
        return [f"The FR block has {len(fr)} entries, the EN block {len(en)}: "
                "translate every EN entry, in the same order."]
    errors = []
    for i, (e, f) in enumerate(zip(en, fr), 1):
        if (e["type"], e["area"]) != (f["type"], f["area"]):
            errors.append(
                f'Entry {i}: EN is {TYPES[e["type"]]["en"]} [{e["area"]}], '
                f'FR is {TYPES[f["type"]]["en"]} [{f["area"]}]: same type and area expected.'
            )
    return errors


# --------------------------------------------------------------------------
# CHANGELOG files
# --------------------------------------------------------------------------

BOLD_LABEL_RE = re.compile(r"^\*\*(.+?)\*\* ?: (.*)$")


def render_bullet(cfg: dict, entry: dict, lang: str) -> list[str]:
    lines = entry["text"].split("\n")
    label = area_labels(cfg, entry["area"], lang)
    if label:
        sep = " : " if lang == "fr" else ": "
        lines[0] = f"**{label}**{sep}{lines[0]}"
    return [f"- {lines[0]}\n"] + [f"  {l}\n" for l in lines[1:]]


def _parse_bullet(cfg: dict, lines: list[str], type_: str | None) -> dict:
    first = lines[0]
    area = None
    m = BOLD_LABEL_RE.match(first)
    if m:
        label = m.group(1)
        area = _area_key(cfg, label)
        if area is None and label.lower() in (l.lower() for l in FALLBACK_AREA_LABELS.values()):
            area = FALLBACK_AREA
        if area is not None:
            first = m.group(2)
    return {"type": type_, "area": area, "text": "\n".join([first] + lines[1:])}


def parse_section_lines(cfg: dict, lines: list[str]) -> list[dict]:
    """Entries of the body of a "## " section (the lines after its header)."""
    entries = []
    type_ = None
    current: list[str] | None = None

    def flush() -> None:
        nonlocal current
        if current:
            entries.append(_parse_bullet(cfg, current, type_))
        current = None

    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith("### "):
            flush()
            type_ = _type_key(stripped[4:])
        elif stripped.startswith(("- ", "* ")):
            flush()
            current = [stripped[2:].strip()]
        elif line.startswith("  ") and stripped and current is not None:
            current.append(stripped.strip())
        elif stripped:
            flush()
    flush()
    return entries


def render_section_body(cfg: dict, entries: list[dict], lang: str) -> list[str]:
    """Lines of a section body: one "### Type" group per type, then the
    entries without a type under UNTYPED_HEADING (no heading when no entry
    has a type), each group followed by a blank line."""
    out: list[str] = ["\n"]
    typed = any(e["type"] is not None for e in entries)
    for type_ in [*TYPES, None]:
        group = [e for e in entries if e["type"] == type_]
        if not group:
            continue
        if type_ is not None:
            out += [f"### {TYPES[type_]['en']}\n", "\n"]
        elif typed:
            out += [f"### {UNTYPED_HEADING}\n", "\n"]
        for e in group:
            out += render_bullet(cfg, e, lang)
        out.append("\n")
    return out


def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return f.readlines()


def write_lines(path: str, lines: list[str]) -> None:
    # One trailing newline, no trailing blank lines
    while lines and not lines[-1].strip():
        lines.pop()
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def section_end(lines: list[str], start: int) -> int:
    """Index of the line ending the section whose header is at start: the next
    "## " header, the link reference block, or the end of the file."""
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## ") or LINK_REF_RE.match(lines[i]):
            return i
    return len(lines)


def find_unreleased(lines: list[str]) -> int | None:
    for i, line in enumerate(lines):
        if line.rstrip() in UNRELEASED_HEADERS:
            return i
    return None


def parse_changelog(cfg: dict, path: str) -> list[dict]:
    """Sections of a CHANGELOG file, in file order:
    [{"version": None | str, "date": str | None, "yanked": bool, "entries": [...]}]
    (version None: the unreleased section)."""
    if not os.path.isfile(path):
        return []
    lines = read_lines(path)
    sections = []
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        m = VERSION_HEADER_RE.match(stripped)
        if stripped in UNRELEASED_HEADERS:
            section = {"version": None, "date": None, "yanked": False}
        elif m:
            section = {"version": m["version"], "date": m["date"], "yanked": bool(m["yanked"])}
        else:
            continue
        section["entries"] = parse_section_lines(cfg, lines[i + 1:section_end(lines, i)])
        sections.append(section)
    return sections


def update_links(cfg: dict, path: str, lang: str) -> None:
    """Rewrite the link references at the end of the file (Keep a Changelog:
    versions are linkable). Only for components with a tag convention."""
    if not cfg.get("tag_format") or not os.path.isfile(path):
        return
    lines = read_lines(path)
    while lines and (not lines[-1].strip() or LINK_REF_RE.match(lines[-1])):
        lines.pop()

    versions = [m["version"] for m in (VERSION_HEADER_RE.match(l.rstrip()) for l in lines) if m]
    base = f"https://github.com/{cfg['repo']}"
    refs = []
    if versions and find_unreleased(lines) is not None:
        refs.append(f"[{UNRELEASED_LABELS[lang].lower()}]: {base}/compare/{tag_for(cfg, versions[0])}...HEAD\n")
    for i, version in enumerate(versions):
        refs.append(f"[{version}]: {release_url(cfg, versions, i)}\n")

    write_lines(path, lines + ["\n"] + refs if refs else lines)


def release_url(cfg: dict, versions: list[str], index: int) -> str | None:
    """Compare URL of versions[index] (versions newest first), its tag page
    for the oldest one, None without a tag convention."""
    if not cfg.get("tag_format"):
        return None
    base = f"https://github.com/{cfg['repo']}"
    tag = tag_for(cfg, versions[index])
    if index + 1 < len(versions):
        return f"{base}/compare/{tag_for(cfg, versions[index + 1])}...{tag}"
    return f"{base}/releases/tag/{tag}"
