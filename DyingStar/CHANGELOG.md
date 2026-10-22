# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Star map**: The places that belong to your missions, to other players and to corporations are now on the star map, each with its own icon.
- **Star map**: When a form is waiting for a place, clicking one on the chart picks it — you no longer have to aim at a planet.
- **Interface**: An objective now names the place it happens at and takes you to it on the chart.
- **Interface**: The goods and the units a contract asks for are chosen from the market's catalogue instead of typed in.

### Changed

- **Mining**: An extract now packs a single mineral: the button only lights up when one mineral holds a whole crate, and ore is counted in litres.
- **Interface**: The missions you issued are marked in the mission list.

### Fixed

- **Interface**: Interaction prompts no longer show through walls.
- **Vehicles**: A part behind a shut hatch can no longer be taken or seen through it.
- **Player**: Getting up from your bed no longer puts you through the wall into the next home, and you look ahead again.
- **Star map**: Your home shows over the storeys above it on the star map.
- **Star map**: The star map no longer drops the frame rate in a village.
- **Player**: The DataPad opens in god mode.
- **Performance**: The game no longer crashes when you quit it.
- **Performance**: The first ration, tool or place you meet no longer freezes the game a moment.
- **Server**: Passenger and delivery missions read your seat and your goods directly, instead of a presence refreshed once a minute without either.
- **Server**: Your position, a place and a mission zone are stored relative to their planet, so they no longer drift away from it as it orbits.

## [0.1.0-dev.202610211614] - 2026-10-21

### Added

- **Buildings**: Spawn homes are habitat containers, each with a bed, a bedside table and a wardrobe.
- **Buildings**: Container homes stand on several storeys, reached by walkways and stairs.
- **Buildings**: A container's plate shows its number, red when someone lives there and green when it is free, and its occupant's name is on the door.
- **Props**: Doors, drawers and the bedside lamp of your home open, close and light up, and everyone sees them as you left them.
- **Props**: The wardrobe's shelves take what you carry.
- **Player**: You can lie down on your bed and get up again.
- **Player**: Railings and fences can be vaulted over.
- **Star map**: Your home shows on the star map, from anywhere on its planet.
- **Interface**: Tapping a screen moves your hand to it with a touch sound.
- **Audio**: Container doors, wardrobes and drawers have their own sounds.
- **Buildings**: Every home has a shower, a toilet and a mirror.
- **Props**: The mirror shows the room and you in it, and its lights come on like a neon.
- **Props**: The shower and toilet lights come on when their door opens and go out once nobody is inside.
- **Buildings**: A mining village has about 250 homes.

### Changed

- **Interface**: Screens are clicked from closer.
- **Interface**: Furniture that is not yours shows a red prompt.
- **Props**: Doors stop when they meet a wall or a piece of furniture.
- **Interface**: The interaction prompt shows beside the crosshair.
- **Performance**: Only the homes near you are furnished, so a village of homes costs less to draw.

### Fixed

- **Graphics**: A village of homes no longer runs out of room for its shader effects.

## [0.1.0-dev.202610201627] - 2026-10-20

### Changed

- **Performance**: Servers stay smooth around busy villages: crowds of characters no longer recompute their route all at once.

## [0.1.0-dev.202610201544] - 2026-10-20

### Added

- **Interface**: The loading screen shows your place in the queue while the servers are full.
- **Props**: Bed
- **Props**: Bed table
- **Props**: Wardrobe
- **Props**: Shower Cabin
- **Props**: Restroom Cabin
- **Props**: Bathroom Sink
- **Props**: Mirror

### Changed

- **Props**: Standard shipping containers have their true dimensions, with collisions that match their shape.
- **Props**: Standard shipping containers cost less to draw from afar.

### Fixed

- **Props**: Standard shipping containers no longer vanish when seen from afar.
- **Props**: The yellow paint of the containers shows correctly again.

## [0.1.0-dev.202610192155] - 2026-10-19

### Fixed

- **Performance**: Game servers with nobody on them no longer use a full processor core each.

## [0.1.0-dev.202610192045] - 2026-10-19

### Added

- **Player**: A DataPad worn on the left wrist: raise it to read the services tablet on its screen, even at the wheel, and a green light with a beep tells you when something is waiting.
- **Vehicles**: Cruise control holds the speed you are driving at: set it with Ctrl+T, adjust it with the mouse wheel, and press either pedal to take back control.
- **Vehicles**: The truck's middle screen can show the star map or the rear camera, or stand by with the ARES Hauling logo: aim at it and press F to switch, for everyone aboard.
- **Vehicles**: Backing up shows the rear camera on the middle screen, whatever it was showing.
- **Vehicles**: The star map on the truck's screen is shared: when one passenger zooms or pans it, everyone aboard sees the same view.
- **Star map**: Buildings, dispensers, lifts, teleporters and vehicles appear on the star map, with their pictogram and their name on hover.
- **Star map**: The star map can be zoomed in down to the metre around you.
- **Star map**: The star map handles like an online map: drag to turn, right-drag to zoom, right-click to copy coordinates or drop a pin, Tab to search.
- **Audio**: The vehicle lift sounds an alarm at both landings while it is moving.
- **Audio**: Vehicle suspensions make a pneumatic knock when they take a bump, a pothole or a landing, heard by everyone around from that very wheel, louder and deeper the harder the hit.

### Changed

- **Vehicles**: Vehicles meet real air and rolling resistance: the engine keeps working at top speed, and thin air lets you go a little faster.
- **Player**: Your character starts and stops running more promptly, and moves smoothly instead of in small jolts.
- **Player**: Switching between walking and running no longer jolts the view.
- **Props**: Metal boxes, batteries and engines sound like metal when you pick them up and put them down.
- **Controls**: The speed limiter is now adjusted with the mouse wheel alone.
- **Audio**: Tyre noise grows louder and higher with speed, and fades out while the wheels are off the ground.
- **Audio**: Tyres scrubbing while you steer are quieter.
- **Vehicles**: The truck's headlights light the road ahead instead of a patch right in front of the bumper.

### Fixed

- **Vehicles**: Crates dropped into the truck bed are detected wherever the bed really is.
- **Star map**: Roads and canyons no longer jitter on the star map when zoomed in close.
- **Performance**: The game server slows down much less when many players arrive or when a region of the world moves to another server.
- **Server**: The game server no longer crashes at random while villages are being loaded.
- **Audio**: The driver no longer hears the tyres at full volume whatever the speed.
- **Vehicles**: The truck's rear-view screen shows the road behind the right way round, like the side mirrors.
- **Graphics**: Asphalt roads reflect the headlights instead of staying pitch black at night.

## [0.1.0-dev.202610161255] - 2026-10-16

### Added

- **Audio**: EVA thrusters hiss while you push yourself around in space, and players nearby hear it.
- **Audio**: Clothes rustle when you pick something up, work a door, get into or out of a seat, crouch or lie down.
- **Player**: Drivers hold the steering wheel with both hands, and their hands follow it as it turns.
- **Vehicles**: The dashboard power bar turns from green to red with the power asked of the motors.

### Changed

- **Vehicles**: Doors open when the hand reaches the handle, not the instant the key is pressed.
- **Vehicles**: The truck's driver sits a little closer to the steering wheel.

### Fixed

- **Performance**: The game server slows down less when many characters arrive at the same time.
- **Vehicles**: A truck falling off a cliff no longer adds speed and distance to its dashboard.
- **Vehicles**: Wheel dust stops when the truck leaves the ground.
- **Player**: Seated players can use screens again.
- **Audio**: Footsteps never play the same sound twice in a row.
- **Interface**: The credits list shows each author beside their work again.
- **Buildings**: The ration dispenser stands on levelled ground.

## [0.1.0-dev.202610151839] - 2026-10-15

### Fixed

- **Buildings**: The vehicle lift no longer has missing pieces at some distances when the structures draw distance is not at its default.
- **Player**: Stepping onto the vehicle lift no longer makes you flip over in other players' eyes, nor slows you down.
- **Performance**: No more short freeze when stepping onto the vehicle lift or entering a building.
- **Vehicles**: A truck driving onto the vehicle lift no longer gets stuck as if broken.

## [0.1.0-dev.202610142314] - 2026-10-14

### Added

