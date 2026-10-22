# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Added

- **Connexion** : Un joueur peut demander que les serveurs horodatent ses propres déplacements, pour savoir d'où vient une saccade.

### Changed

- **Performances** : Votre propre position vous parvient deux fois plus souvent : les virages, les arrêts et les chocs contre un mur sont corrigés plus tôt.

## [0.1.0-dev.202610211613] - 2026-10-21

### Added

- **Connexion** : Au démarrage des serveurs, les joueurs qui arrivent attendent dans la file que les premiers villages soient prêts au lieu d'arriver tous dans le même.
- **Persistance** : Les portes, les tiroirs et les lampes d'un logement restent comme leur occupant les a laissés.

### Changed

- **Connexion** : Un village accueille 50 joueurs : les nouveaux venus attendent dans la file plutôt que de s'entasser dans un village plein tant qu'une place peut encore se libérer.
- **Maillage de serveurs** : Les serveurs sont découpés plus tôt et autour des villages : un village et ses joueurs restent sur un seul serveur.

### Fixed

- **Connexion** : Les joueurs qui reçoivent un appartement près d'une frontière entre serveurs ne restent plus bloqués sans jamais apparaître dans le monde.
- **Connexion** : Les joueurs n'attendent plus indéfiniment sur un serveur qui avait redémarré pendant que le jeu continuait à lui envoyer des joueurs.
- **Performances** : Les serveurs ne ralentissent plus quand beaucoup de villages sont créés en même temps.

## [0.1.0-dev.202610202031] - 2026-10-20

### Changed

- **Connexion** : Quand tous les serveurs sont pleins, les joueurs en attente reçoivent le message « All servers are full » au lieu d'attendre sans fin.

### Fixed

- **Connexion** : Les nouveaux joueurs sont répartis dans les villages qui ont encore de la place au lieu de s'entasser dans un seul village bien au-delà de sa taille.

## [0.1.0-dev.202610201807] - 2026-10-20

### Changed

- **Maillage de serveurs** : Un serveur bondé est désormais réparti sur plusieurs serveurs d'un coup au lieu d'être coupé en deux encore et encore.
- **Maillage de serveurs** : Un serveur ralenti par une zone très animée est désormais divisé même s'il a peu de joueurs, pour que le jeu y reste fluide.

### Fixed

- **Connexion** : Les joueurs en attente n'arrivent plus sur un serveur plein au bout de deux minutes : ils attendent qu'il ait de la place.

## [0.1.0-dev.202610201512] - 2026-10-20

### Added

- **Connexion** : Quand les serveurs sont pleins, les joueurs attendent dans une file et voient leur place, au lieu de surcharger un serveur.
- **Persistance** : Votre position est sauvegardée quand vous quittez le jeu et régulièrement pendant que vous jouez.

### Changed

- **Connexion** : En revenant dans le jeu, vous vous réveillez toujours dans votre appartement.
- **Performances** : Les joueurs qui arrivent en masse entrent quelques-uns à la fois, pour que le serveur reste fluide.
- **Performances** : Le serveur écrit beaucoup moins de journaux quand de nombreux joueurs sont connectés : les problèmes rencontrés pendant les grands tests sont plus faciles à retrouver.

## [0.1.0-dev.202610192044] - 2026-10-19

### Fixed

- **Maillage de serveurs** : Les nouveaux joueurs sont répartis équitablement entre les serveurs au lieu d'aller tous sur le plus chargé.
- **Maillage de serveurs** : Les nouveaux joueurs n'apparaissent plus à l'origine du monde quand chaque village compte 50 joueurs : les villages en accueillent davantage tant que leurs bâtiments ont des appartements libres.
- **Maillage de serveurs** : Un serveur de jeu qui a perdu sa connexion à Horizon ne refuse plus définitivement les nouveaux joueurs.
- **Maillage de serveurs** : Quand une foule part et que les serveurs fusionnent, les joueurs restants ne se déplacent plus par à-coups et ne passent plus à travers le sol.
- **Performances** : Le serveur ne ralentit plus quand des centaines de joueurs arrivent en même temps et attendent leur appartement.
- **Performances** : Le serveur rend la mémoire inutilisée au lieu de grossir après chaque afflux de joueurs.
- **Connexion** : Un joueur qui a perdu le réseau peut revenir en jeu tout de suite, au lieu d'échouer au chargement pendant jusqu'à une heure.

