# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Carried objects now feel much better: they don't snap to your hands on pickup — they ease in and trail as you move, react to bumps, and are solid immediately. Look down to set an object on the floor, or up to place it high.
  A carried object no longer shoves you around, and looking up inside a container no longer flings it onto the roof.
  The interaction reach is now a single configurable value on the player.
  New storage containers lock any crate that settles on their floor so it can't be knocked around — pick it back up to free it.
- The dev spawn wheel is now server-authoritative: objects land in front of you, on the ground and upright, and the server decides where. The mouse wheel rotates a carried object by 15° notches, and holding the middle mouse button free-rotates it on all axes with the mouse — both about the object's centre.
  The mining depot is no longer spawnable and packs its ore into a hauling box.
  Using a 3D screen no longer strands your camera in space.
  Vehicles steer and brake with the engine off, and the engine can be cut at any speed.
  In the settings menu, Esc now goes back instead of releasing the mouse.
  A crate that falls or is thrown into a truck bed is now weighed like a hand-loaded one.
  You can no longer grab an object or open a vehicle door through a building wall.
  Plus brighter truck headlights and a class of client crashes fixed.
- Players have sound: footsteps (random samples, cadence following your speed), the torch switch and the jump. They are positional and replicated, so you hear the players around you walk, jump and light their torch.
- Update planet tech. generate heightmap for each LOD, fix teleport to another planet / point.
  On network, planets are now generic objects.
- Vehicles have sound: doors, engine start/stop, an engine note that rises with the revs, a horn (H) and a special horn (Alt+H), hand brake and head lights. The engine must now be started with the ignition key (I) while standing still before the vehicle will drive.
- Updated the mini truck model (fixing the wheel spin axis and the cargo-bay weight zone).
  The pause menu no longer closes when you click in the void — use Esc or the Resume button.
  Changing the screen resolution now asks you to confirm within 10 seconds and reverts automatically otherwise, so a too-large resolution can't lock you out.
- Carried objects now physically collide with the world: you can bump and rest them against the ground, walls and vehicles, and stack them by looking up or down to raise/lower a held object. An object dragged out of reach (e.g. stuck behind a wall) is dropped automatically.
- You can now show/hide the on-screen debug panels from Settings → General, or with a rebindable key (default Alt+²) available in the Controls menu.
- Truck: the steering wheel now turns the right way at a sensible speed, and the reverse camera is no longer mirrored.
- The dev spawn wheel (T) is now a two-level menu (category → variant);
  the pallet crates it spawns can be picked up and carried.
  Test containers now have collision.
  Fixed truck doors that could refuse to open once a prop was spawned nearby, and carrying crates from a normal distance
  held items now float a bit further ahead.
- Update physics to 60 FPS.
  fix per-chunk collision bodies for Jolt at astronomic coordinates
  fix terrain data export + cache validation + idle physics sleep
- Update export options for planets
- fix planet folder && build
  add Bardok house for test
  add Kankan containers for test
- Update planet tech, add valleys, texture...
- Editor-only: add a DyingStar tool to import/export a scene's server props to horizonserver's startup_items.json.
- You can no longer interact with something you can't actually see: picking up an object now requires a clear line of sight to it, and a vehicle door only opens from the handle on your side (outside on foot, inside when seated) when it isn't blocked.
- Vehicle steering now feels progressive and self-centring, with a speed-sensitive steering lock (sharper at low speed, more stable at high speed).
- Players who join now see the current state of everyone already in the world (torch on/off, equipped tool, carrying…), instead of only seeing it after the next change.
- Vehicle fixes: an empty vehicle no longer drives off on its own (it coasts to a stop), vehicles spawn with the hand brake on, a door left open is now visible to players who join later, and the truck's steering wheel turns correctly around its column.
- Vehicles can now use a real 3D model: working wheels and steering wheel, openable doors with look-at handles, Blender-authored collision, and in-cab screens. A door must be opened (look at its handle + E) before you can get in or out.
- Fixed wrong LOD settings for the VIP hab that caused a visual glitch. The correct model is now displayed when being close to it.
- Habs test - container
- feat: mining zones generate rock fields server-side on player entry (seeded, renewable)
  feat: small / medium / large mineable rock variants
  feat: per-zone mineral replicated via `mineral_id` (gold / iron / cryptonite)