- **PlanetTech**: New debug view of the safety nets under the ground (Settings > Debug), in red where the fallback floor pokes out of the terrain, in magenta where the fall catch rises above it.
- **Star map**: Below 6,500 km, the view follows the planet's rotation: the ground no longer slides away.
- **Props**: ARES vending machines: vehicle parts in the garage, rations in the mining villages, the mining tool at the cargo depot. Pick on the screen, wait for the delivery, take your items from the hatch.
- **Audio**: The vehicle lift is heard: its winch, the platform rolling along the rail, and a heavy clunk when it starts and stops.
- **Vehicles**: New truck dashboard, readable on its screen: speed, warning lights, a box per component bay, power gauge, batteries.
- **Vehicles**: An open door blinks and beeps on the dashboard, faster as the wind is about to slam it.
- **Vehicles**: "Stand up to fit or remove a part" when crouched or prone at a vehicle part.
- **Player**: Your own head now casts its shadow.
- **Interface**: The home screen says the game is in development and many assets are placeholders.
- **Vehicles**: Added a "vehicle_lift" folder and its contents to "addons" (scripts, models, textures, etc.)
- **Interface**: Added a test in guid_3d to ensure the presence of a viewport
- **Economy**: "My contracts" lists what you raised, and an issuer objective can be confirmed.
- **Player**: Auto-vault, climb and step-up: your character crosses obstacles automatically — vaulting over low ones, climbing onto ledges (including elevated platforms), and stepping smoothly up small obstacles that used to block you.

### Changed

- **Controls**: The torch has its own key, U (D-pad up on a gamepad): switching on the head lights no longer switches the torch on.
- **Controls**: Vehicle head lights stay on L and move to D-pad down on a gamepad.
- **Star map**: Canyons are drawn lighter and as curves, as the ground shows them.
- **Mining**: You no longer start with a mining tool: get one at the ARES Mining machine of the cargo depot. Press the action key to take it or to put it down; it stays yours.
- **Interface**: 3D screens are used with the crosshair: walking past a console no longer locks the view.
- **Props**: Small items on the floor can be picked up standing.
- **Vehicles**: Engine and battery parts show the same icons as the dashboard.
- **Buildings**: Teleporter: destinations grouped by type and sorted, bodies marked planet / moon / giant, works with a gamepad.
- **Buildings**: Building lights switch on at dusk (1900 lux), the garage is lit at night.
- **Weather**: Wind-blown dust takes the colour of the ground and fades between biomes; much cheaper, and gone high above the ground.
- **Vehicles**: Enabled the addon in project settings
- **Server**: Modified the "rollForward" parameter in global.json to allow the C# project to build if the SDK version is higher than recommended
- **Server**: The "websocket_url" line in "client.ini" was also modified; it probably shouldn't have been.
- **Interface**: Fold the services tablet's eleven apps into Social, Economy and Properties — eight tabs in the bar, Reports and System left in PLUS.
- **Star map**: Points of interest no longer ask for coordinates — take where you stand, or pick a point on the chart.
- **Economy**: Mission zones take a star system or one of your own POIs; the old scene and area kinds were always rejected.
- **Economy**: The group share line is on your own contracts only, and names the group.
- **Buildings**: Adjacent buildings: when two buildings are close enough for their flat areas to touch, the smaller one adjusts to the level of the larger one.
- **Vehicles**: Vehicle cab screens** (rear-view mirrors and dashboard) turn off when the engine is off and back on with ignition.

### Fixed

- **PlanetTech**: The canyon wall no longer has a large triangular hole next to the road.
- **PlanetTech**: The ground no longer flickers along the edge of the canyons.
- **PlanetTech**: The canyon under a bridge is no longer filled with ground.
- **Mining**: The depot belts carry rocks and crates to the end even when the server is busy.
- **Interface**: With a larger interface size, the settings no longer lose their left side off the screen: long setting names now wrap onto two lines.
- **Player**: Players no longer hop on the spot on sharp mountain crests and crater rims.
- **Vehicles**: A truck parked on a sharp mountain crest is no longer dropped back onto it over and over.
- **PlanetTech**: On Tarsis 3, no more holes in the ground beside the roads that run along the edge of a crack.
- **PlanetTech**: On Tarsis 3, the small steps and slits where two stretches of ground meet are gone, in the open as in the villages.
- **Interface**: Long audio device names no longer push the Audio settings off the left of the screen; they are shortened, and shown whole on hover.
- **Interface**: Right after launching the game, Settings, Credits and Back work again in the main menu.
- **Player**: A player who left the game crouched, prone, floating or at the wheel is no longer stuck in that posture on reconnecting.
- **Mining**: Players no longer spawn with the mining drill on their belt before taking one from the ARES Mining machine.
- **Buildings**: Players no longer stay on "Spawning" near the cargo depot, whose ground was rebuilt without end.
- **Star map**: The debug panel shows over the star map again.
- **Star map**: Canyons no longer show darker blocks where they meet.
- **Interface**: Play hints no longer cover the chat or the voice buttons; Escape closes the tablet opened with F2.
- **Interface**: Fix the tablet drawing nothing: a mounted section was nested too deep and was given no height.
- **Props**: Cargo depot shelves: each depot creates its 193 network shelves only once, and a saved flag prevents them from being recreated upon server restart.
- **Buildings**: Building aprons: the flat area around a building is no longer deformed by neighboring buildings.
- **PlanetTech**: Ground texture: it no longer stretches on steep slopes around buildings.
- **Social**: Fix players showing as offline in the contacts list and on profiles: the client now uses the
  token's `sub` as its player id, instead of a random UUID regenerated on every session. This also
  stops the duplication of profiles (`Player_xxxxxxx`) on each reconnection.
  Fix player names in social: they now come from the account (`preferred_username`) instead of the
  generated pseudo sent by the game server.
  Fix presence location reporting the planet's network name: a player on SandBox now reports
  `tarsis · tarsis_3` instead of an empty system and an unknown scene.
  Fix the chat not opening with F12. The chat was never connected to the message broker, so no
  message could be received or sent.
  Private messages: pin one conversation at a time in the message box, showing the correspondent's
  name. The header is clickable and lists every conversation, those with a new message first, and
  can be closed with the ✕.
  The message log now shows only the pinned conversation instead of mixing every private message
  together.
  Write to a contact straight from their card, with Enter sending, without leaving the card.
  Social notifications (friend request, friend request accepted, corporation joined) now appear as
  a stack at the top of the screen. Clicking one opens the screen where it can be handled.
  Diagnostics: a new panel block showing the chat broker connection and the voice room, refreshed
  every second while the panel is open.
- **Interface**: Pause menu** no longer lets the character move, act, drill, or look around while it is open.

## [0.1.0-dev.202610112359] - 2026-10-11

### Added

- **Weather**: The wind now blows dust across the plains: it streams around you, veils the distant relief and glows in the beams of lamps at night.
- **Weather**: Footstep and tyre dust drifts with the wind.
- **Weather**: You hear the wind, muffled in a cab or behind walls.
- **Graphics**: New "Wind-blown dust" setting (Off / Low / High).
- **Weather**: Vehicles and players now raise dust from the ground: a trail behind the truck's wheels and a puff at each step, thicker on sand and dirt, lighter on rock, none on metal. The truck's headlights now cast shadows.
- **Graphics**: Other planets and moons now show their atmosphere from afar: a hazy world looks brighter, a thick one paler or whiter, and the air's edge glows once it is large enough on screen.
- **Social**: Add client connectivity to the game service
  Add social service
  Add economy service
  Add mission service
  Add inventory service
  Add market service
  Create an interface (F3) with applications that call these services
  Initialized code allowing the Godot server to authenticate with Keycloak to access internal service APIs
