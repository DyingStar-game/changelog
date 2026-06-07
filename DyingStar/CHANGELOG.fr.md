# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

- Extraction minière V0 : équipez-vous d'un perforateur, visez les failles prédéfinies d'une roche et forez pour la briser en morceaux, visible et synchronisé en multijoueur
  Supprime également la caméra à la troisième personne (F4) qui entrait en conflit avec l'extraction minière basée sur la visée
  Voir https://github.com/DyingStar-game/DyingStar/pull/186
- Ajout d'un bouton dans l'UI de pause pour retourner au menu (déconnexion du serveur)
- Correction du pseudo sur le joueur et le parent lors du changement de parent (correctif serveur et client)
- Correction du spawn dans les appartements
- Correction de la lumière de l'univers
- Correction du serveur Godot (nombreuses erreurs)
- Gestion du spawn dans les appartements
- Amélioration des messages d'erreur du serveur
- Correction du crash sur le jeu compilé (mauvaise version dotnet)
- Mise à jour vers dotnet 9, suppression de la page de connexion (auth par JWT)
- Correction des logs dans /tmp (crash sur Windows)
- Correction du déploiement SSH
- Correction du build et du déploiement
- Ajout du build du jeu dans GitHub Actions
- Suppression de Wwise, remplacé par l'audio natif Godot
- Révision de l'interface et des paramètres : son, livekit (proximité vocale)
- Correction de la suppression du joueur à la déconnexion
- Correction de Wwise pour le serveur dédié
- Installation du runtime dotnet dans le docker serveur
- Réécriture du code pour les joueurs hors zone serveur
  Planet tech v1
  Mise à jour Godot 4.6.1
  Mise à jour du docker pour le build serveur
  Nouvelle architecture
  Ajout du téléchargement des données planète pour le build et en local pour les développeurs

## [0.0.1-test5] - 2025-12-16

- Version pour le test5
