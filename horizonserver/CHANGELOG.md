# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-dev.202610231756] - 2026-10-23

### Fixed

- **Connection**: Objects no longer go missing when you enter a busy area, such as a cargo depot full of crates.

## [0.1.0-dev.202610220604] - 2026-10-22

### Added

- **Connection**: A player can ask for their own movement to be timestamped by the servers, to find out where a stutter comes from.

### Changed

- **Performance**: Your own position reaches you twice as often, so turns, stops and bumps into walls are corrected sooner.

## [0.1.0-dev.202610211613] - 2026-10-21

### Added

- **Connection**: At server startup, arriving players wait in the queue until the first villages are ready instead of all landing in the same one.
- **Persistence**: The doors, drawers and lamps of a home stay as their occupant left them.

### Changed

- **Connection**: A village holds 50 players: newcomers wait in the queue rather than crowding a full village while a place can still be made.
- **Server meshing**: Servers are split earlier and around the villages, so a village and its players stay on one server.

### Fixed

- **Connection**: Players given an apartment near a server border no longer stay stuck without ever appearing in the world.
- **Connection**: Players no longer wait forever on a server that had restarted while the game kept sending it players.
- **Performance**: Servers no longer slow down when many villages are created at once.

## [0.1.0-dev.202610202031] - 2026-10-20

### Changed

- **Connection**: When every server is full, waiting players are told "All servers are full" instead of waiting with no end.

### Fixed

- **Connection**: New players are spread over the villages that still have room instead of crowding one village far past its size.

## [0.1.0-dev.202610201807] - 2026-10-20

### Changed

- **Server meshing**: A crowded server is now divided among several servers at once instead of being halved again and again.
- **Server meshing**: A server slowed down by a busy area is now split even when it has few players, so the game stays smooth there.

### Fixed

- **Connection**: Players waiting to join no longer end up on a full server after two minutes: they wait until it has room.

## [0.1.0-dev.202610201512] - 2026-10-20

### Added

- **Connection**: When the servers are full, players wait in a queue and see their place in it instead of overloading a server.
- **Persistence**: Your position is saved when you leave and regularly while you play.

### Changed

- **Connection**: Coming back to the game, you always wake up in your apartment.
- **Performance**: Players arriving in a crowd are let in a few at a time, so the server stays smooth.
- **Performance**: The server writes far fewer logs when many players are online, so problems met during big tests are easier to track down.

## [0.1.0-dev.202610192044] - 2026-10-19

### Fixed

- **Server meshing**: New players are spread evenly across the servers instead of all going to the busiest one.
- **Server meshing**: New players no longer appear at the world's origin when every village holds 50 players: villages take more while their buildings have free apartments.
- **Server meshing**: A game server that lost its connection to Horizon no longer refuses new players for good.
- **Server meshing**: When a crowd leaves and servers merge, the players who stay no longer move in jerks or fall through the ground.
- **Performance**: The server no longer slows down when hundreds of players arrive at once and wait for their apartment.
- **Performance**: The server gives unused memory back instead of growing after each rush of players.
- **Connection**: A player who lost the network can join again at once, instead of failing to load for up to an hour.

## [0.1.0-dev.202610161302] - 2026-10-16

- Added an elevator from the village road (M0001) to the factory, on the left before the first bridge. Several added in village M0059.
  Fixed exit from dwelling to open area.
- spawn shelves in cargo depot

## [0.1.0-dev.202610112359] - 2026-10-11

- Twelve factory cities appear on Tarsis 3.
- The orbital station has its teleporter cabin again.
- fix(mesh): server zones that go offline are reassigned to an available server
  Previously, zones from a lost server would remain unhosted if other servers were still running, leaving their players stranded. Now, they are preserved and handed over to the next available server. If no servers remain active, the system reverts to the initial partitioning, just as before.
  fix(mesh): ongoing player actions are replayed on the new server
  Horizon stores the last value for each active input—driving, sprinting, zero-G thrusting/stabilizing, and walking speed—and replays them immediately after the player arrives or wakes up on the new server; this prevents the truck from coming to an abrupt halt and ensures the sprint continues.
- The truck's engine revs follow its wheels: no more screaming engine in a fall or a jump.
  Releasing a movement key is no longer occasionally ignored by the server.

## [0.1.0-dev.202610042359] - 2026-10-04

- new system when create new server (server meshing dynamic) and send items and players on the new server
- Ordered freeze: after a split, the old server first freezes players, then occupied vehicles, and finally the remaining ~20,000 objects. The transferred player is no longer simulated by two servers simultaneously for 3 seconds, eliminating the truck "rubber-banding" and the freeze.
  Reduced snapshot: after the warm-up phase, Horizon requests only the players and their vehicles from `genericprops`, rather than everything (~2.5s). They arrive on the new server at their current position instead of being 2–3 seconds behind.
  Measurement: each split logs a `[mesh] freeze coverage` line, counting the handed-over objects that are missing from the server's list. This will determine whether it is possible to freeze only the objects currently being simulated.
