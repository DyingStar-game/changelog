# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

## [1.1.0] - 2026-10-26

### Added

- **Compte** : Connexion affichée comme indisponible quand le serveur de connexion est en panne, au lieu d'un bouton de connexion qui échoue.
- **Changelog** : Bouton « Tout marquer comme lu ».
- **Téléchargement et installation** : Le launcher se met à jour tout seul : la nouvelle version se télécharge en arrière-plan et s'installe au redémarrage, ou à la fermeture du launcher.
- **Interface** : La version du launcher est affichée à côté du logo.
- **Téléchargement et installation** : La sortie du jeu est conservée dans un fichier de log à côté de celui du launcher, pour aider à comprendre un plantage.

### Changed

- **Interface** : Le lien Discord ouvre l'application Discord quand elle est installée, directement sur le serveur pour ses membres ; sinon la page web.
- **Social** : Statut des amis rafraîchi toutes les minutes.
- **Interface** : Launcher réduit pendant que le jeu tourne, de retour à sa fermeture.
- **Changelog** : Noms des builds raccourcis, versions non lues signalées par un point ; le changelog s'ouvre sur la version la plus récente.
- **Interface** : Boutons désactivés affichés avec un curseur d'interdiction et, quand la raison n'est pas visible, une infobulle qui l'explique.
- **Téléchargement et installation** : Les launchers installés depuis un paquet .deb ou .rpm téléchargent directement le nouveau paquet.

### Fixed

- **Téléchargement et installation** : Disque plein signalé clairement, avec la place à libérer, au lieu d'un téléchargement interrompu ; le téléchargement est conservé pour reprendre.
- **Interface** : Serveur plus affiché comme indisponible après des changements d'univers rapides.
- **Compte** : Connexion avec Discord de retour dans le navigateur, où Discord connaît déjà le compte, au lieu d'une fenêtre du launcher qui le redemande.
- **Téléchargement et installation** : Le jeu ne plante plus quand il est lancé depuis le launcher AppImage.
- **Interface** : Le statut des serveurs revient tout seul au retour de la connexion, sans relancer le launcher.

### Security

- **Téléchargement et installation** : Une archive du jeu ne peut plus écrire de fichiers hors du dossier du jeu.
- **Interface** : Composants du launcher mis à jour pour corriger des failles de sécurité connues.

## [1.0.1] - 2026-10-14

### Changed

- **Changelog** : Sur Universe Testing, les changements sont listés build par build, regroupés par la version qu'ils préparent.
- **Changelog** : Sur Universe, les builds de développement d'une version sont repliés sous elle, et la version montre tous leurs changements.
- **Téléchargement et installation** : Jouer vérifie la présence d'une nouvelle version du jeu avant de lancer le jeu.
- **Changelog** : Les entrées du changelog sont regroupées par type et indiquent le domaine concerné (véhicules, interface…).
- **Changelog** : Une version retirée est signalée comme telle.

### Fixed

- **Téléchargement et installation** : Une mise à jour du jeu publiée pendant que le launcher est ouvert est désormais proposée sans redémarrage.
- **Téléchargement et installation** : Un téléchargement bloqué sur une connexion lente reprend désormais de lui-même.
- **Téléchargement et installation** : Un téléchargement coupé par la connexion reprend désormais de lui-même ; s'il ne le peut pas, un message le signale.
- **Interface** : Une partie du launcher qui ne s'affiche pas ne laisse plus toute la fenêtre noire.

## [1.0.0] - 2026-10-13

- Modification du profil ajoutée : faction, biographie et fiche RP.
- Gestion des organisations ajoutée : infos, invitations, membres, grades et direction ; possibilité de quitter une organisation ; invitation d'un joueur depuis son profil.
- Page Social séparée en Amis et Organisations, chacune avec sa liste, une recherche et les demandes en attente.
- En-tête séparé en deux barres : le launcher en haut, l'univers en cours en dessous (Accueil, Social, Changelog et compte).
- Connexion déplacée en haut à droite ; hors connexion, le bouton Jouer est remplacé par « Se connecter avec Discord ».
- Compteurs ajoutés pour les demandes d'ami en attente et les versions du changelog non lues.
- Environnement de test signalé sur toutes les pages ; le launcher s'ouvre désormais dessus.
- Page Lore supprimée.
- Grésillements des sons de l'interface corrigés.
- Page d'accueil repensée : l'univers sur un diaporama d'images plein écran, et une seule barre en bas avec l'état du serveur, l'état du jeu et son action principale (installer, mettre à jour, se connecter, jouer).
- Téléchargement du jeu : pause, reprise (même après avoir fermé le launcher) et annulation ; vitesse et temps restant affichés.
- Fichiers du jeu (version, répertoire d'installation, cache) déplacés derrière un bouton ⚙ à côté de l'action principale.
- Une mise à jour du jeu disponible affiche la version installée et la nouvelle, avec un lien vers son changelog.
- Amis de l'accueil listés par ordre alphabétique, tous.
- Notifications (profil enregistré, organisation créée, cache vidé…) affichées dans un coin de l'écran.
- La déconnexion n'ouvre plus de page dans le navigateur ; la connexion suivante redemande le compte.
- Liste d'amis vidée à la déconnexion.
- Captures d'écran et vidéos du dossier du jeu conservées lors d'une mise à jour.
## [0.4.0] - 2026-10-10

- Social : amis, demandes d'ami et organisations passent par le service social du jeu, avec une recherche de joueurs
  Pages joueur et organisation, ouvertes en cliquant sur un joueur ou une organisation ; Retour ramène là où on était
  Correction de la fenêtre du launcher qui ne s'affichait pas sous Linux en session Wayland (seul le son était présent)
  L'en-tête s'adapte aux fenêtres étroites : les sections et le choix d'univers passent dans le menu
  Les statuts (membre, ami, demande envoyée…) ne ressemblent plus à des boutons ; tous les boutons affichent le curseur main
  Nouveau menu des langues dans l'en-tête, et infobulles sur les boutons de l'en-tête
  Les menus et le réglage du volume sont utilisables au clavier
  Les pages et les listes affichent un aperçu de leur contenu pendant le chargement
## [0.3.2] - 2026-09-23

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

[non publié]: https://github.com/DyingStar-game/launcher/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/DyingStar-game/launcher/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/DyingStar-game/launcher/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/DyingStar-game/launcher/compare/v0.4.0...v1.0.0
[0.4.0]: https://github.com/DyingStar-game/launcher/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/DyingStar-game/launcher/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/DyingStar-game/launcher/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/DyingStar-game/launcher/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/DyingStar-game/launcher/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/DyingStar-game/launcher/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/DyingStar-game/launcher/compare/0.1.0...v0.2.0
[0.1.0]: https://github.com/DyingStar-game/launcher/releases/tag/0.1.0
