# Plugging a repository into the changelog

What each DyingStar repository needs so its PRs feed the changelog under
[ADR 0001](../docs/adr/0001-changelog-format.md).

## Once, in `DyingStar-game/.github`

1. Copy [`PULL_REQUEST_TEMPLATE.md`](./PULL_REQUEST_TEMPLATE.md) to
   `.github/PULL_REQUEST_TEMPLATE.md`. GitHub uses it for every repository without its own
   template.
2. In `.github/workflows/update-changelog.yml`, send the entries as raw strings: with `--field`,
   a value starting with `@` is read as a file name and `42` / `true` become numbers / booleans.

   ```diff
   -            --field "client_payload[entry_en]=$ENTRY_EN" \
   -            --field "client_payload[entry_fr]=$ENTRY_FR" \
   +            --raw-field "client_payload[entry_en]=$ENTRY_EN" \
   +            --raw-field "client_payload[entry_fr]=$ENTRY_FR" \
   ```

## In each component repository

1. Delete `.github/PULL_REQUEST_TEMPLATE.md` (the organisation's template takes over).
2. Replace `.github/workflows/update-changelog.yml` with
   [`update-changelog.yml`](./update-changelog.yml), `COMPONENT` set to the component key of
   [`components.json`](../components.json) (twice). It adds the PR check. For
   `DyingStar-game/services`, whose component comes from the PR's `service:*` label, use
   [`update-changelog.services.yml`](./update-changelog.services.yml) instead.
3. Enable the Claude Code skill in `.claude/settings.json` (merge with what is there):

   ```json
   {
     "extraKnownMarketplaces": {
       "dyingstar": {
         "source": { "source": "github", "repo": "DyingStar-game/changelog" }
       }
     },
     "enabledPlugins": {
       "changelog@dyingstar": true
     }
   }
   ```

4. Add to `CLAUDE.md`, where PRs are described:

   ```markdown
   - The `CHANGELOG_EN` / `CHANGELOG_FR` blocks of a PR description follow the skill
     `changelog-entry` (types, areas, wording); the PR check "Check Changelog Entry" enforces it.
   ```

## A new component

Add it to [`components.json`](../components.json) (repository, areas, tag convention if it
tags releases) and create its `CHANGELOG.md` / `CHANGELOG.fr.md` from an existing one.
