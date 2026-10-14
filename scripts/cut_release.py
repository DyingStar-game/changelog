#!/usr/bin/env python3
"""
Move the [Unreleased] section to a versioned block in a component's
CHANGELOG.md and CHANGELOG.fr.md, then insert a fresh empty [Unreleased]
header at the top and rewrite the version links (ADR 0001).

Usage:
    python3 scripts/cut_release.py \
        --component "launcher" \
        --version "0.3.0" \
        --date "2026-06-06"
"""
import argparse
import os
import re
import sys

import changelog_lib as lib

# Semantic Versioning 2.0.0, pre-release and build metadata included
VERSION_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def cut_release(path: str, version: str, date: str, lang: str) -> None:
    if not os.path.isfile(path):
        print(f"Warning: {path} not found, skipping.", file=sys.stderr)
        return
    lines = lib.read_lines(path)
    header_idx = lib.find_unreleased(lines)
    if header_idx is None:
        print(f"Warning: no unreleased header found in {path}, skipping.", file=sys.stderr)
        return
    if any(l.startswith(f"## [{version}] ") for l in lines):
        print(f"Error: version {version} already in {path}.", file=sys.stderr)
        sys.exit(1)

    # The unreleased header becomes the version's; a fresh one goes above it
    lines[header_idx] = f"## [{version}] - {date}\n"
    lines[header_idx:header_idx] = [f"## [{lib.UNRELEASED_LABELS[lang]}]\n", "\n"]
    lib.write_lines(path, lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Cut a release from the [Unreleased] section.")
    parser.add_argument("--component", required=True)
    parser.add_argument("--version", required=True, help="Semantic version, e.g. 1.2.3 or 1.2.3-beta.1")
    parser.add_argument("--date", required=True, help="Release date YYYY-MM-DD")
    args = parser.parse_args()

    config = lib.load_config()
    if args.component not in config:
        print(f"Error: unknown component '{args.component}'.\nValid: {list(config)}", file=sys.stderr)
        sys.exit(1)
    if not VERSION_RE.match(args.version):
        print(f"Error: version must follow Semantic Versioning, got '{args.version}'", file=sys.stderr)
        sys.exit(1)
    if not DATE_RE.match(args.date):
        print(f"Error: date must be YYYY-MM-DD, got '{args.date}'", file=sys.stderr)
        sys.exit(1)

    cfg = config[args.component]
    comp_dir = os.path.join(lib.REPO_ROOT, args.component)
    for lang in lib.LANGS:
        path = os.path.join(comp_dir, lib.FILES[lang])
        cut_release(path, args.version, args.date, lang)
        lib.update_links(cfg, path, lang)


if __name__ == "__main__":
    main()
