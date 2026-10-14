#!/usr/bin/env python3
"""
Check the changelog block of a PR description (ADR 0001).

Usage:
    python3 scripts/check_entry.py --component DyingStar --body-file pr.md
    PR_BODY="..." python3 scripts/check_entry.py --component DyingStar
    python3 scripts/check_entry.py --component DyingStar --list-areas

Exits 1 when the block has errors, printed as GitHub annotations and, in
GitHub Actions, in the job summary. A PR without a CHANGELOG_EN block (no
player-visible change) passes. On success, prints the entries as they will
appear in CHANGELOG.md.
"""
import argparse
import os
import sys

import changelog_lib as lib


def summary(text: str) -> None:
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(text + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a PR's changelog block.")
    parser.add_argument("--component", required=True)
    parser.add_argument("--body-file", help="PR description file (default: $PR_BODY)")
    parser.add_argument("--list-areas", action="store_true", help="List the component's areas and types")
    args = parser.parse_args()

    config = lib.load_config()
    if args.component not in config:
        print(f"Error: unknown component '{args.component}'.\nValid: {list(config)}", file=sys.stderr)
        sys.exit(2)
    cfg = config[args.component]

    if args.list_areas:
        print("Types (### heading): " + ", ".join(t["en"] for t in lib.TYPES.values()))
        print("Areas ([key] at the start of each entry):")
        for key, labels in cfg["areas"].items():
            print(f"  [{key}]  {labels['en']} / {labels['fr']}")
        return

    if args.body_file:
        with open(args.body_file, encoding="utf-8") as f:
            body = f.read()
    else:
        body = os.environ.get("PR_BODY", "")

    block = {lang: lib.extract_block(f"CHANGELOG_{lang.upper()}", body) for lang in lib.LANGS}
    if not block["en"]:
        if block["fr"]:
            errors = ["The CHANGELOG_FR block is filled but CHANGELOG_EN is empty: EN is required."]
        else:
            print("No changelog entry: nothing player-visible in this PR.")
            summary("### Changelog\n\nNo entry in this PR.")
            return
    else:
        entries = {}
        errors = []
        for lang in lib.LANGS:
            if block[lang]:
                entries[lang], errs = lib.parse_block(block[lang], cfg, strict=True)
                errors += [f"{lang.upper()}: {e}" for e in errs]
        if not entries["en"] and not errors:
            if entries.get("fr"):
                errors.append("The CHANGELOG_FR block has entries but CHANGELOG_EN has none: EN is required.")
            else:
                print("No changelog entry: nothing player-visible in this PR.")
                summary("### Changelog\n\nNo entry in this PR.")
                return
        if not errors and entries.get("fr"):
            errors += lib.compare_languages(entries["en"], entries["fr"])

    if errors:
        for e in errors:
            print(f"::error title=Changelog::{e}")
        summary("### Changelog: errors\n\n" + "\n".join(f"- {e}" for e in errors)
                + "\n\nSee https://github.com/DyingStar-game/changelog/blob/main/docs/adr/0001-changelog-format.md")
        sys.exit(1)

    entries.setdefault("fr", entries["en"])
    preview = []
    for lang in lib.LANGS:
        preview.append(f"#### {lib.FILES[lang]}\n\n```markdown")
        preview.append("".join(lib.render_section_body(cfg, entries[lang], lang)).strip())
        preview.append("```\n")
    print("\n".join(preview))
    summary("### Changelog: OK\n\n" + "\n".join(preview))


if __name__ == "__main__":
    main()
