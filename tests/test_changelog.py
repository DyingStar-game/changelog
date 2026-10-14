"""
Tests of the changelog scripts (ADR 0001).

Run from the repository root:
    python3 -m unittest discover -s tests -v
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS = os.path.join(REPO_ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

import changelog_lib as lib  # noqa: E402

CONFIG = lib.load_config()
DS = CONFIG["DyingStar"]
LAUNCHER = CONFIG["launcher"]

HEADER = {
    "en": "# Changelog\n\nAll notable changes.\n\n",
    "fr": "# Changelog\n\nToutes les modifications.\n\n",
}


def lines_of(text: str) -> list[list[str]]:
    return [i["lines"] for i in lib.split_items(text)]


def entry(type_, area, text):
    return {"type": type_, "area": area, "text": text}


class TempRepo:
    """A copy of the scripts and components.json, with CHANGELOG files to fill."""

    def __init__(self) -> None:
        self.root = tempfile.mkdtemp()
        shutil.copytree(SCRIPTS, os.path.join(self.root, "scripts"),
                        ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy(os.path.join(REPO_ROOT, "components.json"), self.root)
        for component in CONFIG:
            os.makedirs(os.path.join(self.root, component))
            for lang in lib.LANGS:
                self.write(component, lang, f"## [{lib.UNRELEASED_LABELS[lang]}]\n")

    def path(self, component: str, lang: str) -> str:
        return os.path.join(self.root, component, lib.FILES[lang])

    def write(self, component: str, lang: str, body: str) -> None:
        with open(self.path(component, lang), "w", encoding="utf-8") as f:
            f.write(HEADER[lang] + body)

    def read(self, component: str, lang: str) -> str:
        with open(self.path(component, lang), encoding="utf-8") as f:
            return f.read()

    def body(self, component: str, lang: str) -> str:
        return self.read(component, lang)[len(HEADER[lang]):]

    def run(self, script: str, *args: str, env: dict | None = None) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, os.path.join(self.root, "scripts", script), *args],
            capture_output=True, text=True, env={**os.environ, **(env or {})},
        )

    def cleanup(self) -> None:
        shutil.rmtree(self.root)


class RepoTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = TempRepo()
        self.addCleanup(self.repo.cleanup)


# --------------------------------------------------------------------------
# Markdown → items
# --------------------------------------------------------------------------

class SplitItemsTest(unittest.TestCase):
    def test_list_markers(self):
        self.assertEqual(lines_of("- a\n* b\n+ c\n1. d\n2) e"), [["a"], ["b"], ["c"], ["d"], ["e"]])

    def test_crlf(self):
        self.assertEqual(lines_of("\r\n- a\r\n- b\r\n"), [["a"], ["b"]])

    def test_tab_after_marker(self):
        self.assertEqual(lines_of("-\ta\n-\tb"), [["a"], ["b"]])

    def test_wrapped_line_joined(self):
        self.assertEqual(lines_of("- uses the\n  token's `sub`.\n- next"),
                         [["uses the token's `sub`."], ["next"]])

    def test_lazy_continuation_joined(self):
        self.assertEqual(lines_of("- one\ntwo\n- next"), [["one two"], ["next"]])

    def test_hard_breaks(self):
        self.assertEqual(lines_of("- a  \n  b\n- c\\\n  d"), [["a", "b"], ["c", "d"]])

    def test_nested_items_are_sub_lines(self):
        self.assertEqual(lines_of("- Parent\n  - one\n    - deep\n  - two\n- Next"),
                         [["Parent", "one", "deep", "two"], ["Next"]])

    def test_nested_under_ordered_item(self):
        self.assertEqual(lines_of("1. Parent\n   - child\n2. Next"), [["Parent", "child"], ["Next"]])

    def test_indented_paragraph_is_sub_line(self):
        self.assertEqual(lines_of("- Item\n\n  More detail\n- Next"), [["Item", "More detail"], ["Next"]])

    def test_paragraph_after_list_is_new_item(self):
        self.assertEqual(lines_of("- a\n\nA note"), [["a"], ["A note"]])

    def test_list_below_paragraph_is_not_nested(self):
        self.assertEqual(lines_of("Changes:\n- x\n- y"), [["Changes:"], ["x"], ["y"]])

    def test_plain_lines_without_list(self):
        self.assertEqual(lines_of("Rewrite code\nPlanet tech v1"), [["Rewrite code"], ["Planet tech v1"]])

    def test_task_boxes_dropped(self):
        self.assertEqual(lines_of("- [x] done\n- [ ] todo"), [["done"], ["todo"]])

    def test_dropped_markup(self):
        text = "<!-- a comment -->\n- a\n---\n> - b\n***\n- c"
        self.assertEqual(lines_of(text), [["a"], ["b"], ["c"]])

    def test_empty_items_dropped(self):
        self.assertEqual(lines_of("-\n- a\n- "), [["a"]])

    def test_leading_dash_in_text_kept(self):
        self.assertEqual(lines_of("- -5% lag\n- --flag added"), [["-5% lag"], ["--flag added"]])

    def test_code_block(self):
        self.assertEqual(lines_of("- Config:\n```\nkey = 1\n- not an item\n```\n- Next"),
                         [["Config:", "`key = 1`", "`- not an item`"], ["Next"]])

    def test_headings(self):
        items = lib.split_items("- before\n### Added\n- a\n## Fixed ##\n- b")
        self.assertEqual([(i["heading"], i["lines"]) for i in items],
                         [(None, ["before"]), ("Added", ["a"]), ("Fixed", ["b"])])

    def test_list_after_heading_not_nested_in_previous_item(self):
        items = lib.split_items("### Added\n- a\n### Fixed\n  - b")
        self.assertEqual([i["lines"] for i in items], [["a"], ["b"]])


# --------------------------------------------------------------------------
# PR block → entries
# --------------------------------------------------------------------------

class ParseBlockTest(unittest.TestCase):
    def parse(self, text, strict=True, cfg=DS):
        return lib.parse_block(textwrap.dedent(text), cfg, strict)

    def test_valid_block(self):
        entries, errors = self.parse("""\
            ### Added
            - [vehicles] New dashboard:
              - speed
            - [ui] Hints moved.
            ### Fixed
            - [planettech] Ground texture.
            """)
        self.assertEqual(errors, [])
        self.assertEqual(entries, [
            entry("added", "vehicles", "New dashboard:\nspeed"),
            entry("added", "ui", "Hints moved."),
            entry("fixed", "planettech", "Ground texture."),
        ])

    def test_type_and_area_names_are_case_insensitive_and_accept_labels(self):
        entries, errors = self.parse("### fixed\n- [PlanetTech] a\n### Corrections\n- [Véhicules] b")
        self.assertEqual(errors, [])
        self.assertEqual([(e["type"], e["area"]) for e in entries],
                         [("fixed", "planettech"), ("fixed", "vehicles")])

    def test_entry_without_type(self):
        entries, errors = self.parse("- [ui] a")
        self.assertEqual(len(errors), 1)
        self.assertIn("not under a type heading", errors[0])

    def test_unknown_type_suggests_the_closest(self):
        _, errors = self.parse("### Fixes\n- [ui] a")
        self.assertIn('Did you mean "### Fixed"?', errors[0])

    def test_entry_without_area(self):
        _, errors = self.parse("### Fixed\n- a")
        self.assertIn("has no area", errors[0])

    def test_unknown_area_suggests_the_closest(self):
        _, errors = self.parse("### Fixed\n- [vehicle] a")
        self.assertIn('Did you mean "[vehicles]"?', errors[0])

    def test_markdown_link_is_not_an_area(self):
        _, errors = self.parse("### Fixed\n- [the wiki](https://x) a\n- [ref][1] b")
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("has no area" in e for e in errors))

    def test_template_placeholders_skipped(self):
        self.assertEqual(self.parse("### Added\n- [area] \n### Fixed\n- [area]"), ([], []))

    def test_area_alone_with_sub_lines(self):
        entries, errors = self.parse("### Fixed\n- [ui]\n  - a\n  - b")
        self.assertEqual(errors, [])
        self.assertEqual(entries, [entry("fixed", "ui", "a\nb")])

    def test_lenient_fallbacks(self):
        entries, errors = self.parse("- no type, no area\n### Nope\n- [unknown] text", strict=False)
        self.assertEqual(len(errors), 4)
        self.assertEqual(entries, [
            entry(lib.FALLBACK_TYPE, lib.FALLBACK_AREA, "no type, no area"),
            entry(lib.FALLBACK_TYPE, "unknown", "text"),
        ])

    def test_compare_languages(self):
        en = [entry("added", "ui", "a"), entry("fixed", "ui", "b")]
        self.assertEqual(lib.compare_languages(en, [entry("added", "ui", "x"), entry("fixed", "ui", "y")]), [])
        self.assertIn("1 entries", lib.compare_languages(en, en[:1])[0])
        errors = lib.compare_languages(en, [entry("added", "ui", "x"), entry("fixed", "audio", "y")])
        self.assertEqual(len(errors), 1)
        self.assertIn("Entry 2", errors[0])

    def test_extract_block(self):
        body = "x\n<!-- CHANGELOG_EN -->\n- a\n<!-- /CHANGELOG_EN -->\n<!--changelog_fr-->- b<!-- /CHANGELOG_FR -->"
        self.assertEqual(lib.extract_block("CHANGELOG_EN", body), "- a")
        self.assertEqual(lib.extract_block("CHANGELOG_FR", body), "- b")
        self.assertEqual(lib.extract_block("CHANGELOG_EN", "nothing"), "")


# --------------------------------------------------------------------------
# CHANGELOG files
# --------------------------------------------------------------------------

class RenderTest(unittest.TestCase):
    ENTRIES = [
        entry("fixed", "vehicles", "Second\nsub-line"),
        entry("added", "ui", "First"),
        entry(None, None, "Legacy\n  indented"),
        entry("changed", lib.FALLBACK_AREA, "General one"),
    ]

    def test_render(self):
        self.assertEqual("".join(lib.render_section_body(DS, self.ENTRIES, "fr")), textwrap.dedent("""
            ### Added

            - **Interface** : First

            ### Changed

            - **Général** : General one

            ### Fixed

            - **Véhicules** : Second
              sub-line

            ### Uncategorized

            - Legacy
                indented

            """))

    def test_untyped_only_has_no_heading(self):
        self.assertEqual("".join(lib.render_section_body(DS, [entry(None, None, "a")], "en")), "\n- a\n\n")

    def test_round_trip(self):
        for lang in lib.LANGS:
            body = lib.render_section_body(DS, self.ENTRIES, lang)
            parsed = lib.parse_section_lines(DS, body)
            order = [*lib.TYPES, None]
            expected = sorted(self.ENTRIES, key=lambda e: order.index(e["type"]))
            # Sub-lines are read back without their indentation
            expected = [{**e, "text": "\n".join(l.strip() for l in e["text"].split("\n"))} for e in expected]
            self.assertEqual(parsed, expected, lang)

    def test_unknown_bold_label_stays_in_text(self):
        self.assertEqual(lib.parse_section_lines(DS, ["- **Note**: text\n"]),
                         [entry(None, None, "**Note**: text")])


class AppendEntryTest(RepoTestCase):
    def append(self, *args):
        return self.repo.run("append_entry.py", "--component", "DyingStar", *args)

    def test_entries_grouped_by_type_newest_first(self):
        self.repo.write("DyingStar", "en", "## [Unreleased]\n\n## [0.0.1] - 2025-01-01\n\n- old\n")
        self.repo.write("DyingStar", "fr", "## [Non publié]\n")
        r = self.append("--entry-en=### Fixed\n- [ui] fix 1\n### Added\n- [vehicles] add 1",
                        "--entry-fr=### Fixed\n- [ui] corr 1\n### Added\n- [vehicles] ajout 1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.append("--entry-en=### Fixed\n- [audio] fix 2")
        self.assertEqual(self.repo.body("DyingStar", "en"), textwrap.dedent("""\
            ## [Unreleased]

            ### Added

            - **Vehicles**: add 1

            ### Fixed

            - **Audio**: fix 2
            - **Interface**: fix 1

            ## [0.0.1] - 2025-01-01

            - old
            """))
        # FR falls back to EN when the PR has no FR block
        self.assertIn("- **Audio** : fix 2\n- **Interface** : corr 1\n", self.repo.body("DyingStar", "fr"))

    def test_legacy_entries_kept_last(self):
        legacy = "- legacy one\n  its second line\n- legacy two\n"
        self.repo.write("DyingStar", "en", "## [Unreleased]\n" + legacy + "## [0.0.1] - 2025-01-01\n")
        self.append("--entry-en=### Fixed\n- [ui] new")
        self.assertEqual(self.repo.body("DyingStar", "en"), textwrap.dedent("""\
            ## [Unreleased]

            ### Fixed

            - **Interface**: new

            ### Uncategorized

            """) + legacy + "\n## [0.0.1] - 2025-01-01\n")

    def test_link_references_stay_last(self):
        self.repo.write("launcher", "en", "## [Unreleased]\n\n## [1.0.0] - 2026-01-01\n\n- a\n\n"
                        "[unreleased]: https://x/compare/v1.0.0...HEAD\n[1.0.0]: https://x/releases/tag/v1.0.0\n")
        self.repo.run("append_entry.py", "--component", "launcher", "--entry-en=### Added\n- [ui] b")
        body = self.repo.body("launcher", "en")
        self.assertTrue(body.endswith("[1.0.0]: https://x/releases/tag/v1.0.0\n"))
        self.assertIn("- **Interface**: b\n\n## [1.0.0]", body)

    def test_merged_with_errors_is_still_recorded(self):
        r = self.append("--entry-en=- no type, no area")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("::warning", r.stdout)
        self.assertIn("### Changed\n\n- **General**: no type, no area\n", self.repo.body("DyingStar", "en"))

    def test_text_starting_with_a_dash(self):
        r = self.append("--entry-en=-fix")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("- **General**: -fix\n", self.repo.body("DyingStar", "en"))

    def test_unfilled_template_adds_nothing(self):
        before = self.repo.read("DyingStar", "en")
        r = self.append("--entry-en=### Added\n- [area] \n### Fixed\n- [area] ")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.repo.read("DyingStar", "en"), before)

    def test_unknown_component(self):
        self.assertEqual(self.repo.run("append_entry.py", "--component", "nope", "--entry-en=x").returncode, 1)


class CutReleaseTest(RepoTestCase):
    def cut(self, component, version, date="2026-10-14"):
        return self.repo.run("cut_release.py", "--component", component, "--version", version, "--date", date)

    def test_cut(self):
        self.repo.write("DyingStar", "en", "## [Unreleased]\n\n### Fixed\n\n- **Interface**: a\n")
        self.repo.write("DyingStar", "fr", "## [Non publié]\n\n### Fixed\n\n- **Interface** : a\n")
        r = self.cut("DyingStar", "0.1.0-test.6+build.1")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.repo.body("DyingStar", "en"),
                         "## [Unreleased]\n\n## [0.1.0-test.6+build.1] - 2026-10-14\n\n### Fixed\n\n- **Interface**: a\n")
        self.assertTrue(self.repo.body("DyingStar", "fr").startswith(
            "## [Non publié]\n\n## [0.1.0-test.6+build.1] - 2026-10-14\n"))
        # No tag convention: no links
        self.assertNotIn("]: ", self.repo.read("DyingStar", "en"))

    def test_invalid_input(self):
        for version, date in [("1.0", "2026-10-14"), ("v1.0.0", "2026-10-14"), ("01.0.0", "2026-10-14"),
                              ("1.0.0", "14/10/2026")]:
            self.assertEqual(self.cut("DyingStar", version, date).returncode, 1, version)

    def test_existing_version_refused(self):
        self.assertEqual(self.cut("DyingStar", "1.0.0").returncode, 0)
        r = self.cut("DyingStar", "1.0.0")
        self.assertEqual(r.returncode, 1)
        self.assertIn("already", r.stderr)

    def test_links(self):
        self.repo.write("launcher", "en", "## [Unreleased]\n\n- c\n\n## [0.2.0] - 2026-02-01\n\n- b\n\n"
                        "## [0.1.0] - 2026-01-01\n\n- a\n\n[unreleased]: https://stale\n")
        self.assertEqual(self.cut("launcher", "0.3.0").returncode, 0)
        base = "https://github.com/DyingStar-game/launcher"
        refs = (f"[unreleased]: {base}/compare/v0.3.0...HEAD\n"
                f"[0.3.0]: {base}/compare/v0.2.0...v0.3.0\n"
                f"[0.2.0]: {base}/compare/0.1.0...v0.2.0\n"  # tag_overrides
                f"[0.1.0]: {base}/releases/tag/0.1.0\n")
        self.assertTrue(self.repo.read("launcher", "en").endswith("- a\n\n" + refs))
        self.assertIn("[non publié]: ", self.repo.read("launcher", "fr"))
        # Rewriting gives the same result
        lib.update_links(LAUNCHER, self.repo.path("launcher", "en"), "en")
        self.assertTrue(self.repo.read("launcher", "en").endswith("- a\n\n" + refs))


class GenerateGlobalJsonTest(RepoTestCase):
    def generate(self) -> dict:
        r = self.repo.run("generate_global_json.py")
        self.assertEqual(r.returncode, 0, r.stderr)
        with open(os.path.join(self.repo.root, "global.v2.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_schema(self):
        self.repo.write("launcher", "en", textwrap.dedent("""\
            ## [Unreleased]

            ### Fixed

            - **Download and install**: resumes
              after a restart

            ## [0.2.0] - 2026-02-01 [YANKED]

            - legacy

            ## [0.1.0] - 2026-01-01

            ### Added

            - **General**: first
            """))
        self.repo.write("launcher", "fr", "## [Non publié]\n\n### Fixed\n\n- **Téléchargement et installation** : reprend\n")
        data = self.generate()
        self.assertEqual(data["schema_version"], 2)
        self.assertEqual(list(data["types"]), list(lib.TYPES))
        c = data["components"]["launcher"]
        self.assertEqual(c["repo"], "DyingStar-game/launcher")
        self.assertIn("download", c["areas"])
        self.assertIn(lib.FALLBACK_AREA, c["areas"])
        self.assertEqual(c["unreleased"], {
            "url": "https://github.com/DyingStar-game/launcher/compare/v0.2.0...HEAD",
            "entries": {"en": [entry("fixed", "download", "resumes\nafter a restart")],
                        "fr": [entry("fixed", "download", "reprend")]},
        })
        self.assertEqual([(r["version"], r["date"], r["yanked"]) for r in c["releases"]],
                         [("0.2.0", "2026-02-01", True), ("0.1.0", "2026-01-01", False)])
        self.assertEqual(c["releases"][0]["url"], "https://github.com/DyingStar-game/launcher/compare/0.1.0...v0.2.0")
        self.assertEqual(c["releases"][0]["entries"]["en"], [entry(None, None, "legacy")])
        # Version missing from the FR file: EN entries
        self.assertEqual(c["releases"][1]["entries"]["fr"], [entry("added", "general", "first")])
        self.assertIsNone(data["components"]["DyingStar"]["unreleased"]["url"])


class CheckEntryTest(RepoTestCase):
    def check(self, body, component="DyingStar"):
        return self.repo.run("check_entry.py", "--component", component, env={"PR_BODY": body})

    def body(self, en, fr=""):
        return (f"## Description\n\n<!-- CHANGELOG_EN -->\n{en}\n<!-- /CHANGELOG_EN -->\n\n"
                f"<!-- CHANGELOG_FR -->\n{fr}\n<!-- /CHANGELOG_FR -->\n")

    def test_valid(self):
        r = self.check(self.body("### Added\n- [ui] a\n### Fixed\n- [audio] b",
                                 "### Added\n- [ui] x\n### Fixed\n- [audio] y"))
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("- **Interface**: a", r.stdout)
        self.assertIn("- **Audio** : y", r.stdout)

    def test_errors(self):
        r = self.check(self.body("- [vehicle] a"))
        self.assertEqual(r.returncode, 1)
        self.assertEqual(r.stdout.count("::error"), 2)

    def test_fr_must_match_en(self):
        r = self.check(self.body("### Added\n- [ui] a\n- [ui] b", "### Added\n- [ui] x"))
        self.assertEqual(r.returncode, 1)
        self.assertIn("translate every EN entry", r.stdout)

    def test_fr_without_en(self):
        self.assertEqual(self.check(self.body("", "### Added\n- [ui] x")).returncode, 1)
        self.assertEqual(self.check(self.body("### Added\n- [area] ", "### Added\n- [ui] x")).returncode, 1)

    def test_no_entry(self):
        for body in ["No changelog blocks", self.body(""), self.body("### Added\n- [area] \n### Fixed\n- [area] ")]:
            r = self.check(body)
            self.assertEqual(r.returncode, 0, body)
            self.assertIn("No changelog entry", r.stdout)

    def test_pr_template_passes(self):
        with open(os.path.join(REPO_ROOT, "integration", "PULL_REQUEST_TEMPLATE.md"), encoding="utf-8") as f:
            self.assertEqual(self.check(f.read()).returncode, 0)

    def test_body_file_and_summary(self):
        body_file = os.path.join(self.repo.root, "body.md")
        summary = os.path.join(self.repo.root, "summary.md")
        with open(body_file, "w", encoding="utf-8") as f:
            f.write(self.body("### Fixed\n- [ui] a"))
        r = self.repo.run("check_entry.py", "--component", "DyingStar", "--body-file", body_file,
                          env={"GITHUB_STEP_SUMMARY": summary})
        self.assertEqual(r.returncode, 0)
        with open(summary, encoding="utf-8") as f:
            self.assertIn("Changelog: OK", f.read())

    def test_list_areas(self):
        r = self.repo.run("check_entry.py", "--component", "DyingStar", "--list-areas")
        self.assertEqual(r.returncode, 0)
        self.assertIn("[vehicles]  Vehicles / Véhicules", r.stdout)


# --------------------------------------------------------------------------
# Repository data
# --------------------------------------------------------------------------

class RepositoryTest(unittest.TestCase):
    def test_config(self):
        for component, cfg in CONFIG.items():
            self.assertTrue(os.path.isdir(os.path.join(REPO_ROOT, component)), component)
            self.assertRegex(cfg["repo"], r"^DyingStar-game/[\w.-]+$")
            self.assertTrue(cfg["areas"], component)
            self.assertNotIn(lib.FALLBACK_AREA, cfg["areas"])
            labels = {"en": set(), "fr": set()}
            for key, area in cfg["areas"].items():
                self.assertRegex(key, r"^[a-z0-9]+(-[a-z0-9]+)*$")
                for lang in lib.LANGS:
                    self.assertTrue(area[lang], f"{component} {key} {lang}")
                    self.assertNotIn(area[lang], labels[lang], f"{component}: duplicate label")
                    labels[lang].add(area[lang])
            if "tag_format" in cfg:
                self.assertIn("{version}", cfg["tag_format"])

    def test_changelog_files_parse_and_survive_a_rewrite(self):
        for component, cfg in CONFIG.items():
            for lang in lib.LANGS:
                path = os.path.join(REPO_ROOT, component, lib.FILES[lang])
                lines = lib.read_lines(path)
                start = lib.find_unreleased(lines)
                self.assertIsNotNone(start, path)
                end = lib.section_end(lines, start)
                before = lib.parse_section_lines(cfg, lines[start + 1:end])
                body = lib.render_section_body(cfg, before, lang)
                self.assertEqual(lib.parse_section_lines(cfg, body), before, path)

    def test_global_v2_json_is_up_to_date(self):
        repo = TempRepo()
        self.addCleanup(repo.cleanup)
        for path in glob.glob(os.path.join(REPO_ROOT, "**", "CHANGELOG*.md"), recursive=True):
            shutil.copy(path, os.path.join(repo.root, os.path.relpath(path, REPO_ROOT)))
        self.assertEqual(repo.run("generate_global_json.py").returncode, 0)
        with open(os.path.join(repo.root, "global.v2.json"), encoding="utf-8") as f:
            generated = json.load(f)
        with open(os.path.join(REPO_ROOT, "global.v2.json"), encoding="utf-8") as f:
            committed = json.load(f)
        generated.pop("generated_at")
        committed.pop("generated_at")
        self.assertEqual(generated, committed, "global.v2.json is stale: run scripts/generate_global_json.py")

    def test_plugin_files(self):
        for path in [".claude-plugin/marketplace.json", "plugins/changelog/.claude-plugin/plugin.json"]:
            with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
                json.load(f)
        with open(os.path.join(REPO_ROOT, "plugins/changelog/skills/changelog-entry/SKILL.md"), encoding="utf-8") as f:
            front = re.match(r"^---\n(.*?)\n---\n", f.read(), re.DOTALL)
        self.assertIsNotNone(front)
        self.assertIn("name: changelog-entry", front.group(1))


if __name__ == "__main__":
    unittest.main()