- **Interface**: A short list on the left of the screen shows the keys you can use right now — on foot, at the wheel, carrying, with the drill — and learns: each line goes once you have used its key, and the next ones (speed limiter, walking pace, roll…) come after the basics.
- **Star map**: The star map shows its controls the same way, on its left.
- **Audio**: A separate volume for the menu music (Settings > Audio), and the music no longer cuts off when you arrive in a town.
- **Controls**: Accelerate and slow down at the wheel have their own controls: put them on the gamepad triggers without changing how you walk.
- **Vehicles**: An open vehicle door now slams shut once you drive fast enough — sooner in thick air, later up on the plateaus.
- **Graphics**: Every planet and moon with an atmosphere now has its own sky.
- **Buildings**: Mining villages get container yards, stacked up to three high, and ore skips.
- **Buildings**: Factory cities: industrial zones with mining depots, cargo depots, garages, two teleporters and container yards.
- **Buildings**: Every mining village has a teleporter cabin, and the orbital station has its own again.
- **Buildings**: Village buildings wear neon signs (garage, teleporter, cargo and mining depots), in your language.
- **Buildings**: Mining villages get floodlights, lampposts and crates; the floodlights' generators hum.
- **Controls**: New controls help: press F1 (or hold View on the gamepad) to see your keys, with what each one does.
- **Interface**: New Credits screen in the main menu and the pause menu: everyone who made the game's music, sounds, models and textures, scrolling like a film's credits with one of the community's tracks playing.
- **Interface**: Every track on the Credits screen has a play button to listen to it.
- **Audio**: Ten new music tracks: in space, in the wild, in the menu, and in the mining and factory villages, which had no music until now. Tracks whose author is unknown say so in the credits: if one is yours, contact us on Discord.

### Changed

- **PlanetTech**: The terrain cache is moving to v60 to account for re-exported roads.
- **Performance**: Each export (server, Linux, Windows) receives its own build number (date, time, and random number), which invalidates the chunk cache upon the first launch. In the editor, there is no number, and nothing changes.
- **PlanetTech**: QGIS modifications: new POI types, auto-filling of population/radius, and zones colored by rock type.
- **PlanetTech**: New tarsis_3 export from QGIS.
- **Mining**: Rock weight: a factor reduces rock density (WEIGHT_REDUCTION_FACTOR, set to 25). They are lighter, can be carried sooner, and require fewer cuts.
- **Mining**: Rock color: rocks take on the color of the ground where they spawn, including its brightness and matte finish. Broken pieces retain this color.
- **Vehicles**: The truck reaches the same top speed whatever the number of motors fitted (about 100 km/h); more motors mean more pull on slopes, not more speed.
- **Vehicles**: The truck still slows down by itself when you release the accelerator.
- **Star map**: The star chart now opens inside the DataPad's Navigation tab (F2, or F3 ▸ Navigation), in the tablet's frame.
- **Controls**: The DataPad (F3) now appears in Settings > Controls under its name, in the controls help (F1) and in the play hints.
- **Player**: Developer free-flight renamed "God mode": the mouse wheel now changes its speed (shown at the top of the screen), and the middle mouse button lands you on the ground below; your own body is hidden while flying.
- **Performance**: Village buildings are now streamed in rather than all being built at once;
- **Buildings**: $BoxDetectorEnd removed from mining_depot.gd;
- **PlanetTech**: Feat(planet), your work in progress (85 files): longitude convention aligned with QGIS, along with the corresponding scenes and tests, plus the new tarsis_3 export and its re-baked grade_profiles.pack.
- **Vehicles**: The decelerate key now brakes while rolling forward and only backs up once stopped, and the brakes stop a loaded truck as hard as an empty one.
- **Vehicles**: Vehicle parts: "Fit" shows in green, "Remove" in yellow, and every interaction prompt sits on a dark patch that keeps it readable.
- **Vehicles**: Get into a vehicle by looking at its seat through the open door, then pressing the action key.
- **Buildings**: Street lamps, floodlights and neon signs now switch on when it gets dark, not only at sunset: in the valleys under the corundum veil they light up in broad daylight.
- **Buildings**: Brighter floodlights.
- **Props**: Containers carry the ARES logo and keep their detail much further away.
- **Buildings**: Street lamps, floodlights and signs come on at dusk and go off at dawn, one after the other.
- **Vehicles**: The truck can be started and stopped at any speed, and its engine revs now follow its wheels.
- **Vehicles**: A vehicle's parts can no longer be removed while its engine runs.
- **Audio**: Footsteps on sand, dirt and gravel play a placeholder sound for now (their sounds had no known source).

### Fixed

- **Mining**: Carrying: a broken piece is now held by its actual center, rather than the origin point of the original rock. It no longer appears offset in your hands and rotates on its own axis.
- **Mining**: Rock lighting: texture relief has been corrected. A rock no longer appears entirely bright or entirely dark depending on how it is placed.
- **Vehicles**: The truck's motors and batteries now fit their hatches (60 × 40 × 30 cm) instead of sticking out of the truck's side.
- **Player**: Fixed the respawn point at the house exit; it used to launch us into space.
- **Interface**: Main menu: the outpost stands upright again after the map re-export, the figures and trucks rest on the ground instead of sinking into it, and the lampposts are now large floodlights.
- **Performance**: No more 400ms stutter every 2 seconds on the client side;
- **PlanetTech**: The bake tool and hole_probe.gd have been fixed.
- **Graphics**: Planets and moons seen from orbit are now fully lit: no more black squares over rocky or grassy regions, and no more grid pattern in the air over hazy worlds.
- **Graphics**: Fixed the sunlight not following the time of day or the ride while seated in a vehicle, and jumping when getting out.
- **Server**: Fixed a game crash under certain conditions
- **Vehicles**: The truck no longer has a light inside its cabin.
- **Star map**: Clicking a planet, moon or point of interest shows its info card again.
- **Props**: Containers now stand in levelled storage yards in the mining villages and factory cities, and no longer float or sink on slopes.
- **Buildings**: Teleporting to the orbital station works again.
- **Props**: Crates can no longer be picked up by hand, and the "Carry" prompt only shows on what you can carry.
- **Player**: Your torch beam is no longer cut by the shadow of your own shoulders.
- **Vehicles**: Server no longer crashes when a battery is removed.
  batteries() and the vehicle display now ignore batteries that have already been removed.
  The dashboard display no longer runs on the server, eliminating "String formatting error" spam.
  fix(vehicle): an installed part no longer collides with its truck.
  Parts (battery, engine) disable collision with their truck upon creation, preventing the truck from flying off when changing servers.
  fix(server): trucks continue moving when changing servers.
  At the border, the transferred truck resumes its previous state and speed (this does not apply when loading from the base).
  Speed ​​is applied as soon as the truck is no longer frozen, within a 1.5-second limit.
  An active copy is adopted, preventing the driver from being "rubber-banded" back.
  The "no ground" freeze is lifted upon adoption.
- **Player**: The character could keep walking up a slope after the key was released.
- **Interface**: Screenshots taken after resizing the window were cut off.
- **Controls**: On AZERTY and other layouts, the F1 help lit the microphone key at the wrong place.
- **Controls**: Dev: the + / - time keys change the hour instantly again.

## [0.1.0-dev.202610042359] - 2026-10-04

### Added

- **Server**: New system when create new server (server meshing dynamic) and send items and players on the new server
- **Buildings**: Add garage
- **Vehicles**: New: the T1 battery. The truck now runs on energy: it will not start without a charged battery, and a battery empties as the motors pull (slopes and heavy loads drain it faster).
- **Vehicles**: A truck uses one battery at a time and moves on to the next when it is empty; the battery in use cannot be removed while the engine runs.
- **Vehicles**: Each battery shows its charge (in kWh) on its side, and the truck's dashboard shows one bar per battery with its percentage (green, orange, red).
- **Vehicles**: Batteries can be spawned from the spawn wheel.
- **Audio**: New music: "Balade" (LRC), "A starry night" and "Meloncholia" (Koothka), "EVA Atmo 1" (Solstium), "Syd where are you" (spaceman), in EVA, space stations and the wilderness.
- **Star map**: Every control (click, double click, right click, middle click, wheel, gamepad) can now be rebound in Settings > Controls, and the help line at the bottom of the map shows your own keys.
- **Star map**: The gamepad's X button resets the view.
- **Vehicles**: The truck has a registration plate.
- **Audio**: New music in the wilderness, by Plx.
- **Buildings**: POI Villages: The server generates village buildings and can activate the village when Horizon requests housing for new players.
- **Buildings**: Added a basement area and a connecting staircase leading down to it.
- **Graphics**: Created a new led_panel_1x1m.tscn light scene.
- **Graphics**: New in-game benchmark (Settings > Graphics > Benchmark): the view turns slowly on the spot while each graphics option is lowered in turn, then your settings are put back. It writes a report of what each option costs on your machine (also copied to the clipboard) to send to the team; "Open folder" shows the reports.
- **Controls**: Gamepad support: play with a controller (Xbox layout by default), rebind its buttons in Controls (separate Keyboard / mouse and Gamepad columns), and on-screen prompts follow the device you use.
  Menus can be driven from the gamepad: D-pad / stick to move, A to confirm, B to go back, LB / RB for categories, LT / RT for the top bar.
  The star map shows longitude, latitude and altitude under the cursor near a body.
  FPS / GPU shown in the settings tab row; new Interface volume slider.
