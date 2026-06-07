# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Mining V0: equip a perforator, aim at a rock's predefined faults and drill to break it
- into pieces, visible and synchronized in multiplayer. Also removes the F4 third-person
- camera, which conflicts with the aim-based mining.
- See details on https://github.com/DyingStar-game/DyingStar/pull/186
- Add button in pause UI to return to menu (disconnect from the server)
- Fix pseudo on player and parent when changing parent (server and client fix)
- Fix spawn in apartments
- Fix light of the universe
- Fix godot server (many errors)
- Manage apartments spawn
- Enhance server error messages
- Fix crash on built game (wrong dotnet version)
- Update to dotnet 9, remove login page (auth with JWT token)
- Fix log in /tmp (crash on Windows)
- Fix SSH deploy
- Fix build and deploy
- Add build game in GitHub Actions
- Remove Wwise, replaced by audio directly in Godot
- Review UI interface and settings: sound, livekit (vocal proximity)
- Fix delete player on disconnect
- Fix Wwise for dedicated server
- Install dotnet runtime in docker server
- Rewrite code for player out of server zone; Planet tech v1; update to Godot 4.6.1; new tree architecture; add planet data download

## [0.0.1-test5] - 2025-12-16

- Version for the test5
