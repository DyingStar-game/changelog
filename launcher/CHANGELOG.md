# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Account**: Sign-in shown as unavailable while the sign-in server is down, instead of a sign-in button that fails.
- **Changelog**: "Mark all as read" button.
- **Download and install**: The launcher updates itself: the new version downloads in the background and installs on restart, or when the launcher closes.
- **Interface**: The launcher's version is shown beside the logo.
- **Download and install**: The game's output is kept in a log file beside the launcher's, to help understand a crash.

### Changed

- **Interface**: The Discord link opens the Discord app when it is installed, straight to the server for its members; otherwise the web page.
- **Social**: Friends' status refreshed every minute.
- **Interface**: Launcher minimized while the game runs, back when it closes.
- **Changelog**: Shorter build names, unread versions shown by a dot; the changelog opens on the newest version.
- **Interface**: Disabled buttons show a not-allowed cursor and, when the reason is not visible, say why in a tooltip.
- **Download and install**: Launchers installed from a .deb or .rpm package download the new package directly.

### Fixed

- **Download and install**: Full disk reported clearly, with the space to free, instead of an interrupted download; the download is kept to resume.
- **Interface**: Server no longer shown as unavailable after switching universes quickly.
- **Account**: Sign-in with Discord back in the browser, where Discord already knows the account, instead of a launcher window asking for it again.
- **Download and install**: The game no longer crashes when started from the AppImage launcher.
- **Interface**: Server status recovers by itself when the connection comes back, without restarting the launcher.

### Security

- **Download and install**: A game archive can no longer write files outside the game folder.
- **Interface**: Launcher components updated to close known security flaws.

## [1.0.1] - 2026-10-14

### Changed

- **Changelog**: On Universe Testing, changes are listed build by build, grouped by the version they lead to.
- **Changelog**: On Universe, the development builds of a version are folded under it, and the version shows all of their changes.
- **Download and install**: Play checks for a new game version before launching the game.
- **Changelog**: Changelog entries are grouped by type and show the area they concern (vehicles, interface…).
- **Changelog**: A withdrawn version is marked as such.

### Fixed

- **Download and install**: A game update released while the launcher is open is now offered without restarting it.
- **Download and install**: A download stuck on a slow connection now recovers by itself.
- **Download and install**: A download cut off by the connection now resumes by itself; when it cannot, a message says so.
- **Interface**: A part of the launcher that fails to display no longer leaves the whole window black.

## [1.0.0] - 2026-10-13

- Profile editing added: faction, biography and role-play sheet.
- Organisation management added: details, invitations, members, ranks and leadership; leaving an organisation; inviting a player from their profile.
- Social page split into Friends and Organisations, each with its list, a search and the pending requests.
- Header split into two bars: the launcher on top, the current universe below (Home, Social, Changelog and account).
- Sign-in moved to the top right corner; while signed out, the Play button is replaced by "Sign in with Discord".
- Counters added for pending friend requests and unread changelog versions.
- Test environment flagged on every page; the launcher now opens on it.
- Lore page removed.
- Crackling in the interface sounds fixed.
- Home page redesigned: the universe over a full-screen image slideshow, and a single bar at the bottom with the server status, the game's state and its main action (install, update, sign in, play).
- Game downloads can be paused, resumed (even after closing the launcher) and cancelled; the speed and time left are shown.
- Game files (version, install folder, cache) moved behind a ⚙ button next to the main action.
- A pending game update shows the installed and new versions, with a link to its changelog.
- Friends on the home page listed alphabetically, all of them.
- Notifications (profile saved, organisation created, cache cleared…) shown in a corner of the screen.
- Signing out no longer opens a browser page; the next sign-in asks for the account again.
- Friend list cleared when signing out.
- Screenshots and videos in the game folder kept when the game is updated.
## [0.4.0] - 2026-10-10

- Social: friends, friend requests and organisations now use the game's social service, with a player search
  Player and organisation pages, opened by clicking a player or an organisation; Back returns where you were
  Fixed the launcher window not appearing on Linux Wayland sessions (sound only)
  The header adapts to narrow windows: sections and the universe switch move into the menu
  Statuses (member, friend, request sent…) no longer look like buttons; every button shows the hand cursor
  New language menu in the header, and tooltips on the header buttons
  Menus and the volume slider can be used with the keyboard
  Pages and lists show a placeholder of their content while loading
## [0.3.2] - 2026-09-23

- Added **Fullscreen** and **Minimize** buttons.
  Added a **hamburger menu** when the launcher is in a smaller size. This will allow the launcher to be resized even further for those who prefer a more compact layout, although not everything has been moved into the menu yet.
  Added **game launch detection** to disable the **Launch** button as soon as it is clicked, preventing multiple launch attempts.
  Added **changelog read detection**, which should fix the issue where notification badges would reappear after every release.
## [0.3.1] - 2026-06-11

- Fix sounds playing when game is running.
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

[unreleased]: https://github.com/DyingStar-game/launcher/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/DyingStar-game/launcher/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/DyingStar-game/launcher/compare/v0.4.0...v1.0.0
[0.4.0]: https://github.com/DyingStar-game/launcher/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/DyingStar-game/launcher/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/DyingStar-game/launcher/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/DyingStar-game/launcher/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/DyingStar-game/launcher/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/DyingStar-game/launcher/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/DyingStar-game/launcher/compare/0.1.0...v0.2.0
[0.1.0]: https://github.com/DyingStar-game/launcher/releases/tag/0.1.0
