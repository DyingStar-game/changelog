# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]
- Lorsqu'un joueur se déconnecte, la fonction remove_player le désabonne de tous ses abonnements, mais ne le supprime pas de la base de données interne de gorc. Nous le supprimons désormais. Correction du joueur déconnecté visible pour les nouveaux joueurs connectés
- Ajout de la définition de réplication des propriétés du véhicule (canal d'état + canal de suppression).
  Ajout de la définition de réplication des propriétés du véhicule (état, canal de suppression et vitesse).
- Correction du minerai visible sur les faces de coupe d'une roche fracturée afin qu'il reste cohérent pour tous les clients.
