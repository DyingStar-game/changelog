# 0001. Changelog format: types, areas and the PR changelog block

- **Status:** Accepted
- **Date:** 2026-10-14
- **Deciders:** maintainers
- **Scope:** Every component repository (DyingStar, horizonserver, services, launcher), this
  repository's scripts and `global.json`, its readers (launcher, website)

## Context

Each component repository sends the changelog of a merged PR here: its workflow extracts the
`CHANGELOG_EN` / `CHANGELOG_FR` blocks of the PR description and dispatches them;
`append_entry.py` writes them into the component's `CHANGELOG.md` / `CHANGELOG.fr.md`;
`generate_global_json.py` builds `global.json`, read by the launcher and the website.

The files claim to follow [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), but:

- changes were not grouped by type (Added, Fixed…), and a PR often mixes features and fixes;
- versions were not linkable;
- a `[YANKED]` version lost its entries in `global.json`, a SemVer pre-release could not be cut;
- each PR became one bullet whatever its Markdown (fixed on 2026-10-13: one bullet per list item);
- authors marked the area of a change by hand, each in their own way (`Vehicles:`, `Truck:`,
  `fix(vehicle):`, `[Rock]`, `Star map:` / `Star chart:`), so nothing can be filtered or grouped;
- nothing checked the block before the merge: a mistake was only seen in the published changelog.

Most PR descriptions are written by Claude Code, which only knows what the repository it works in
tells it.

## Decision

### The PR changelog block

Each entry has a **type** (Keep a Changelog) and an **area** (where in the component), both
required. A PR may hold several types and areas:

```markdown
<!-- CHANGELOG_EN -->
### Added
- [vehicles] New truck dashboard: speed, warning lights, batteries.
### Fixed
- [planettech] The ground texture no longer stretches on steep slopes.
<!-- /CHANGELOG_EN -->

<!-- CHANGELOG_FR -->
### Added
- [vehicles] Nouveau tableau de bord du camion : vitesse, voyants, batteries.
### Fixed
- [planettech] La texture du sol ne s'étire plus sur les pentes raides.
<!-- /CHANGELOG_FR -->
```

- **Types:** `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`,
  `### Security`, in English in both blocks (as Keep a Changelog's French text keeps them).
- **Areas:** `[key]` at the start of each entry, from the component's closed list in
  [`components.json`](../../components.json). The FR block uses the same keys; the readers show
  the label of the reader's language. A new area is added by a PR on `components.json`.
- **Entries:** one per Markdown list item (`-`, `*`, `+`, `1.`). Nested items and indented
  paragraphs become sub-lines of their entry; wrapped lines are joined as Markdown renders them.
- **FR:** optional. When present, the same entries in the same order, with the same type and area.
- **No player-visible change:** delete both blocks; the PR needs no entry.
- **Writing:** for players, not a commit log. No file names, no `fix(scope):` prefixes, no dates.
  One change per entry, its effect first.

### Enforcement

- **PR check:** each component repository calls the reusable workflow
  [`check-entry.yml`](../../.github/workflows/check-entry.yml) on its pull requests (opened,
  edited, synchronized). It runs [`check_entry.py`](../../scripts/check_entry.py), which fails on
  a missing type or area, an unknown one (suggesting the closest), or FR entries that do not
  match EN. The job summary previews the entries as they will be written.
- **At merge:** a block merged with errors is still recorded, never lost: no type → `Changed`,
  no area → `general`; the errors are printed as warnings.
- **Claude Code:** the `changelog-entry` skill of the `changelog` plugin (marketplace
  `dyingstar`, in this repository) holds these rules for writing a PR description. Each
  component repository enables it in `.claude/settings.json` and points to it from `CLAUDE.md`.
- **PR template:** one organisation-wide template in `DyingStar-game/.github`, linking here.

### CHANGELOG files

```markdown
## [Unreleased]

### Added

- **Vehicles**: New truck dashboard: speed, warning lights, batteries.

### Fixed

- **PlanetTech**: The ground texture no longer stretches on steep slopes.

### Uncategorized

- An entry written before types existed.
```

- One `### Type` group per type, in Keep a Changelog's order; the area label in bold at the start
  of the entry (` : ` in French). The newest entries come first in their group.
- Entries written before this ADR have no type and no area. In a section that also has typed
  entries they are kept under `### Uncategorized`, last; released sections are left as they are.
- `## [x.y.z] - YYYY-MM-DD`, with ` [YANKED]` for a withdrawn version. Versions follow SemVer,
  pre-releases included (`0.0.1-test5`, `1.1.0-beta.1`).
- **Links:** for a component with a tag convention (`tag_format`, `tag_overrides` in
  `components.json`), `cut_release.py` rewrites the link references at the end of the file:
  `[unreleased]` compares the last tag with `HEAD`, each version with the previous one. Only the
  launcher has release tags (`vX.Y.Z`); DyingStar and horizonserver are still in development
  (their changelog is `[Unreleased]` only) and get links once they tag releases.

### `global.json` (schema version 2)

The schema is documented at the top of
[`generate_global_json.py`](../../scripts/generate_global_json.py). Changes from version 1:

- each entry is `{"type", "area", "text"}` instead of a string; `type` and `area` are `null`
  for entries written before this ADR;
- `types` (display order, EN / FR labels) at the root, `areas` and `repo` per component;
- `unreleased` and each release carry a `url` (compare link, or `null`) and their entries
  under `entries`; releases carry `yanked`;
- `text` is Markdown, its lines separated by `\n` without indentation (first line: the bullet,
  next ones: its sub-lines).

The launcher and the website move to version 2 together with this change.

## Consequences

- A PR description with a malformed changelog block fails its check until fixed.
- Adding an area or a component is a PR on this repository's `components.json`.
- The old entries of `[Unreleased]` (DyingStar mainly) stay uncategorized until someone sorts
  them by hand.
- The rules live in three places, which must change together: this ADR (why), `check_entry.py`
  and `changelog_lib.py` (what is enforced), the `changelog-entry` skill (how to write).