- **Audio**: Music now follows where you are: menu, space, points of interest and places with their own music, with cross-fades between tracks.
- **Audio**: New tracks: Beyond the Horizon, Tin Can.
- **Audio**: Footsteps on metal.
- **Audio**: Debug panel: a Music section shows which track plays and why.
- **Server**: Added ESG (EntityStreamingGodot)
- **Star map**: Star chart (F2): the canyons now show, as real relief near the ground and as dark strips from higher up.
  Star chart: tunnels and bridges are marked on roads and railways when you are close enough (about 30 km up); railways are drawn with their sleepers.
  Star chart: points of interest that overlap are grouped under one marker with a count; they separate as you zoom in, and clicking a group zooms onto it.
  Star chart: over a selected orbital station, the middle mouse button now orbits around the station.
  Fixed: roads and railways on the star chart were cut into pieces when seen from high up.
  Controls: you can now bind key combinations (Ctrl, Alt, Shift + a key) and any mouse button, the wheel click included.
  Controls: a combination no longer also triggers the action bound to the key alone (Ctrl+E no longer fires E).
  Graphics settings: the frame rate and GPU time are shown at the top of the tab, colour-coded; the hour slider is back in the menu.
  Fixed: the Medium ground detail lost the hex tiling of the terrain.
  Debug panel: the Server box lists every zone as a table that scrolls on its own.
  Truck: gentler steering.
- **Interface**: New setting: interface size (Settings > General).
- **Interface**: The main menu is now a live scene on Tarsis 3 at sunrise, with an outpost, workers and trucks on the road; the camera moves with each menu screen. It can be switched off in Settings > General.
- **Graphics**: A tuning scene to compare the graphics options on real ground, at any hour, from Settings > Graphics or the home screen.
- **Interface**: A progress bar on the loading screens.
- **Graphics**: New graphics options: presets (auto-detected for your GPU on first launch), FSR 1 / FSR 2.2 upscaling, render scale, MSAA / FXAA / SMAA / TAA, shadow quality, SSAO / SSIL / SSR, bloom, anisotropic filtering, debanding, atmosphere and ground quality, and terrain / buildings / vegetation draw distances. Every option explains itself on hover.
- **Graphics**: An in-game graphics panel (Settings > General) to compare options live, with FPS and GPU time; hold AltGr to use the mouse.
- **Interface**: The screenshot and video folders open from the top of Settings > Graphics.
- **PlanetTech**: Organic edges: meandering (domain warp) and eroded edges (fBm)
- **PlanetTech**: [Volcanoes] New pack types: volcanoes (8), lava flows (9), fumaroles (10), drawn in QGIS
- **PlanetTech**: [Volcanoes] Volcanoes: 5 presets (stratovolcano, shield, caldera, cinder cone, dome), client-side lava lake and plume
- **PlanetTech**: [Volcanoes] Lava: never flows uphill (DESCENT rule); shader states: active / cooling / solid
- **PlanetTech**: [Volcanoes] Fumaroles: deterministically placed events, gas deposits in vertex colors
- **Performance**: [Performance] Pre-calculation: a new tool, `tools/bake_grade_profiles.tscn`, calculates line profiles, crevasse crossings, and bridge decks once and for all. It writes them to `grade_profiles.pack`, which the game loads at startup: 827 ms instead of several minutes.
- **Buildings**: New: Palaka-Pital Orbital Station, on a real orbit around SandBox (400 km, 1 h 44 per orbit), reachable by teleporter and with a cabin aboard to come back, with rings that turn to give their floor gravity.
- **Player**: New: EVA with real inertia: roll (A/E), up/down (Space/Ctrl), brake (X), a new EVA tab in the key settings, a floating animation, and orbital drift beside a station.
- **Star map**: New: star map shows stations, a view cone, and opens on you the first time and after you travel.

### Changed

- **Vehicles**: Trucks now leave the factory with two T1 motors and a T1 battery.
- **Star map**: Its debug numbers moved to the debug panel, behind their own switch in Settings > Debug.
- **Controls**: Mouse buttons are named in your language in the controls page.
- **Player**: No more head bob: the first-person view stays steady when walking, running, standing still or turning on the spot, while still lowering when you crouch or lie down.
- **Interface**: The "Gamepad detected" window's OK looks like a button.
- **Interface**: Every setting in the Godot inspector now explains itself when hovered (for creators).
- **PlanetTech**: On a first launch, the ground around you appears first instead of the distant landscape.
- **Performance**: The terrain loads about three times faster on a first launch or in a new area.
- **PlanetTech**: When flying fast, new ground is drawn in less detail so it keeps up with you; ground you have already seen stays detailed, and full detail comes back when you slow down.
- **PlanetTech**: The terrain where you look now comes in first.
- **Player**: Smoother take-off and stopping when flying fast.
- **Performance**: The terrain loads about three times faster on a first launch or in a new area: its data is now downloaded over several connections at once.
- **Performance**: Server performance: TPS has risen from around 7 to 55, and player logins are no longer delayed.
- **Performance**: Stuck NPCs: They now space out their retry attempts, reducing navigation requests by approximately tenfold.
- **Performance**: NPCs awaiting a path: They switch to standby mode—just like inactive NPCs—to save on physics processing.
- **Graphics**: Updated the led_panel_1x0.3m.tscn light scene (including a light intensity adjustment).
- **Performance**: Much higher frame rate in an atmosphere: the sky and the haze are computed with a precomputed table instead of a per-pixel loop (about 41 → 70 fps at Ultra on an RTX 3090 at the spawn).
- **Performance**: Fewer periodic hitches from the planet's rotation.
- **Performance**: Truck dashboards and the star map are no longer redrawn when nobody looks at them.
- **Controls**: Mute all game sound (N) and mute your microphone (M) are now listed in Controls > General and can be rebound.
- **Interface**: The chat and the HUD are hidden while the pause menu is open.
- **PlanetTech**: Chunk disk cache: the version has been bumped from v56 to v58, so old chunks with holes or offsets are being rebuilt.
- **Interface**: New menu layout: a bar across the top with the logo, settings in tabs, smaller text, and the scene visible beside the settings.
- **Interface**: Esc in game opens the settings directly, over the game.
- **Interface**: Debug options moved to their own Debug tab.
- **Interface**: The menus fit a centred 16:9 area on wide screens, and follow a switch between windowed and fullscreen.
- **Interface**: The home and pause menu buttons share one look; the home buttons stand on one row.
- **Interface**: The debug panels (Alt+²) are now one panel on the right that never overlaps itself, with the ground, movement and vehicle readouts in it, and the number of terrain chunks on screen.
- **Interface**: The dev-clock warning now appears in that panel.
- **PlanetTech**: [Crevasses] Clean vertical walls: corrected quad diagonals, 1.6-step snap range, wall-specific normals
- **PlanetTech**: [Crevasses] Integer hash instead of sine: bit-identical results across all platforms
- **PlanetTech**: [Crevasses] Bit-exact C# counterparts (TileFrameNative, CrackVoronoiNative)
- **PlanetTech**: [Volcanoes] Crater rim lowers on the flow side: lava spills over by 2m instead of carving a 203m canyon
- **Performance**: [Performance] Line carving in C# (GradeCarveNative): 32 → 12 µs per call
- **Performance**: [Performance] Chunks beneath a lava flow: 30–50% reduction in generation time
- **Performance**: [Performance] Indexed stale chunk pass: 200–440 ms → 1–5 ms (fixing the 1–3 FPS drop near lava)
- **Performance**: [Performance] Chunk disk cache read/write off the main thread: ~330 ms/s → < 7 ms/s ms/s
- **Performance**: [Performance] Chunk construction near a line: it now reads only the relevant section of the profile instead of traversing the entire line (212,000 nodes for the loop rail). The result is bit-for-bit identical.
- **Performance**: [Performance] Memory: terrain samples taken every 5m are discarded once the profile is calculated, freeing up ~140 MB.
- **PlanetTech**: [Performance] Stale data: if the baked data no longer matches the source data (new export, modified crevasses or roads), the game recalculates it and displays a warning. A test fails, and `link_modifiers.py` reminds the user which command to run again.
- **Server**: [Miscellaneous] Lint limit raised to 6,000 lines; two new test suites added (profile splitting, baking).
- **Controls**: Changed: `action` moved from E to F, and the separate `interact` key is gone: F does one thing at a time.

