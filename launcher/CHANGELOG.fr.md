# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

- Ajout d'un bouton d'affichage plein écran (et réduit).
  Ajout d'un menu burger quand le launcher est petit (ce qui permettra de mettre le launcher un peu plus petit pour ceux qui veulent même si pour le moment tout n'est pas mis dans le burger).
  Ajout de la détection du lancement du jeu pour bloquer le bouton de lancement dès que l'on clique dessus.
  Ajout de la détection de lecture de changelog ce qui devrait résoudre le soucis des pastilles après chaque release.
## [0.3.1] - 2026-06-11

- Correctif sur les sons du launcher qui se jouaient lorsque le jeu est lancé.
## [0.3.0] - 2026-06-10

- Changelog distant : chargement depuis un JSON centralisé, page dédiée avec filtrage par environnement (Testing / Universe) et badges lu/non lu.
  Sons UI : musique de fond, SFX hover/clic, contrôle volume/mute dans la navbar.
  Auth OAuth intégrée : connexion Discord/Keycloak dans une fenêtre du launcher (plus besoin du navigateur système), avec bascule vers l’app Discord via discord://.
  FilesPanel : message « Sélectionnez un répertoire d’installation » quand aucun dossier n’est défini.
  Linux (AppImage) : désactivation GPU / décodage vidéo accéléré au démarrage (plus besoin de --disable-accelerated-video-decode).
  Ancien changelog local dans FilesPanel (CHANGELOG.md, modal associée).
## [0.2.2] - 2026-05-27

- correction du nombre de joueur sur le panel game
- correction expiration authentification
- correction de la mise a jour d'une nouvelle version du jeu

## [0.2.1] - 2026-05-17

- taille du launcher, dans certains cas ça s'agrandi tout seul au démarrage
- lien pour télécharger la nouvelle version du launcher

## [0.2.0] - 2026-05-16

- Documentation contributeur bilingue dans `docs/en/` et `docs/fr/` (onboarding, contribution, sécurité, code de conduite)
- Libellés de progression d'installation structurés et i18n UI (`installProgress.*`)
- Détection de la langue navigateur et persistance (`ds-language`)
- github actions pour build le launcher
- Gestionnaire de paquets **pnpm** uniquement (suppression de `package-lock.json`)
- Dialogue natif de dossier d'installation localisé (fr/en) côté main
- Mock `addFriend` : validation des doublons et erreurs typées
- Stub IPC inutilisé `game:get-state` supprimé

## [0.1.0] - 2025-01-01

- Premier launcher Electron open source : auth, install/mise à jour jeu, statut serveur, lore, UI social (mock)
