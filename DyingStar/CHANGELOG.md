# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- New truck parking hand brake: long-press Space under 3 km/h, released by throttle,
  stays engaged when you leave the truck. Shown on the dashboard, HUD and shortcut hint.
  Seated players now add their weight (75 kg) to the truck's load and total weight;
  OVERLOADED accounts for passengers + bed cargo.
  Smoother ride: no more camera jitter once seated, and the truck moves smoothly for
  everyone (driver included).
  "Driver seat taken" message when the driver seat is occupied; the enter-seat prompt
  no longer shows while already seated. You now exit beside the seat you used.
  Fixed: cargo no longer disappears when dropped into the bed in multiplayer.
  The vehicle UI is now in English.
- Mining rocks can hold different minerals (gold added); the ore look is data-driven per mineral.
- Collision calculation reduction by 50 times (tested on 200 boxes and rocks)
- Add a drivable networked truck (driver and passenger seats, powertrain, in-cab dashboard, free look); the admin cleanup tool can now remove vehicles and depot crates.
  Smooth networked vehicles and players (client interpolation), and let the admin cleanup tool remove vehicles and depot crates.
- Fix carried props (boxes, ore) despawning for other players over distance.
- Fix the admin cleanup tool leaving ghost collisions after deleting a prop.
- Add admin cleanup tool: ray from the player's hand, red/yellow aim line, click to delete the targeted prop (rock / box / depot only).
  Server-authoritative delete: frees the node (or forwards to Horizon) -> removed from GORC + database. World infrastructure is protected.
  Tools 1 (perforator) and 2 (cleanup) are now mutually exclusive.
  Mining depot placeholder spawns its networked copy on the game server (collision + collect/SEND logic), with a deterministic uuid (optional stable_id) to avoid duplicate accumulation; placed in Sandbox Capital.
- Unify how player and prop properties replicate to nearby players, and fix mining rocks sometimes appearing at the world origin.
- Press F6 to record the game screen (for bug reports or clips); recordings are saved as AVI files in your Documents/DyingStar/records folder.
- Add a mining depot: deposit mined ore, refine it by volume (ore purity, stock and per-crate fill shown on the depot screen) and extract a carryable crate of ore.
- Mining rocks now show their ore: a few small traces on the surface, while the real amount is revealed by breaking the rock — richer pieces contain more ore.
- Press **E** to **pick up / drop** a mined ore (one at a time).
  Only a **fully mined** ore (no fault left) can be carried; you can't take one already carried by someone else.
  Carrying **slows you down**, the ore **floats in front of you** (no collision), and **everything is visible to other players**.
  The **perforator** is always present: **stowed** by default / while carrying, **out** when equipped.
- Mining V0: equip a perforator, aim at a rock's predefined faults and drill to break it into pieces, visible and synchronized in multiplayer
  Also removes the F4 third-person camera, which conflicts with the aim-based mining
  See https://github.com/DyingStar-game/DyingStar/pull/186
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
- Rewrite code for player out of server zone
  Planet tech v1
  Update to Godot 4.6.1
  Update docker for build server
  New tree architecture
  Add planet data download for build and get locally for developers

## [0.0.1-test5] - 2025-12-16

- Version for the test5