### Removed

- **Graphics**: The graphics tuning scene is gone: the settings now show the scene beside them.
- **PlanetTech**: [Volcanoes] Removal of old volcanic biomes (migration script provided)
- **Buildings**: Removed: the teleporter's Return button.

### Fixed

- **Server**: If your body leaves the scene tree during a transfer, it is placed under the recreated truck (or under the planet).
- **Server**: You sit back behind the wheel, and the camera returns to you. You no longer see through another player's eyes.
- **Server**: The seat is vacated before a transferred driver is erased, and their body is removed from the truck.
- **Server**: The truck is destroyed at least two physical frames after its driver, and removed from physical space beforehand. This should fix the Godot server crashes.
- **Server**: The driver registered in the database is now the actual occupant of the seat. A departing driver is erased after 10 seconds.
- **Vehicles**: Engines put back into a truck stay in their bay after a server restart.
- **Performance**: Far fewer hitches when walking and driving: the terrain's level of detail is now worked out in the background.
- **Performance**: Flying fast (EVA) no longer freezes the game for seconds while the terrain catches up.
- **PlanetTech**: No more holes blinking in the ground ahead of you while you move.
- **Performance**: No more freeze when you fly away from a busy area.
- **Interface**: Fixed a crash a few seconds into the main menu on a first launch.
- **Performance**: No more long freeze when slowing down or arriving over ground you have already seen.
- **Buildings**: Terrain: On slopes, buildings sit flush on their platforms, and the ground between them no longer has a jagged, saw-tooth appearance.
- **Graphics**: Building lamps no longer blink: only the nearest lamps cast shadows (the others still light), which is also faster at night.
- **Interface**: Main menu: trucks stand on their wheels and the workers' feet are on the ground.
- **PlanetTech**: A planet body waits for its terrain collision before turning dynamic
- **Controls**: N and M could not be typed in text fields, such as the controls search box.
- **Interface**: Settings: the line under the pointer is highlighted again, and the background behind the settings is darker and fades out more smoothly.
- **PlanetTech**: Holes in front of the teleporter: in the village, terrain vertices are no longer offset toward the edge of an un-excavated fissure, and the terrain around buildings connects seamlessly again—both visually (mesh) and physically (collision).
- **PlanetTech**: Step between chunks: on either side of a trimmed tile boundary, both chunks now read the same height. The 24.5 cm step is gone, in both GDScript and C#.
- **Interface**: Tooltips are readable: dark background, wrapped text.
- **Interface**: The menus did not resize when switching between windowed and fullscreen.
- **Performance**: The game could freeze when entering the universe from the main menu.
- **Interface**: The dev clock offset carried over to the next connection.
- **Controls**: Holding AltGr made you sink in EVA; F7 photos showed the graphics panel.
- **Performance**: [Performance] Performance bug fixed: the modifier tile cache performed a linear traversal—under a lock—every time a height was read. Threads were blocking each other, and performance degraded over time.
- **Player**: Leaving a planet's air no longer drops you in the middle of the system.
- **Props**: A crate carried through the teleporter (or a truck's load sent to another body) is no longer deleted and can be put down.

## [0.1.0-dev.202609272359] - 2026-09-27

### Added

- **Vehicles**: Progressive steering. Tap or hold the arrows to turn the wheels little by little; they keep their angle when you let go, and straighten up gently while rolling.
- **Vehicles**: Speed limiter. T turns it on or off, Alt + mouse wheel sets the limit in 5 km/h steps. Shown on the dashboard: green when on, red while it holds the truck back.
- **Vehicles**: Odometer on the dashboard, kept across sessions and server restarts.
- **Interface**: F7 takes a photo without any interface; F8 takes a screenshot with the debug panels for bug reports. Both are saved in the game's screenshots folder and copied to the clipboard.
- **Interface**: Settings › Video: a button opens the screenshot gallery.
- **Star map**: The star map now draws real ground: relief at its true height, coloured by the rock it is made of, with its mountains, its roads and its railways. Towns show how high they stand. The ground refines as you approach and fills itself in from the tile service, and it no longer claims detail it does not have.
- **Graphics**: Objects resting on a planet now blend into the ground instead of meeting it on a hard cut line: the terrain's own colour and texture rise over the base of buildings, rocks, crates and props, with an irregular, wind-drifted edge. Interior walls and flat surfaces are left clean, and the band is lit like the ground it imitates, so it no longer darkens against a shaded wall.
- **Interface**: Added a language setting (Automatic / English / French) under Settings ▸ General, applied immediately and remembered between sessions.
- **Vehicles**: The driver's dashboard now shows the slope you are actually on next to the steepest one your engines can climb, so you can see how much is left. And vehicle components are marked with a pictogram of what they are — readable from either side of the truck, and from above when one is lying on the ground.
- **Vehicles**: Vehicles are powered by engines you can actually see. The T1 motor is an object you pick up, carry and bolt into one of the truck's four hatches — and what is fitted is what decides how hard it pulls, how steep a slope it climbs and how fast it gets there. Take one out and the truck suffers; take them all out and it will not start. A new Settings option hides the driver dashboard.
- **Buildings**: Added a teleporter cabin for testing: pick a system, a body and a point of interest from its screen,
  or type a longitude, latitude and height, and you are put down on the ground there. Vehicles parked
  in the cabin and anybody standing in it travel with you, and RETURN brings you back. Replaces the old
  seven fixed pads. Known limitation: leave the vehicle before jumping — a seated passenger's own view
  and controls may not survive the trip yet.

### Changed

- **Performance**: Enhance performances on chunks
  Enhance starmap
  add/fix CI for GUT tests
- **Interface**: F6 recordings are now saved in screenshots/records.
- **PlanetTech**: Update road to can't have more than 10 degres of slope
- **Interface**: The in-game HUD is now translated in English and French. Interaction prompts show the key you actually bound, on your own keyboard layout, instead of a hardcoded one.
- **Interface**: The menus are now fully translated in English and French. Keybindings are grouped into families (General, On foot, In a vehicle, In flight, Debug), and settings rows highlight under the pointer.
- **PlanetTech**: Manage snap to planet surface + update terrain mesh in editor and runtime
- **Performance**: Players optimization when have many players near me
- **Mining**: Rock impurities: mountain-driven colour and ore for every corundum
- **PlanetTech**: Update montain to have canyon on corundum zones. Fix border of canyons and finish in the begin of mountains

### Fixed

- **Controls**: A mouse binding with a modifier (e.g. Alt + wheel) lost its modifier once remapped.
- **Interface**: Debug panels showing "Soon™" right after being turned on.
- **Interface**: Standing at a console no longer drags your view towards it. Lean the pointer on the edge of the window to look across a screen too wide to take in at once, the view holds still while you read, and typing into a field no longer triggers gameplay keys — Escape hands the keyboard back. Panels now redraw only when they are visible, and a keystroke reaches the console you are using instead of every screen in the world.
- **Star map**: The teleporter and the system chart list the planets again in exported builds.
- **Audio**: Footsteps on sand and stone now play their own sounds instead of an error marker. Footsteps on metal still play that marker, pending a freely licensed replacement.
- **Vehicles**: Fix problem with seat in the vehicule
- **Vehicles**: Vehicle safety mechanism fix: it does not appear to rise high enough above the chunk when passing underneath it.

## [0.1.0-dev.202609202359] - 2026-09-20

### Added

- **Server**: [server] add secutiry for vehicle (like players)
- **PlanetTech**: Add mountain
- **Server**: Server performance profiling setup ([debug] perf=true): frame breakdown ([Perf/frame]), script-based attribution ([Perf/bands], opt-in), node census, Horizon messages, NPC tick breakdown—each of these issues was identified using this tool.

### Changed

- **Server**: [server] Increase number of items managed in jolt
- **Server**: Atomic file cache for server meshing dynamic (collision mesh for server)
- **Performance**: Shared navmesh cache (NpcNavCache): 72m tiles on a grid, one map per 5×5 cell block to allow roads to span tiles; geometry collected via physics queries and extracted on a worker thread; TTL, invalidation, eviction; parked trucks carve out the mesh.
- **Performance**: Lightweight NPCs: interleaved 30Hz tick, unnecessary sub-trees disabled server-side (UI, mining tool, raycasts, NavigationAgent3D), replication only when the pose changes.
- **Performance**: Reduced overhead: static props and parked vehicles at 6Hz, cached HEALPix rings for pins, time-sliced ​​pin scanning, mining logic running without the NPCs.
- **Performance**: Measured: 47 NPCs → from 5 fps / 43 TPS to 60 / 60; 93 NPCs → 60 TPS.

### Fixed

- **Server**: [server] Fix stdout
- **Performance**: Problem: 50 to 90 walking NPCs were dragging the server down to 5 fps. Each NPC was baking its own navmesh (analyzing the entire planet on the main thread, Recast bake at 0.1m, re-baking every 18m).
- **PlanetTech**: Fix chunk problem
  fix player safety mesh for tunnels
  Optimizations, prevent draw rail and roads too far away and it's not visible
  fix floor of tunnel
- **PlanetTech**: Embossing highway
  fix enable debug items
  fix hex-tiles AMD cards

## [0.1.0-dev.202609132359] - 2026-09-13

### Added

- **PlanetTech**: Planet tech wth roads, QGIS export, refactoring
- **PlanetTech**: Editor only: a "Fly in planet frame" toggle in the 3D viewport toolbar flies the view over a body with up always up and forward following the curvature, instead of the world-aligned camera that goes sideways away from the pole.

### Changed

- **Performance**: Enhance calculation of chunks from -26 to -66 %
- **PlanetTech**: Usage of tiles (points) into a web server and use it as streaming
- **Performance**: Enhance client perf debug

### Fixed

- **Vehicles**: Fixed the passenger's seated view sitting too low in vehicles: the driver and passenger poses place the head differently, and each now has its own eye height.
- **Vehicles**: Players riding a vehicle now belong to that vehicle's frame: the ride is smooth for driver and passenger alike, and their position is no longer re-sent over the network on every tick while the vehicle moves.
- **Interface**: The debug panel now shows the real altitude above the reference sphere alongside the height above the ground, and player coordinates keep updating while riding a vehicle.
- **Interface**: Fixed the pause menu opening over a game that kept running (the camera still turned underneath), being unable to leave Settings > Controls with Escape, and player name tags staying at standing height while crouched or prone. Remapped keys are applied again at startup instead of only after opening the controls page. Escape now cancels a key rebinding instead of being bound, and the jump binding is named "Jump / Vault".
- **Player**: Walking at the top of the mouse-wheel range no longer breaks into a jog: the whole range is a walk, played faster, and only sprint changes gait.
- **Vehicles**: Players sitting in a vehicle are now shown seated to everyone, including players who connect or come into range after they sat down.
- **Performance**: Fix client locked at 6 FPS: LiveKit mic queue size was in ms, not samples
  add debug code
- **Player**: The first-person view no longer swings off centre as you look around, and you no longer see your own neck when running or turning your head.
- **Player**: Low steps, kerbs and stairs are climbed reliably, including through doorways and under low ceilings where they used to block you.
- **Vehicles**: Trucks no longer tip over in a hard turn, their wheels now move with the suspension for everyone who can see them, and their tyres are audible — scuffing as you turn on the spot, rolling as you pick up speed. The mini truck comes with a new model and four interchangeable beds.

## [0.1.0-dev.202609062359] - 2026-09-06

### Added

- **Performance**: Users can activate perf debug in logs when have few FPS
- **Audio**: Footsteps and dropped crates now sound like the surface they are on — metal, sand, stone, concrete — instead of one sample everywhere. Crates are heard when lifted and when they land.

### Changed

- **Player**: Players are now represented by a proper character model instead of the placeholder mannequin, with all existing animations preserved. The flashlight is attached to the head, so its beam follows the body.
- **Player**: Vaulting and climbing now happen when you PRESS JUMP in front of an obstacle, instead of on their own as you walk into one. Stairs and low steps are still walked up automatically.
- **Vehicles**: You can no longer board a vehicle with your hands full, and boarding puts your tools away.
- **PlanetTech**: Sandbox is now the third world of the Tarsis system, closer to its star and shielded by its corundum veil; Gaea takes the fourth orbit. Sandbox and its moons Korax and Xarok are renamed accordingly.
- **Graphics**: The sky is now computed from each world's real atmosphere — its gases, its pressure, its dust —
  instead of a painted gradient. Sunsets, the colour of distance and the haze on far mountains all
  follow from the same physics, and change from one planet to the next. Two bugs that lit the world
  at night, making buildings and distant peaks look backlit after dark, are fixed.

### Fixed

- **PlanetTech**: Fix bridges
  disable spawn by player
  modify possibility of spawn rocks on chunk from 70% to 90%
- **PlanetTech**: Fixed cliff detection on planet surfaces: steep faces are now correctly identified everywhere, instead of the whole star-facing hemisphere being rendered as cliff and genuine vertical faces being missed.
- **Star map**: The system chart (F2) and the debug readouts now work while seated in a vehicle, and the chart is properly modal: nothing else reacts while it is up, and the truck coasts instead of keeping your last throttle.
- **Controls**: Alt+L and Alt+I no longer switch the head lights and the engine on and off along with their debug tool.
- **Audio**: The SFX volume slider now affects every sound in the game, and a sound's own volume setting works even when it comes from your own hands or feet.
- **Vehicles**: A truck left with a door open no longer ejects you when you try to sit in it.
- **Server**: Fixed the game server sometimes starting with no world at all, which left players unable to move.
- **Server**: Fix rotation and player exit zone (gorc)

## [0.1.0-dev.202608232359] - 2026-08-23

### Added

- **Star map**: The planets and moons of the Tarsis system travel their real orbits, and a new system chart on F2 shows where everything is — including you.
- **Graphics**: Nights have a starry sky, and dusk now lasts, fading over the point where the star set.
- **PlanetTech**: Addition of kilometer markers (placed by hand, so it's approximate)

### Changed

- **Performance**: Limit threads for server to enhance performances on the kubernetes
- **Server**: Update server godot version to 4.7, missed to use 4.7 like the client ;(

### Removed

- **Interface**: The developer spawn wheel, the prop cleanup tool and EVA free-flight are no longer available in game, and their shortcuts no longer appear in the control settings.

### Fixed

- **Interface**: Fix loading page indefinitely
- **Performance**: Server performance near cities is greatly improved, and players and vehicles no longer tremble on the spot.
- **Vehicles**: Trucks placed in the world now actually appear, instead of silently falling through the ground before anyone could see them.
- **Player**: Spawning no longer drops you through the floor of your habitation on the first connection after a server restart.
- **Interface**: 3D screens, like the mining depot's, can be used again: the pointer no longer trembles or snaps back to the middle of the screen, and buttons can be clicked anywhere on the surface.
- **Buildings**: Walking through a teleporter pad now shows up correctly for the other players.
- **Server**: Fix build and version of the build. Now it's same for linux and windows client (try fix launcher and update the game)

## [0.1.0-dev.202608162359] - 2026-08-16

### Added

- **Server**: Add NPC management
  Add propsync (network object)
- **Audio**: New sounds: the three vault types, the mining perforator (drilling loop, end, fail, equip/unequip), the player torch, and truck head lights / electric engine.

### Changed

- **Player**: Walking, sprinting and crouching now move at the speeds described in the design doc, and the mouse-wheel walk speed steps smoothly between 0.5 and 3 m/s instead of jumping around.
- **Social**: Chat: shown by default, clearer message order, and readable on bright backgrounds.
- **Interface**: The on-screen sound/microphone icons sit in the bottom-left corner and are smaller.

### Fixed

- **Interface**: Emote wheel (T) no longer spawns a prop when the spawn wheel (Alt+T) was used before.
- **Player**: Repeatedly jumping while sprinting no longer builds up unlimited speed; a jump now carries the momentum it took off with.
- **Player**: Character animation no longer flickers between walking and jogging when moving at a steady pace near a gait change.
- **Social**: Chat: holding TAB no longer cycles through interface buttons, and typing a message no longer triggers gameplay actions such as crouching or going prone.
- **Social**: Voice chat: muting your microphone actually stops transmitting, and your voice is no longer captured twice.
- **Social**: Voice chat: with several players around, every voice is heard, and a player who leaves stops being audible instead of lingering or being heard twice after rejoining.
- **Player**: Spawn: a "Spawning..." screen now holds until the world is ready, so you no longer see a daytime flash or the camera snapping straight right after spawning.

## [0.1.0-dev.202608092359] - 2026-08-09

### Added

- **Player**: Players now have an animated body: you see your own body in first person and other players are fully animated — walk/run/jump, crouch (C) and prone (W), in-place turn, sit/drive in vehicles, emotes (T wheel) and carrying. Carrying a box is only possible while standing, and holstered tools follow the body.

## [0.1.0-dev.202608022359] - 2026-08-02

### Added

- **Graphics**: The world is now lit and animated by the real star system: sunlight, day/night and
  sunrise/sunset colours follow the actual star, distant planets and moons are correctly lit
  even at astronomic range, the sky follows the star — in the main view AND in vehicle mirrors —
  and fades to space with altitude, and every body rotates on its axis at its real period. The
  HUD now also shows your longitude/latitude and the local time of the body you stand on. Adds
  free-flight and marker tools for inspecting the system.

## [0.1.0-dev.202607192359] - 2026-07-19

### Added

- **Graphics**: Added Graphics settings to toggle real-time shadows on/off and adjust the sun shadow draw distance (persisted, applied live).
- **Props**: New storage containers lock any crate that settles on their floor so it can't be knocked around — pick it back up to free it.
- **Audio**: Players have sound: footsteps (random samples, cadence following your speed), the torch switch and the jump. They are positional and replicated, so you hear the players around you walk, jump and light their torch.

### Changed

- **Server**: Update server URLs to the new infrastructure
- **Props**: Carried objects now feel much better: they don't snap to your hands on pickup — they ease in and trail as you move, react to bumps, and are solid immediately. Look down to set an object on the floor, or up to place it high.
- **Player**: The interaction reach is now a single configurable value on the player.
- **Props**: The dev spawn wheel is now server-authoritative: objects land in front of you, on the ground and upright, and the server decides where. The mouse wheel rotates a carried object by 15° notches, and holding the middle mouse button free-rotates it on all axes with the mouse — both about the object's centre.
- **Mining**: The mining depot is no longer spawnable and packs its ore into a hauling box.
- **Vehicles**: Vehicles steer and brake with the engine off, and the engine can be cut at any speed.
- **Interface**: In the settings menu, Esc now goes back instead of releasing the mouse.
- **PlanetTech**: Update planet tech. generate heightmap for each LOD, fix teleport to another planet / point.
- **Server**: On network, planets are now generic objects.

### Fixed

- **Social**: Fix text chat (connection to the server)
- **Performance**: Fixed a physics CPU spike on server start-up: props reloaded from persistence no longer all re-run collision at once — they reload frozen and wake up when a player approaches.
- **Props**: A carried object no longer shoves you around, and looking up inside a container no longer flings it onto the roof.
- **Player**: Using a 3D screen no longer strands your camera in space.
- **Vehicles**: A crate that falls or is thrown into a truck bed is now weighed like a hand-loaded one.
- **Props**: You can no longer grab an object or open a vehicle door through a building wall.
- **Vehicles**: Plus brighter truck headlights and a class of client crashes fixed.

## [0.1.0-dev.202607122359] - 2026-07-12

### Added

- **Audio**: Vehicles have sound: doors, engine start/stop, an engine note that rises with the revs, a horn (H) and a special horn (Alt+H), hand brake and head lights. The engine must now be started with the ignition key (I) while standing still before the vehicle will drive.
- **Interface**: Changing the screen resolution now asks you to confirm within 10 seconds and reverts automatically otherwise, so a too-large resolution can't lock you out.
- **Interface**: You can now show/hide the on-screen debug panels from Settings → General, or with a rebindable key (default Alt+²) available in the Controls menu.
- **Props**: Test containers now have collision.

### Changed

- **Vehicles**: Updated the mini truck model (fixing the wheel spin axis and the cargo-bay weight zone).
- **Props**: Carried objects now physically collide with the world: you can bump and rest them against the ground, walls and vehicles, and stack them by looking up or down to raise/lower a held object. An object dragged out of reach (e.g. stuck behind a wall) is dropped automatically.
- **Interface**: The dev spawn wheel (T) is now a two-level menu (category → variant);
- **Props**: The pallet crates it spawns can be picked up and carried.
- **Performance**: Update physics to 60 FPS.
  fix per-chunk collision bodies for Jolt at astronomic coordinates
  fix terrain data export + cache validation + idle physics sleep

### Fixed

- **Interface**: The pause menu no longer closes when you click in the void — use Esc or the Resume button.
- **Vehicles**: Truck: the steering wheel now turns the right way at a sensible speed, and the reverse camera is no longer mirrored.
- **Vehicles**: Fixed truck doors that could refuse to open once a prop was spawned nearby, and carrying crates from a normal distance held items now float a bit further ahead.

## [0.1.0-dev.202607052359] - 2026-07-05

### Added

- **PlanetTech**: Update planet tech, add valleys, texture...
- **Props**: Editor-only: add a DyingStar tool to import/export a scene's server props to horizonserver's startup_items.json.

### Changed

- **PlanetTech**: Update export options for planets
- **Vehicles**: Vehicle steering now feels progressive and self-centring, with a speed-sensitive steering lock (sharper at low speed, more stable at high speed).

### Fixed

- **PlanetTech**: Fix planet folder && build
  add Bardok house for test
  add Kankan containers for test
- **Props**: You can no longer interact with something you can't actually see: picking up an object now requires a clear line of sight to it, and a vehicle door only opens from the handle on your side (outside on foot, inside when seated) when it isn't blocked.
- **Player**: Players who join now see the current state of everyone already in the world (torch on/off, equipped tool, carrying…), instead of only seeing it after the next change.
- **Vehicles**: Vehicle fixes: an empty vehicle no longer drives off on its own (it coasts to a stop), vehicles spawn with the hand brake on, a door left open is now visible to players who join later, and the truck's steering wheel turns correctly around its column.

## [0.1.0-dev.202606282359] - 2026-06-28

### Added

- **Vehicles**: Vehicles can now use a real 3D model: working wheels and steering wheel, openable doors with look-at handles, Blender-authored collision, and in-cab screens. A door must be opened (look at its handle + E) before you can get in or out.
- **Buildings**: Habs test - container

### Fixed

- **Buildings**: Fixed wrong LOD settings for the VIP hab that caused a visual glitch. The correct model is now displayed when being close to it.

## [0.1.0-dev.202606212359] - 2026-06-21

### Added

- **Mining**: Feat: mining zones generate rock fields server-side on player entry (seeded, renewable)
  feat: small / medium / large mineable rock variants
  feat: per-zone mineral replicated via `mineral_id` (gold / iron / cryptonite)
- **Graphics**: Add a 30-minute day/night cycle and a physical sky (with sunrise/sunset colours) to the sandbox.
- **Graphics**: Feat: FPS limit + field-of-view graphics settings (persisted)
- **Audio**: Feat: working audio settings (bus volumes, input/output device, mic test)
- **Player**: You can now see other players turn their flashlight on and off.
- **Vehicles**: Improve cargo: drop an item in a truck's bed (or over the side) to load it, drive it around, and tip the truck to spill it. Changed render of  rear-view mirrors / reversing camera screens.
- **Interface**: New "Dev mode" toggle in the Video settings: it ignores the saved resolution/fullscreen on launch (handy when running several game windows at once).
- **Vehicles**: Toggle your flashlight while seated in a vehicle (driver or passenger).
- **Vehicles**: Stand in a truck bed to add your weight to its load, and load a crate by dropping it in the bed; carrying a crate no longer flips a truck.
- **Social**: Add an in-game text chat: shown by default on the left, F12 to hide/show, Enter to write and send, Escape to cancel, Tab to switch channel.
- **Props**: Add food ration props (biscuit, nutrigris).
- **Interface**: Start screen: a Quit button. The mouse cursor shows when opening the pause menu. The debug overlay stays in the corner at any resolution.
- **Vehicles**: Vehicles can show a live rear-view camera and side mirrors on in-cab screens (reusable RearCamera drop-in; "mirror" flips it left/right). The truck ships with a reversing camera + two mirrors.
- **Vehicles**: Vehicle head lights: a dev just drops Light3D(s) into the "vehicle_light" group of their vehicle scene (no code); the driver toggles them with L. Shown on the HUD and the in-cab dashboard.
- **Vehicles**: The bed spills its whole load when the vehicle tips over.

### Changed

- **Server**: Upgrade the project to Godot 4.7
  enable HDR
- **Interface**: Your video settings (monitor, resolution, fullscreen, v-sync) are now kept between sessions.
- **Mining**: Mining rock pieces now weigh according to their size, and carrying one into a truck bed adds its weight to the load.
- **Controls**: All gameplay keys (vehicle reset/lights, brake & hand brake, the "Zapette" cleanup tool, the spawn wheel) are rebindable in Settings → Controls.
- **Controls**: E embarks a vehicle; Y leaves it. one spawn wheel on T.
- **Interface**: Pause menu reordered (Resume / Settings / Return to menu / Quit); Settings opens the full menu.
- **Controls**: L is contextual: head lights while driving, the player's flashlight on foot. The flashlight is now visible to other players and starts off.

### Fixed

- **Mining**: Fix bug when player go out its appartment
  Fix rock can't carry
  Network optimisation
  Add engine brake on vehicule
  Enhance loading screen when join the universe
- **Mining**: Fix designer-placed mining depots being duplicated in the database on every server restart.
- **Interface**: Fix: settings menu active-category highlight + title; V-Sync label fix: main-menu and ERROR 1337 layouts no longer shift on window resize fix: pause menu button SFX
- **Player**: Other players' name tags no longer jitter, and are hidden when too far away.
- **Vehicles**: Spamming the vehicle reset key no longer makes the truck fly off.
- **Props**: You can no longer pick up items through walls; the carry prompt only shows when the item is actually reachable.
- **Interface**: The settings menu works: Controls list, Fullscreen/Windowed, Screen Resolution auto-filled from your monitor, Monitor selection.
- **Vehicles**: A parked truck no longer creeps with the hand brake on (it freezes once stopped).

## [0.1.0-dev.202606142359] - 2026-06-14

### Added

- **Vehicles**: You can now retrieve a crate or rock you placed in a vehicle's bed.
- **Props**: "[E] Carry" / "[E] Drop" prompts when aiming at a grabbable object or holding one.
- **Vehicles**: New truck parking hand brake: long-press Space under 3 km/h, released by throttle, stays engaged when you leave the truck. Shown on the dashboard, HUD and shortcut hint.
- **Mining**: Mining rocks can hold different minerals (gold added); the ore look is data-driven per mineral.
- **Vehicles**: Add a drivable networked truck (driver and passenger seats, powertrain, in-cab dashboard, free look); the admin cleanup tool can now remove vehicles and depot crates.
- **Props**: Add admin cleanup tool: ray from the player's hand, red/yellow aim line, click to delete the targeted prop (rock / box / depot only).
  Server-authoritative delete: frees the node (or forwards to Horizon) -> removed from GORC + database. World infrastructure is protected.
  Tools 1 (perforator) and 2 (cleanup) are now mutually exclusive.
  Mining depot placeholder spawns its networked copy on the game server (collision + collect/SEND logic), with a deterministic uuid (optional stable_id) to avoid duplicate accumulation; placed in Sandbox Capital.
- **Interface**: Press F6 to record the game screen (for bug reports or clips); recordings are saved as AVI files in your Documents/DyingStar/records folder.
- **Mining**: Add a mining depot: deposit mined ore, refine it by volume (ore purity, stock and per-crate fill shown on the depot screen) and extract a carryable crate of ore.
- **Mining**: Mining rocks now show their ore: a few small traces on the surface, while the real amount is revealed by breaking the rock — richer pieces contain more ore.

### Changed

- **Vehicles**: Seated players now count toward the vehicle's load (OVERLOADED).
- **Props**: Carried objects are solid to the world and other players (but not to the carrier).
- **Vehicles**: Seated players now add their weight (75 kg) to the truck's load and total weight;
- **Vehicles**: OVERLOADED accounts for passengers + bed cargo.
- **Interface**: The vehicle UI is now in English.
- **Performance**: Collision calculation reduction by 50 times (tested on 200 boxes and rocks)
- **Vehicles**: Smooth networked vehicles and players (client interpolation), and let the admin cleanup tool remove vehicles and depot crates.

### Fixed

- **Vehicles**: Cargo placed in a bed no longer disappears in multiplayer.
- **Vehicles**: A vehicle can no longer be loaded into another vehicle's bed.
- **Vehicles**: A vehicle seat is freed when its occupant disconnects.
- **Vehicles**: Smoother ride: no more camera jitter once seated, and the truck moves smoothly for everyone (driver included).
- **Vehicles**: "Driver seat taken" message when the driver seat is occupied; the enter-seat prompt no longer shows while already seated. You now exit beside the seat you used.
- **Vehicles**: Cargo no longer disappears when dropped into the bed in multiplayer.
- **Props**: Fix carried props (boxes, ore) despawning for other players over distance.
- **Props**: Fix the admin cleanup tool leaving ghost collisions after deleting a prop.
- **Mining**: Unify how player and prop properties replicate to nearby players, and fix mining rocks sometimes appearing at the world origin.

## [0.1.0-dev.202606072359] - 2026-06-07

### Added

- **Mining**: Press **E** to **pick up / drop** a mined ore (one at a time).
- **Mining**: Mining V0: equip a perforator, aim at a rock's predefined faults and drill to break it into pieces, visible and synchronized in multiplayer
- **Interface**: Add button in pause UI to return to menu (disconnect from the server)
- **PlanetTech**: Add planet data download for build and get locally for developers

### Changed

- **Mining**: Only a **fully mined** ore (no fault left) can be carried; you can't take one already carried by someone else.
- **Mining**: Carrying **slows you down**, the ore **floats in front of you** (no collision), and **everything is visible to other players**.
- **Mining**: The **perforator** is always present: **stowed** by default / while carrying, **out** when equipped.
- **Mining**: See https://github.com/DyingStar-game/DyingStar/pull/186
- **Server**: Enhance server error messages
- **Server**: Update to dotnet 9, remove login page (auth with JWT token)
- **Audio**: Remove Wwise, replaced by audio directly in Godot
- **Interface**: Review UI interface and settings: sound, livekit (vocal proximity)

### Removed

- **Player**: Also removes the F4 third-person camera, which conflicts with the aim-based mining

### Fixed

- **Player**: Fix pseudo on player and parent when changing parent (server and client fix)
- **Buildings**: Fix spawn in apartments
- **Server**: Fix crash on built game (wrong dotnet version)
- **Server**: Fix delete player on disconnect

## [0.1.0-dev.202605312359] - 2026-05-31

### Added

- **Buildings**: Manage apartments spawn

### Fixed

- **Graphics**: Fix light of the universe
- **Server**: Fix godot server (many errors)

## [0.1.0-dev.202605102359] - 2026-05-10

### Added

- **Server**: Add build game in GitHub Actions
- **PlanetTech**: Planet tech v1

### Changed

- **Server**: Install dotnet runtime in docker server
- **Server**: Rewrite code for player out of server zone
- **Server**: Update to Godot 4.6.1
- **Server**: Update docker for build server
- **Server**: New tree architecture

### Fixed

- **Server**: Fix log in /tmp (crash on Windows)
- **Server**: Fix SSH deploy
- **Server**: Fix build and deploy
- **Server**: Fix Wwise for dedicated server

## [0.0.1-test5] - 2025-12-16

- Version for the test5
