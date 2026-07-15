# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- fix player disconnect
  fix bridge when have many events (persistences)
- The state of a vehicle's engine and horns is now replicated: every player around a truck hears it start, idle, rev and honk.
- feat: replicate `mineral_id` on miningrock
  tweak: miningrock GORC distance 30 → 150 m
- Replicate the player's server-driven carry prompt to clients.
- Fix reparent object. The position calculation wasn't right and so the item is so far, it' not updated on client (because gorc works nicely :D)
- Fix the apartment attribution store in persistence (it wasn't the case, that's why when restart Horizon, we loose them)
- When player disconnect, the remove_player will unscribe to all subscription, but not delete player from gorc internal database. Now, we delete it. Fix disconnected player seen for new players connected.
- Add the vehicle prop replication definition (state channel + deletion channel).
  Add the vehicle prop replication definition (state, deletion channel, and speed).
- Fix the ore shown on a fractured rock's cut faces so it stays consistent across clients.
