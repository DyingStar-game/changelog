---
name: changelog-entry
description: How to write the CHANGELOG_EN / CHANGELOG_FR blocks of a DyingStar pull request description (types, areas, wording) and check them. Use whenever you create a PR or update a PR description in a DyingStar-game repository, or are asked about its changelog entry.
---

# Changelog entry of a DyingStar PR

The `CHANGELOG_EN` / `CHANGELOG_FR` blocks of the PR description become the player-facing
changelog (launcher, website) when the PR is merged. A check on the PR fails until they follow
these rules. Why they are so: ADR 0001 of `DyingStar-game/changelog`
(`docs/adr/0001-changelog-format.md`).

## Format

```markdown
<!-- CHANGELOG_EN -->
### Added
- [vehicles] New truck dashboard: speed, warning lights, batteries.
- [ui] Play hints no longer cover the chat.
### Fixed
- [planettech] The ground texture no longer stretches on steep slopes.
<!-- /CHANGELOG_EN -->

<!-- CHANGELOG_FR -->
### Added
- [vehicles] Nouveau tableau de bord du camion : vitesse, voyants, batteries.
- [ui] Les bulles d'aide ne couvrent plus le chat.
### Fixed
- [planettech] La texture du sol ne s'étire plus sur les pentes raides.
<!-- /CHANGELOG_FR -->
```

- **Type, required:** each entry sits under one of `### Added`, `### Changed`, `### Deprecated`,
  `### Removed`, `### Fixed`, `### Security`, written in English in both blocks. A PR mixing
  features and fixes uses several headings.
- **Area, required:** each entry starts with `[key]`, a key from the component's list (below).
  Same keys in the FR block, never translated.
- **One entry per `-` item.** A nested item or an indented paragraph becomes a sub-line of its
  entry; keep sub-lines for details of that entry only.
- **FR:** recommended. Same entries, same order, same type and area as EN. Left empty, the EN
  text is used for French players.
- **Nothing player-visible** (refactor, CI, tests, docs): delete both blocks.

## Wording

The readers are players, not developers.

- Say what changes for the player, effect first: "The truck reaches the same top speed whatever
  the number of motors", not "Refactor motor torque computation".
- No file, class, function or setting names (`global.json`, `client.ini`, `rollForward`), no
  commit prefixes (`fix(mesh):`, `feat:`), no dates, no PR or issue numbers.
- One change per entry; a short sentence, ending with a full stop.
- The type already says "added" or "fixed": no need to start with "Added" / "Fix".
- French: natural French, French typography (space before `:` `;` `?` `!`, « guillemets »).

## Areas

The list is in `components.json` of `DyingStar-game/changelog`; the component key is the one in
this repository's `.github/workflows/update-changelog.yml` (`component:`). To see the list and
check a description before pushing it:

```bash
d=$(mktemp -d) && gh repo clone DyingStar-game/changelog "$d" -- --depth 1 --quiet
python3 "$d/scripts/check_entry.py" --component <component> --list-areas
python3 "$d/scripts/check_entry.py" --component <component> --body-file <pr-body.md>
```

The check prints each error (with the closest area or type when one is misspelt) or, when the
block is valid, the entries as they will appear in `CHANGELOG.md`. On GitHub, the same check runs
on the PR ("Check Changelog Entry"): after updating the description, look at its result with
`gh pr checks`.

No area fits? Do not pick a wrong one: say so to the user, a new area is added by a PR on
`components.json` in `DyingStar-game/changelog`.
