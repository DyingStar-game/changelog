#!/usr/bin/env python3
"""
Add the changelog entries of a merged PR to the [Unreleased] section of a
component's CHANGELOG.md and CHANGELOG.fr.md (ADR 0001).

Usage:
    python3 scripts/append_entry.py \
        --component "launcher" \
        --entry-en="### Fixed
- [download] The download resumes after a restart." \
        --entry-fr="### Fixed
- [download] Le téléchargement reprend après un redémarrage."

The entries text is the PR's CHANGELOG_EN / CHANGELOG_FR block (see
changelog_lib.parse_block). If --entry-fr is empty or omitted, the EN entries
are used for the FR file.

The PR check (check_entry.py) refuses a block with errors; one merged anyway
is still recorded (fallback type and area) and the errors printed as warnings.
New entries go first in their type group.
"""
import argparse
import os
import sys

import changelog_lib as lib


def insert_entries(cfg: dict, path: str, entries: list[dict], lang: str) -> None:
    if not os.path.isfile(path):
        print(f"Warning: {path} not found, skipping.", file=sys.stderr)
        return
    lines = lib.read_lines(path)
    start = lib.find_unreleased(lines)
    if start is None:
        print(f"Error: no unreleased header found in {path}", file=sys.stderr)
        sys.exit(1)
    end = lib.section_end(lines, start)
    existing = lib.parse_section_lines(cfg, lines[start + 1:end])
    body = lib.render_section_body(cfg, entries + existing, lang)
    lines[start + 1:end] = body
    lib.write_lines(path, lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Add a PR's changelog entries to [Unreleased].")
    parser.add_argument("--component", required=True,
                        help="Component key, e.g. 'DyingStar' or 'services/monitoring'")
    parser.add_argument("--entry-en", required=True, help="CHANGELOG_EN block of the PR")
    parser.add_argument("--entry-fr", default="", help="CHANGELOG_FR block (falls back to EN if empty)")
    args = parser.parse_args()

    config = lib.load_config()
    if args.component not in config:
        print(f"Error: unknown component '{args.component}'.\nValid values: {list(config)}",
              file=sys.stderr)
        sys.exit(1)
    cfg = config[args.component]

    entries = {}
    for lang, text in (("en", args.entry_en), ("fr", args.entry_fr)):
        entries[lang], errors = lib.parse_block(text, cfg, strict=False)
        for e in errors:
            print(f"::warning title=Changelog {lang.upper()}::{e}")
    if not entries["en"]:
        print("No entry in --entry-en (template left unfilled): nothing to add.")
        return
    if not entries["fr"]:
        entries["fr"] = entries["en"]

    comp_dir = os.path.join(lib.REPO_ROOT, args.component)
    for lang in lib.LANGS:
        insert_entries(cfg, os.path.join(comp_dir, lib.FILES[lang]), entries[lang], lang)


if __name__ == "__main__":
    main()
