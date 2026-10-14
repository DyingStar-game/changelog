#!/usr/bin/env python3
"""
One-off (ADR 0003): split a component's [Unreleased] section into one dev
release per week, as if a dev release had been cut every Sunday.

Each entry is dated by the first commit of the given git histories whose
CHANGELOG file holds its text (its area label aside). The week of that date
gives its section, `<base>-dev.<yyyymmdd>2359 - <yyyy-mm-dd>` on the Sunday;
the entries keep their order inside a section. The entries of the current
week stay in [Unreleased], for the next dev release. A FR entry takes the week of
the EN entry at the same position when both files hold the same number of
entries, its own date otherwise.

Usage:
    python3 scripts/split_unreleased_weekly.py \
        --component DyingStar --base 0.1.0 \
        --history .:DyingStar/CHANGELOG.md \
        --history ../DyingStar:CHANGELOG.md

--history REPO:PATH may be repeated (the CHANGELOG lived in the component
repository before this one); the FR file is PATH with ".fr.md".
Prints the entries dated by no commit (they go in the newest week).
"""
import argparse
import datetime
import os
import re
import subprocess
import sys

import changelog_lib as lib

BOLD_PREFIX_RE = re.compile(r"\*\*[^*]+\*\* ?: ")
# Old entries carried their area by hand: "Vehicles: ", "[Rock] ", "fix(vehicle): "
HAND_PREFIX_RE = re.compile(r"^(?:\[[^\]]+\]\s*|[\w ()/-]{1,30}:\s+)")


def normalize(text: str) -> str:
    text = BOLD_PREFIX_RE.sub("", text).replace("**", "")
    return re.sub(r"\s+", " ", text).strip().lower()


def entry_key(entry: dict) -> str:
    """The part of an entry most likely to be found unchanged in old files."""
    first = normalize(entry["text"].split("\n")[0])
    first = HAND_PREFIX_RE.sub("", first)
    return first[:80]


def snapshots(repo: str, path: str) -> list[tuple[datetime.date, str]]:
    """(commit date, normalized file content) of every commit touching path, oldest first."""
    log = subprocess.run(["git", "-C", repo, "log", "--reverse", "--format=%H %cs", "--", path],
                         capture_output=True, text=True, check=True).stdout.split("\n")
    out = []
    for line in filter(None, log):
        sha, date = line.split()
        show = subprocess.run(["git", "-C", repo, "show", f"{sha}:{path}"], capture_output=True, text=True)
        if show.returncode == 0:
            out.append((datetime.date.fromisoformat(date), normalize(show.stdout)))
    return out


def date_entries(entries: list[dict], history: list[tuple[datetime.date, str]]) -> list[datetime.date | None]:
    dates: list[datetime.date | None] = []
    for e in entries:
        key = entry_key(e)
        dates.append(next((d for d, content in history if key in content), None))
    return dates


def week_end(date: datetime.date) -> datetime.date:
    return date + datetime.timedelta(days=6 - date.weekday())


def split(cfg: dict, path: str, lang: str, weeks: list[datetime.date | None], base: str) -> None:
    """weeks: the Sunday of each entry's week, None to leave it in [Unreleased]."""
    lines = lib.read_lines(path)
    start = lib.find_unreleased(lines)
    end = lib.section_end(lines, start)
    entries = lib.parse_section_lines(cfg, lines[start + 1:end])
    current = [e for e, w in zip(entries, weeks) if w is None]
    body = [f"## [{lib.UNRELEASED_LABELS[lang]}]\n"]
    body += lib.render_section_body(cfg, current, lang) if current else ["\n"]
    for sunday in sorted({w for w in weeks if w is not None}, reverse=True):
        group = [e for e, w in zip(entries, weeks) if w == sunday]
        body.append(f"## [{base}-dev.{sunday:%Y%m%d}2359] - {sunday.isoformat()}\n")
        body += lib.render_section_body(cfg, group, lang)
    lines[start:end] = body
    lib.write_lines(path, lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Split [Unreleased] into weekly dev releases.")
    parser.add_argument("--component", required=True)
    parser.add_argument("--base", required=True, help="Version the dev releases lead to, e.g. 0.1.0")
    parser.add_argument("--history", action="append", required=True, metavar="REPO:PATH")
    args = parser.parse_args()

    cfg = lib.load_config()[args.component]
    comp_dir = os.path.join(lib.REPO_ROOT, args.component)
    weeks: dict[str, list[datetime.date]] = {}
    sections: dict[str, list[dict]] = {}
    for lang in lib.LANGS:
        path = os.path.join(comp_dir, lib.FILES[lang])
        lines = lib.read_lines(path)
        start = lib.find_unreleased(lines)
        if start is None:
            sys.exit(f"Error: no unreleased header in {path}")
        sections[lang] = lib.parse_section_lines(cfg, lines[start + 1:lib.section_end(lines, start)])
        history = []
        for spec in args.history:
            repo, file = spec.split(":", 1)
            if lang == "fr":
                file = file.removesuffix(".md") + ".fr.md"
            history += snapshots(repo, file)
        history.sort(key=lambda s: s[0])
        dates = date_entries(sections[lang], history)
        newest = max((d for d in dates if d), default=datetime.date.today())
        for e, d in zip(sections[lang], dates):
            if d is None:
                print(f"{lang}: undated, put in the newest week: {e['text'].splitlines()[0][:90]}")
        this_week = week_end(datetime.date.today())
        weeks[lang] = [None if week_end(d or newest) >= this_week else week_end(d or newest) for d in dates]

    if len(sections["fr"]) == len(sections["en"]):
        weeks["fr"] = weeks["en"]
    for lang in lib.LANGS:
        split(cfg, os.path.join(comp_dir, lib.FILES[lang]), lang, weeks[lang], args.base)
        lib.update_links(cfg, os.path.join(comp_dir, lib.FILES[lang]), lang)
    for sunday in sorted({w for w in weeks["en"] if w is not None}):
        print(f"{args.base}-dev.{sunday:%Y%m%d}2359: {weeks['en'].count(sunday)} entries")
    print(f"Left in [Unreleased] (this week): {weeks['en'].count(None)} entries")


if __name__ == "__main__":
    main()
