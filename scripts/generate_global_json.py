#!/usr/bin/env python3
"""
Parse all component CHANGELOG.md and CHANGELOG.fr.md files and emit
a single global.json at the repository root.

Schema:
{
  "generated_at": "<ISO-8601 UTC>",
  "components": {
    "<component>": {
      "unreleased": { "en": ["entry", ...], "fr": ["entrée", ...] },
      "releases": [
        { "version": "1.2.3", "date": "YYYY-MM-DD",
          "entries": { "en": [...], "fr": [...] } },
        ...
      ]
    },
    ...
  }
}

Releases are ordered newest-first (as they appear in CHANGELOG files).
The FR unreleased list falls back to the EN list if empty.
For each release, FR entries fall back to EN entries if the FR CHANGELOG
does not contain that version.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

COMPONENTS = [
    "DyingStar",
    "horizonserver",
    "services/monitoring",
    "services/persistence",
    "services/resourcesDynamic",
    "launcher",
]

UNRELEASED_HEADERS = {"## [Unreleased]", "## [Non publié]"}
VERSION_RE = re.compile(r"^## \[(.+)\] - (\d{4}-\d{2}-\d{2})\s*$")


def parse_changelog(filepath: str) -> tuple[list[str], list[dict]]:
    """
    Returns:
        unreleased  – list of bullet strings for the [Unreleased] section
        releases    – list of {"version": str, "date": str, "entries": [str, ...]}
                      ordered as they appear in the file (newest first)
    """
    if not os.path.isfile(filepath):
        return [], []

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    unreleased: list[str] = []
    releases: list[dict] = []
    # current_section: None | "unreleased" | dict (release block)
    current_section = None

    for line in lines:
        stripped = line.rstrip()

        if stripped in UNRELEASED_HEADERS:
            current_section = "unreleased"
            continue

        m = VERSION_RE.match(stripped)
        if m:
            if isinstance(current_section, dict):
                releases.append(current_section)
            current_section = {"version": m.group(1), "date": m.group(2), "entries": []}
            continue

        # Any other ## header closes the current section
        if stripped.startswith("## "):
            if isinstance(current_section, dict):
                releases.append(current_section)
            current_section = None
            continue

        # ### sub-section headers (e.g. ### Added) are skipped but we stay in the section
        if stripped.startswith("### "):
            continue

        # Collect bullet lines
        if stripped.startswith("- ") or stripped.startswith("* "):
            entry = stripped[2:].strip()
            if current_section == "unreleased":
                unreleased.append(entry)
            elif isinstance(current_section, dict):
                current_section["entries"].append(entry)

    # Flush the last open release block
    if isinstance(current_section, dict):
        releases.append(current_section)

    return unreleased, releases


def main() -> None:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    result: dict = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "components": {},
    }

    missing: list[str] = []
    for component in COMPONENTS:
        comp_dir = os.path.join(repo_root, component)
        en_file = os.path.join(comp_dir, "CHANGELOG.md")
        fr_file = os.path.join(comp_dir, "CHANGELOG.fr.md")

        if not os.path.isdir(comp_dir):
            print(f"Warning: component directory not found: {comp_dir}", file=sys.stderr)
            missing.append(component)
            continue

        unreleased_en, releases_en = parse_changelog(en_file)
        unreleased_fr, releases_fr = parse_changelog(fr_file)

        # Build a version → FR entries lookup for fast access
        fr_by_version: dict[str, list[str]] = {r["version"]: r["entries"] for r in releases_fr}

        merged_releases = []
        for rel in releases_en:
            merged_releases.append(
                {
                    "version": rel["version"],
                    "date": rel["date"],
                    "entries": {
                        "en": rel["entries"],
                        # Fall back to EN if no matching version in FR file
                        "fr": fr_by_version.get(rel["version"], rel["entries"]),
                    },
                }
            )

        result["components"][component] = {
            "unreleased": {
                "en": unreleased_en,
                # Fall back to EN if FR unreleased is empty
                "fr": unreleased_fr if unreleased_fr else unreleased_en,
            },
            "releases": merged_releases,
        }

    if missing:
        print(f"Warning: skipped missing components: {missing}", file=sys.stderr)

    output_path = os.path.join(repo_root, "global.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"global.json written to {output_path}")


if __name__ == "__main__":
    main()
