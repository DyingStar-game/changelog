# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]
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
