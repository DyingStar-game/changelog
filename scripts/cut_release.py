#!/usr/bin/env python3
"""
Move the [Unreleased] section to a versioned block in a component's
CHANGELOG.md and CHANGELOG.fr.md, then insert a fresh empty [Unreleased]
header at the top.

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

COMPONENTS = [
    "DyingStar",
    "horizonserver",
    "services/monitoring",
    "services/persistence",
    "services/resourcesDynamic",
    "launcher",
]

UNRELEASED_HEADERS = {"## [Unreleased]", "## [Non publié]"}
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def cut_release(filepath: str, version: str, date: str, new_unreleased_header: str) -> None:
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
        print(f"Warning: no unreleased header found in {filepath}, skipping.", file=sys.stderr)
        return

    versioned_header = f"## [{version}] - {date}\n"

    # Replace the unreleased header with the versioned one
    lines[header_idx] = versioned_header

    # Insert a fresh unreleased block above: header + blank line separator
    lines[header_idx:header_idx] = [f"{new_unreleased_header}\n", "\n"]

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Cut a release from the [Unreleased] section.")
    parser.add_argument("--component", required=True)
    parser.add_argument("--version", required=True, help="Semantic version, e.g. 1.2.3")
    parser.add_argument("--date", required=True, help="Release date YYYY-MM-DD")
    args = parser.parse_args()

    if args.component not in COMPONENTS:
        print(f"Error: unknown component '{args.component}'.\nValid: {COMPONENTS}", file=sys.stderr)
        sys.exit(1)
    if not VERSION_RE.match(args.version):
        print(f"Error: version must be semver X.Y.Z, got '{args.version}'", file=sys.stderr)
        sys.exit(1)
    if not DATE_RE.match(args.date):
        print(f"Error: date must be YYYY-MM-DD, got '{args.date}'", file=sys.stderr)
        sys.exit(1)

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    comp_dir = os.path.join(repo_root, args.component)

    cut_release(os.path.join(comp_dir, "CHANGELOG.md"), args.version, args.date, "## [Unreleased]")
    cut_release(os.path.join(comp_dir, "CHANGELOG.fr.md"), args.version, args.date, "## [Non publié]")


if __name__ == "__main__":
    main()