## [0.1.0-dev.202610161302] - 2026-10-16

- ajout d'un ascenseur route du village M0001 vers la factory, à gauche avant le premier pont. Plusieurs au village M0059
  fix sortie habitation -> espace
- spawn des étagères dans l'entrepôt

## [0.1.0-dev.202610112359] - 2026-10-11

- Douze villes-usines apparaissent sur Tarsis 3.
- La station orbitale retrouve sa cabine de téléportation.
- fix(mesh) : les zones d'un serveur qui meurt vont à un serveur libre
  Avant, les zones d'un serveur perdu restaient sans serveur si d'autres tournaient encore, et leurs joueurs étaient orphelins. Elles sont maintenant gardées, puis données au prochain serveur libre. Si plus aucun serveur ne tourne, on revient au découpage initial, comme avant.
  fix(mesh) : les actions tenues du joueur sont rejouées sur son nouveau serveur
  Horizon retient la dernière valeur de chaque action maintenue : conduite, sprint, poussée et stabilisation en apesanteur, vitesse de marche. Il les rejoue juste après l'arrivée ou le réveil du joueur sur le nouveau serveur : le camion ne s'arrête plus net et le sprint tient.
- Le régime du camion suit ses roues : plus de moteur qui hurle en chute ou en saut.
  Relâcher une touche de déplacement n'est plus parfois ignoré par le serveur.

## [0.1.0-dev.202610042359] - 2026-10-04

- nouveau système lors de la création d'un nouveau serveur (maillage de serveurs dynamique) et transfert des objets et des joueurs vers ce nouveau serveur
- Gel ordonné : après un split, l'ancien serveur gèle d'abord les joueurs, puis les véhicules occupés, puis le reste des ~20 000 objets. Le joueur transféré n'est plus simulé 3 s par deux serveurs, ce qui supprime le saut en arrière du camion et le freeze.
  Photo fraîche réduite : après le préchauffage, horizon ne redemande à genericprops que les joueurs et leurs véhicules, au lieu de tout le monde (~2,5 s). Ils arrivent sur le nouveau serveur avec leur position actuelle au lieu de 2 à 3 s de retard.
  Mesure : chaque split écrit une ligne [mesh] freeze coverage, qui compte les objets cédés absents de la liste du serveur. On saura ainsi si on peut ne geler que ce qu'il simule.
- [server meshing dynamic] changement de la façon de spliter le tout premier server : split sur 2 nouveaux serveurs pré-chauffés au lieu de tout envoyer sur un nouveau serveur
- Au démarrage, plus de bâtiments, seulement les villages ; M0001 est demandé d'office. Un nouveau joueur attend ses habs jusqu'à 40 s, sinon il reçoit Server not ready et est déconnecté. Ajoute aussi les définitions des nouveaux props (simple_building, ascenseurs à véhicules).
  Les nouveaux joueurs sont placés sur le serveur Godot le moins chargé, et non plus village après village.
  Le pool de serveurs Godot ne s'effondre plus quand certains se figent sous la charge. Ajoute aussi un état [mesh] loggué toutes les 5 s et des scripts pour analyser les tests de charge.
- un seul serveur par joueur, donc plus de doublons ni de total à 6 372.
- changement de fonctionnement sur le nombre de place d'habitations disponible pour gérer la charge de joueurs d'un coup
- Seed des villages : les 4 POI « mining village » de l'export QGIS de tarsis_3 sont ajoutés dans startup_items.json, avec un uuid fixe et une position calculée depuis leur lat/lon. mining_village_01 est déjà marqué spawné, ses habs étant les 23 spawnbuildings existants.
  Lien bâtiment → village : la nouvelle propriété poi_uuid rattache chaque spawnbuilding à son village (parent_id reste informatif). Le village reçoit aussi une propriété spawn_requested.
  Attribution des appartements : un nouveau joueur va dans le village le plus rempli encore sous le plafond (50, configurable via max_players_per_village). Le plafond est strict pour un joueur seul. Le dépassement est prévu pour le futur matchmaking (amis / groupe) via AssignRequest, mais pas encore actif.
  Spawn à la demande : à 80 % du plafond (village_prespawn_ratio), si aucun autre village n'a de place, Horizon passe spawn_requested sur le village non spawné le plus proche, un seul à la fois. Seul le serveur Godot qui possède sa zone reçoit la demande et crée les habs.
