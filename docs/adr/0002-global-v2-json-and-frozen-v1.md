# 0002. Version 2 in `global.v2.json`, `global.json` frozen at version 1 until removed

- **Status:** Accepted
- **Date:** 2026-10-14
- **Deciders:** maintainer
- **Scope:** `generate_global_json.py`, `global.json`, `global.v2.json`, their readers
- **Amends:** [ADR 0001](./0001-changelog-format.md), section "`global.json` (schema version 2)"

## Context

ADR 0001 moved `global.json` to schema version 2, expecting the launcher and the website to move
with it. Launcher 1.0.0, the version players have, reads `global.json` without checking it: with
version 2 its window turns black at startup, hiding the notice that a newer launcher is out (the
launcher has no automatic update). A released launcher cannot be fixed from here: the file it
reads has to stay readable until players have moved to a newer launcher.

## Options considered

1. **Go back to version 1 until every reader has moved.** New readers wait, and the switch
   breaks again whatever still reads `global.json`.
2. **Generate both versions.** Launcher 1.0.0 keeps receiving new entries, but version 1 stays
   maintained in the scripts for a reader meant to disappear.
3. **Version 2 in `global.v2.json`, `global.json` frozen at version 1.** The scripts know only
   version 2; launcher 1.0.0 starts and shows the changelog as it was, until it is replaced.

## Decision

We take option 3.

- `generate_global_json.py` writes only `global.v2.json` (schema version 2, ADR 0001); the tests
  check it against the CHANGELOG files.
- `global.json` is a snapshot at schema version 1 (`generated_at`, then per component
  `unreleased: {en, fr}` and `releases: [{version, date, entries: {en, fr}}]`), committed once and
  never regenerated.
- New readers (the launcher after 1.0.0, the website) read `global.v2.json`.
- `global.json` is deleted once players have moved to a launcher reading `global.v2.json`.

## Consequences

- Launcher 1.0.0 starts again and shows a changelog that no longer changes, its update notice
  pointing players to the newer launcher.
- Deleting `global.json` early brings the black window back on launcher 1.0.0.
