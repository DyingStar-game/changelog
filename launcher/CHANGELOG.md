# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-06-10

- Remote changelog: fetch from centralized JSON, dedicated page with environment filtering (Testing / Universe) and read/unread badges.
  UI sounds: background music, hover/click SFX, volume/mute control in the navbar.
  In-app OAuth: Discord/Keycloak login in a launcher window (no system browser), with handoff to the Discord app via discord://.
  FilesPanel: “Select an install directory” message when no folder is set.
  Linux (AppImage): GPU / accelerated video decode disabled at startup (no need for --disable-accelerated-video-decode).
  Legacy local changelog in FilesPanel (CHANGELOG.md, related modal).
## [0.2.2] - 2026-05-27

- fix player count on game panel
- fix expiration authentication
- fix game version update

## [0.2.1] - 2026-05-17

- size of launcher, in some case expands on its own at startup
- link to download the new version of the launcher

## [0.2.0] - 2026-05-16

- Bilingual contributor docs under `docs/en/` and `docs/fr/` (onboarding, contributing, security, code of conduct)
- Structured install progress labels with full UI i18n (`installProgress.*`)
- Browser language detection and persisted UI language (`ds-language`)
- github actions for build the launcher
- Package manager standardized on **pnpm** (removed `package-lock.json`)
- Native install folder dialog localized (fr/en) via main-process l10n
- Social `addFriend` mock validates duplicate names and throws typed errors
- Unused `game:get-state` IPC stub removed

## [0.1.0] - 2025-01-01

- Initial open-source Electron launcher: auth, game install/update, server status, lore, social UI (mock)