- serverinfo relaie scenes_number_actives aux clients.

## [0.1.0-dev.202609272359] - 2026-09-27

- Optimisation des relations parent-enfant par l'ajout d'un index
  Correction du problème de déconnexion du joueur (dans certains cas, les événements continuaient d'être envoyés à personne).
- Les composants de véhicule (moteurs, et plus tard batteries et réservoirs) sont répliqués et persistés : quelle baie contient quelle pièce est désormais transmis à tous les clients.

## [0.1.0-dev.202609202359] - 2026-09-20

- Augmentation de la limite de joueurs par serveur de 30 à 75
  Correction d'un problème de déplacement et de changement de parenté (manqué dans certains cas à cause du LOD)
  Envoi de la vélocité lors du transfert d'un joueur vers un autre joueur
- Désactivation l'audio pour les PNJ
  Résolution de la liste du pool de serveurs Godot via DNS lors de l'exécution plutôt qu'au démarrage du pod
  Ajouter du LOD pour les déplacements du joueur
  logs la transmission du LOD pour le débogage
- Gérer la fréquence par zone + gérer des fréquences différentes selon la distance au sein d'une même zone.
- Mise à jour du système de server meshing dynamic avec le nouveau système world dans le serveur Godot.
- Déplacement du fichier plugin.toml (configuration des plugins) dans l'image Docker horizon-data.

## [0.1.0-dev.202609132359] - 2026-09-13

- Correction du problème de gorc lorsque le joueur est dans un véhicule
- Mise à jour de la position/rotation de départ
  augmentation server meshing dynamic (50 joueurs)
- Les véhicules peuvent désormais montrer leur suspension bouger aux autres joueurs.

## [0.1.0-dev.202609062359] - 2026-09-06

- Suppression des rochers statiques au démarrage et mise à jour de leurs propriétés.
- L'etoile du systeme n'est plus perdue au chargement d'un monde.
- Fix/player network

## [0.1.0-dev.202608302359] - 2026-08-30

- Fix player connection
- Le patch Horizon a été remplacé par un sous-module DyingStar-game/Horizon

## [0.1.0-dev.202608232359] - 2026-08-23

- Correction d'un plantage qui pouvait faire tomber le serveur à chaque connexion d'un joueur, laissant les clients sur un écran gris avec l'erreur 1337.
- Mise à jour des objets qui apparaissent, car ils se trouvent désormais directement sur la planète.

## [0.1.0-dev.202608092359] - 2026-08-09

- Réplique la posture du joueur (accroupi/allongé) et le yaw du regard assis, ainsi que l'occupation des sièges de véhicule, pour que les autres joueurs les voient.

## [0.1.0-dev.202607192359] - 2026-07-19

- Correction de la déconnexion du joueur
  Correction du pont en cas de nombreux événements (persistances)

## [0.1.0-dev.202607122359] - 2026-07-12

- L'état du moteur et des klaxons d'un véhicule est désormais répliqué : tous les joueurs autour d'un camion l'entendent démarrer, tourner au ralenti, monter en régime et klaxonner.

## [0.1.0-dev.202606212359] - 2026-06-21

- Feat : répliquer `mineral_id` sur miningrock
  Modification : distance GORC de miningrock 30 → 150 m
- Replication de l'action attraper gérée par le serveur du serveur sur les clients.

## [0.1.0-dev.202606142359] - 2026-06-14

- Correction du problème de reparent de l'objet. Le calcul de position était incorrect, l'élément est donc trop éloigné et n'est pas mis à jour côté client (grâce à gorc qui fonctionne parfaitement :D).
- Correction du stockage persistant des attributions d'appartements (ce n'était pas le cas, c'est pourquoi nous les perdons lors du redémarrage d'Horizon).
- Lorsqu'un joueur se déconnecte, la fonction remove_player le désabonne de tous ses abonnements, mais ne le supprime pas de la base de données interne de gorc. Nous le supprimons désormais. Correction du joueur déconnecté visible pour les nouveaux joueurs connectés
- Ajout de la définition de réplication des propriétés du véhicule (canal d'état + canal de suppression).
  Ajout de la définition de réplication des propriétés du véhicule (état, canal de suppression et vitesse).
- Correction du minerai visible sur les faces de coupe d'une roche fracturée afin qu'il reste cohérent pour tous les clients.
