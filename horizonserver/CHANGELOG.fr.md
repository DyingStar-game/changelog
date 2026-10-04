# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]
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
- Optimisation des relations parent-enfant par l'ajout d'un index
  Correction du problème de déconnexion du joueur (dans certains cas, les événements continuaient d'être envoyés à personne).
- Les composants de véhicule (moteurs, et plus tard batteries et réservoirs) sont répliqués et persistés : quelle baie contient quelle pièce est désormais transmis à tous les clients.
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
- Correction du problème de gorc lorsque le joueur est dans un véhicule
- Mise à jour de la position/rotation de départ
  augmentation server meshing dynamic (50 joueurs)
- Les véhicules peuvent désormais montrer leur suspension bouger aux autres joueurs.
- Suppression des rochers statiques au démarrage et mise à jour de leurs propriétés.
- L'etoile du systeme n'est plus perdue au chargement d'un monde.
- Fix/player network
- Fix player connection
- Le patch Horizon a été remplacé par un sous-module DyingStar-game/Horizon
- Correction d'un plantage qui pouvait faire tomber le serveur à chaque connexion d'un joueur, laissant les clients sur un écran gris avec l'erreur 1337.
- Mise à jour des objets qui apparaissent, car ils se trouvent désormais directement sur la planète.
- Réplique la posture du joueur (accroupi/allongé) et le yaw du regard assis, ainsi que l'occupation des sièges de véhicule, pour que les autres joueurs les voient.
- Correction de la déconnexion du joueur
  Correction du pont en cas de nombreux événements (persistances)
- L'état du moteur et des klaxons d'un véhicule est désormais répliqué : tous les joueurs autour d'un camion l'entendent démarrer, tourner au ralenti, monter en régime et klaxonner.
- Feat : répliquer `mineral_id` sur miningrock
  Modification : distance GORC de miningrock 30 → 150 m
- Replication de l'action attraper gérée par le serveur du serveur sur les clients.
- Correction du problème de reparent de l'objet. Le calcul de position était incorrect, l'élément est donc trop éloigné et n'est pas mis à jour côté client (grâce à gorc qui fonctionne parfaitement :D).
- Correction du stockage persistant des attributions d'appartements (ce n'était pas le cas, c'est pourquoi nous les perdons lors du redémarrage d'Horizon).
- Lorsqu'un joueur se déconnecte, la fonction remove_player le désabonne de tous ses abonnements, mais ne le supprime pas de la base de données interne de gorc. Nous le supprimons désormais. Correction du joueur déconnecté visible pour les nouveaux joueurs connectés
- Ajout de la définition de réplication des propriétés du véhicule (canal d'état + canal de suppression).
  Ajout de la définition de réplication des propriétés du véhicule (état, canal de suppression et vitesse).
- Correction du minerai visible sur les faces de coupe d'une roche fracturée afin qu'il reste cohérent pour tous les clients.
