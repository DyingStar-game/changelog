#!/usr/bin/env python3
"""
Prepend a bullet entry under the [Unreleased] section
of a component's CHANGELOG.md and CHANGELOG.fr.md.

Usage:
    python3 scripts/append_entry.py \
        --component "services/monitoring" \
        --entry-en "fix crash on startup" \
        --entry-fr "correction du crash au démarrage"

If --entry-fr is empty or omitted, the EN text is used for the FR file.

Multi-line entries are stored as a single bullet with the lines joined
by a literal newline (continuation of the same list item in Markdown).
"""
import argparse
import os
import sys

COMPONENTS = [
    "DyingStar",
    "horizonserver",
    "services/monitoring",
    "services/persistence",
    "services/resourcesDynamic",
    "launcher",
]

# Both EN and FR unreleased headers are recognised so the script is robust
# to existing files using either convention.
UNRELEASED_HEADERS = {"## [Unreleased]", "## [Non publié]"}


def _bullets(text: str) -> list[str]:
    """Return a single-element list containing all non-empty lines joined by '\n'.

    Multiple lines in the PR body are kept as one bullet (continuation lines
    in Markdown) rather than being split into separate entries.
    """
    lines = []
    for raw in text.splitlines():
        line = raw.strip().lstrip("-* \t")
        if line:
            lines.append(line)
    if not lines:
        return []
    return ["\n  ".join(lines)]


def insert_entries(filepath: str, entries: list[str]) -> None:
    """Prepend bullet entries under the first recognised [Unreleased] header."""
    if not entries:
        return
    if not os.path.isfile(filepath):
        print(f"Warning: {filepath} not found, skipping.", file=sys.stderr)
        return

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_idx = None
    for i, line in enumerate(lines):
        if line.rstrip() in UNRELEASED_HEADERS:
            header_idx = i
            break

    if header_idx is None:
        print(f"Error: no unreleased header found in {filepath}", file=sys.stderr)
        sys.exit(1)

    # Find insertion point: right after the header (skip one blank line if present)
    insert_idx = header_idx + 1
    if insert_idx < len(lines) and lines[insert_idx].strip() == "":
        insert_idx += 1

    new_bullets = [f"- {e}\n" for e in entries]
    lines[insert_idx:insert_idx] = new_bullets

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Append changelog entries to [Unreleased].")
    parser.add_argument("--component", required=True,
                        help="Component key, e.g. 'DyingStar' or 'services/monitoring'")
    parser.add_argument("--entry-en", required=True, help="English entry text (may be multi-line)")
    parser.add_argument("--entry-fr", default="", help="French entry text (falls back to EN if empty)")
    args = parser.parse_args()

    if args.component not in COMPONENTS:
        print(
            f"Error: unknown component '{args.component}'.\nValid values: {COMPONENTS}",
            file=sys.stderr,
        )
        sys.exit(1)

    bullets_en = _bullets(args.entry_en)
    bullets_fr = _bullets(args.entry_fr) or bullets_en  # fallback to EN

    if not bullets_en:
        print("Error: --entry-en is empty after stripping.", file=sys.stderr)
        sys.exit(1)

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    comp_dir = os.path.join(repo_root, args.component)

    insert_entries(os.path.join(comp_dir, "CHANGELOG.md"), bullets_en)
    insert_entries(os.path.join(comp_dir, "CHANGELOG.fr.md"), bullets_fr)


if __name__ == "__main__":
    main()