- Fix bug when player go out its appartment
  Fix rock can't carry
  Network optimisation
  Add engine brake on vehicule
  Enhance loading screen when join the universe
- Upgrade the project to Godot 4.7
  enable HDR
- Fix designer-placed mining depots being duplicated in the database on every server restart.
- Add a 30-minute day/night cycle and a physical sky (with sunrise/sunset colours) to the sandbox.
- feat: FPS limit + field-of-view graphics settings (persisted)
  feat: working audio settings (bus volumes, input/output device, mic test)
  fix: settings menu active-category highlight + title; V-Sync label
  fix: main-menu and ERROR 1337 layouts no longer shift on window resize
  fix: pause menu button SFX
- You can now see other players turn their flashlight on and off.
- Improve cargo: drop an item in a truck's bed (or over the side) to load it, drive it around, and tip the truck to spill it. Changed render of  rear-view mirrors / reversing camera screens.
- Your video settings (monitor, resolution, fullscreen, v-sync) are now kept between sessions.
  New "Dev mode" toggle in the Video settings: it ignores the saved resolution/fullscreen on launch (handy when running several game windows at once).
  Other players' name tags no longer jitter, and are hidden when too far away.
- Toggle your flashlight while seated in a vehicle (driver or passenger).
  Spamming the vehicle reset key no longer makes the truck fly off.
  Stand in a truck bed to add your weight to its load, and load a crate by dropping it in the bed; carrying a crate no longer flips a truck.
  Mining rock pieces now weigh according to their size, and carrying one into a truck bed adds its weight to the load.
- You can no longer pick up items through walls; the carry prompt only shows when the item is actually reachable.
- Add an in-game text chat: shown by default on the left, F12 to hide/show, Enter to write and send, Escape to cancel, Tab to switch channel.
- Add food ration props (biscuit, nutrigris).
- All gameplay keys (vehicle reset/lights, brake & hand brake, the "Zapette" cleanup tool, the spawn
  wheel) are rebindable in Settings → Controls.
  The settings menu works: Controls list, Fullscreen/Windowed, Screen Resolution auto-filled from
  your monitor, Monitor selection.
  E embarks a vehicle; Y leaves it. one spawn wheel on T.
  Pause menu reordered (Resume / Settings / Return to menu / Quit); Settings opens the full menu.
  Start screen: a Quit button. The mouse cursor shows when opening the pause menu. The debug
  overlay stays in the corner at any resolution.
- Vehicles can show a live rear-view camera and side mirrors on in-cab screens (reusable RearCamera
  drop-in; "mirror" flips it left/right). The truck ships with a reversing camera + two mirrors.
- Vehicle head lights: a dev just drops Light3D(s) into the "vehicle_light" group of their vehicle
  scene (no code); the driver toggles them with L. Shown on the HUD and the in-cab dashboard.
  L is contextual: head lights while driving, the player's flashlight on foot. The flashlight is
  now visible to other players and starts off.
  A parked truck no longer creeps with the hand brake on (it freezes once stopped).
  The bed spills its whole load when the vehicle tips over.
- You can now retrieve a crate or rock you placed in a vehicle's bed.
  Cargo placed in a bed no longer disappears in multiplayer.
  A vehicle can no longer be loaded into another vehicle's bed.
  Seated players now count toward the vehicle's load (OVERLOADED).
  "[E] Carry" / "[E] Drop" prompts when aiming at a grabbable object or holding one.
  Carried objects are solid to the world and other players (but not to the carrier).
  A vehicle seat is freed when its occupant disconnects.
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
