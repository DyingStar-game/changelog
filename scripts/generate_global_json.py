#!/usr/bin/env python3
"""
Parse all component CHANGELOG.md and CHANGELOG.fr.md files and emit
a single global.json at the repository root (schema version 2, ADR 0001).

Schema:
{
  "schema_version": 2,
  "generated_at": "<ISO-8601 UTC>",
  "types": { "added": { "en": "Added", "fr": "Ajouts" }, ... },   // display order
  "components": {
    "<component>": {
      "repo": "DyingStar-game/<repo>",
      "areas": { "<area>": { "en": "...", "fr": "..." }, ... },  // display order
      "unreleased": {
        "url": "<compare URL>" | null,
        "entries": { "en": [<entry>, ...], "fr": [<entry>, ...] }
      },
      "releases": [
        { "version": "1.2.3", "date": "YYYY-MM-DD", "yanked": false,
          "url": "<compare URL>" | null,
          "entries": { "en": [<entry>, ...], "fr": [<entry>, ...] } },
        ...
      ]
    },
    ...
  }
}

<entry> = { "type": "<type>" | null, "area": "<area>" | null, "text": "line\nline" }
type and area are null for entries written before they existed; "general" is
the area of an entry merged without one. The text is Markdown, one display
line per "\n" (the first is the bullet, the others its sub-lines).

Releases are ordered newest-first (as they appear in CHANGELOG files).
FR entries fall back to the EN ones when the FR section is empty or missing.
"""
import json
import os
import sys
from datetime import datetime, timezone

import changelog_lib as lib


def main() -> None:
    config = lib.load_config()
    result: dict = {
        "schema_version": 2,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "types": lib.TYPES,
        "components": {},
    }

    missing: list[str] = []
    for component, cfg in config.items():
        comp_dir = os.path.join(lib.REPO_ROOT, component)
        if not os.path.isdir(comp_dir):
            print(f"Warning: component directory not found: {comp_dir}", file=sys.stderr)
            missing.append(component)
            continue

        sections = {lang: lib.parse_changelog(cfg, os.path.join(comp_dir, lib.FILES[lang]))
                    for lang in lib.LANGS}
        fr_by_version = {s["version"]: s["entries"] for s in sections["fr"]}
        en_sections = sections["en"]
        versions = [s["version"] for s in en_sections if s["version"] is not None]

        unreleased = {"url": None, "entries": {"en": [], "fr": []}}
        releases = []
        for s in en_sections:
            entries = {"en": s["entries"], "fr": fr_by_version.get(s["version"]) or s["entries"]}
            if s["version"] is None:
                if versions and cfg.get("tag_format"):
                    unreleased["url"] = (f"https://github.com/{cfg['repo']}/compare/"
                                         f"{lib.tag_for(cfg, versions[0])}...HEAD")
                unreleased["entries"] = entries
                continue
            releases.append({
                "version": s["version"],
                "date": s["date"],
                "yanked": s["yanked"],
                "url": lib.release_url(cfg, versions, versions.index(s["version"])),
                "entries": entries,
            })

        result["components"][component] = {
            "repo": cfg["repo"],
            "areas": {**cfg["areas"], lib.FALLBACK_AREA: lib.FALLBACK_AREA_LABELS},
            "unreleased": unreleased,
            "releases": releases,
        }

    if missing:
        print(f"Warning: skipped missing components: {missing}", file=sys.stderr)

    output_path = os.path.join(lib.REPO_ROOT, "global.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"global.json written to {output_path}")


if __name__ == "__main__":
    main()
