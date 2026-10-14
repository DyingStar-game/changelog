# 0003. Dev releases, cut by the preprod builds

- **Status:** Accepted
- **Date:** 2026-10-14
- **Deciders:** maintainer
- **Scope:** `cut_release.py`, `generate_global_json.py`, `global.v2.json` and its readers, the
  preprod build workflows of DyingStar and horizonserver
- **Amends:** [ADR 0001](./0001-changelog-format.md), section "CHANGELOG files" (links)

## Context

DyingStar and horizonserver tag no release while in development: every merged PR went into
`[Unreleased]`, which held about 450 DyingStar entries ten months after `0.0.1-test5`. Players
and testers could not tell what changed since the build they last played.

These components are built for preprod several times a week; until now each merge into
`develop` started a build. Those builds are not releases, but each one is what testers play.

## Decision

### A dev release per preprod build

- The preprod builds are started by hand (a merge into `develop` no longer builds): DyingStar's
  `Release Preprod` workflow (server and client together), horizonserver's
  `Build & Deploy to Preprod`.
- Run from `develop` and deployed, such a build is a **dev release**: version
  `<next>-dev.<UTC yyyymmddhhmm>` (`0.1.0-dev.202610141530`), where `<next>` is the stable
  version in preparation (repository variable `NEXT_VERSION`, `0.1.0` when unset). The build
  tags its commit with the version, without the `v` prefix that starts the production builds,
  and sends the `release` dispatch: `cut_release.py` turns `[Unreleased]` into that version.
  The client's `version.json` keeps its 14-digit build id as `version` (the launcher orders
  preprod builds by it: an installed `20261014153012` would rank above `0.1.0-dev.…` and hide
  the update), the same minute plus `00`, and names the dev release in `devRelease`.
- A dev release with nothing in `[Unreleased]` is not cut: no empty section. A stable release is
  always cut, even empty.
- A build from another branch reaches preprod but is no dev release.
- SemVer orders them as wanted: `0.0.1-test5` < `0.1.0-dev.*` < `0.1.0`.

### Dev releases are kept

When `0.1.0` is cut, the `0.1.0-dev.*` sections stay below it in the files and in
`global.v2.json`; its own section only holds what was merged after the last dev release (it may
be empty, or a summary written by hand). Each release of `global.v2.json` carries `"dev": true`
for a dev release. **Readers** (launcher, website) show the dev releases folded under the version
they lead to (`0.1.0-dev.*` under `0.1.0`, "in progress" until it exists), not as a flat list.

### Catching up

`[Unreleased]` was split once into one dev release per week (`split_unreleased_weekly.py`),
`<next>-dev.<Sunday yyyymmdd>2359` dated on the Sunday: each entry is dated by the first commit
of this repository, or of the CHANGELOG the component repository kept before it, that holds its
text. The current week stayed in `[Unreleased]`. These versions have no tag.

### Concurrent writes

A merged PR and a dev release of another component may write here at the same time. The two
`handle-*` workflows start again from the new `main` when their push is refused (5 attempts)
rather than lose the change; a `concurrency` group would cancel a pending run instead.

## Consequences

- Testers see what changed build by build; `0.1.0` will gather many dev releases.
- `NEXT_VERSION` is raised in both component repositories at each stable release.
- No links for DyingStar and horizonserver yet: the weekly catch-up versions have no tag.
- An entry merged while a preprod build runs lands in that build's dev release although the
  build does not contain it.