- [server meshing dynamic]  change to the way the initial server is split: splitting across two new pre-warmed servers instead of moving everything to a single new server.
- At startup, there are no longer any buildings, only villages; M0001 is requested by default. New players wait up to 40 seconds for their housing units to load; otherwise, they receive a "Server not ready" error and are disconnected. Definitions for new props (simple_building, vehicle elevators) have also been added.
  New players are assigned to the least loaded Godot server, rather than being placed sequentially from village to village.
  The Godot server pool no longer collapses when specific servers freeze under load. A [mesh] state is now logged every 5 seconds, and scripts have been added to analyze load test results.
- only one server per player, so no more duplicates or a total of 6,372.
- change in how available housing slots work to manage the sudden influx of players
- Village seeds: The 4 "mining village" POIs from the tarsis_3 QGIS export are added to `startup_items.json` with fixed UUIDs and positions calculated from their lat/lon coordinates. `mining_village_01` is already marked as spawned, with its habs consisting of the 23 existing spawn buildings.
  Building-to-village link: The new `poi_uuid` property links each spawn building to its village (while `parent_id` remains for informational purposes). The village also receives a `spawn_requested` property.
  Apartment assignment: A new player is assigned to the fullest village that is still below the capacity limit (50, configurable via `max_players_per_village`). This limit is strict for individual players. Exceeding the limit is planned for future matchmaking (friends/groups) via `AssignRequest`, but this feature is not yet active.
  On-demand spawning: At 80% capacity (`village_prespawn_ratio`), if no other village has space, Horizon sets `spawn_requested` for the nearest unspawned village—one at a time. Only the Godot server responsible for that zone receives the request and creates the habs.
- serverinfo relays scenes_number_actives to clients.

## [0.1.0-dev.202609272359] - 2026-09-27

- optimization of parent-children by addeing index
  fix disconnect player (on some cases events continues to send to nobody
- Vehicle components (engines, and later batteries and tanks) replicate and persist: which bay holds which part now travels to every client.

## [0.1.0-dev.202609202359] - 2026-09-20

- Update number player split server from 30 to 75
  Fix move & reparent missed in some cases because of LOD
  Send velocity when transfer player to another player
- disable audio for NPC
  Resolve godot server pool list from DNS when run instead of when pod start
  add LOD for player movement
  report LOD delivery for debug
- Manage frequency in zones + manage different frequency depends on distance on a same zone
- Update server meshing dynamic with new world system in godot server
- Moving plugin.toml (plugins config) into the horizon-data docker image

## [0.1.0-dev.202609132359] - 2026-09-13

- Fix gorc when player in vehicule
- Update startup position / rotation
  increase server meshing dynamic (50 players)
- Vehicles can now show their suspension moving to other players.

## [0.1.0-dev.202609062359] - 2026-09-06

- Remove static rocks at startup and update rocks properties
- The system's star is no longer dropped when a world loads.
- Fix/player network

## [0.1.0-dev.202608302359] - 2026-08-30

- Fix player connection
- The Horizon patch has been replaced by a DyingStar-game/Horizon submodule.

## [0.1.0-dev.202608232359] - 2026-08-23

- Fixed a crash that could take the server down whenever a player connected, leaving clients on a grey screen with `ERROR 1337`.
- Update items to spawn, because now it's directly on the planet

## [0.1.0-dev.202608092359] - 2026-08-09

- Replicate the player stance (crouch/prone) and seated look yaw, plus per-seat vehicle occupancy, so other players see them.

## [0.1.0-dev.202607192359] - 2026-07-19

- fix player disconnect
  fix bridge when have many events (persistences)

## [0.1.0-dev.202607122359] - 2026-07-12

- The state of a vehicle's engine and horns is now replicated: every player around a truck hears it start, idle, rev and honk.

## [0.1.0-dev.202606212359] - 2026-06-21

- feat: replicate `mineral_id` on miningrock
  tweak: miningrock GORC distance 30 → 150 m
- Replicate the player's server-driven carry prompt to clients.

## [0.1.0-dev.202606142359] - 2026-06-14

- Fix reparent object. The position calculation wasn't right and so the item is so far, it' not updated on client (because gorc works nicely :D)
- Fix the apartment attribution store in persistence (it wasn't the case, that's why when restart Horizon, we loose them)
- When player disconnect, the remove_player will unscribe to all subscription, but not delete player from gorc internal database. Now, we delete it. Fix disconnected player seen for new players connected.
- Add the vehicle prop replication definition (state channel + deletion channel).
  Add the vehicle prop replication definition (state, deletion channel, and speed).
- Fix the ore shown on a fractured rock's cut faces so it stays consistent across clients.
