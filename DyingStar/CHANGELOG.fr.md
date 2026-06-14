# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

- Nouveau frein à main du camion : appui long sur Espace sous 3 km/h, relâché par
  l'accélération, reste actif quand on sort. Affiché sur le tableau de bord, le HUD et l'aide.
  Les passagers assis ajoutent leur poids (75 kg) à la charge et au poids total ;
  SURCHARGE prend en compte passagers + chargement de la benne.
  Conduite plus fluide : plus de tremblement de caméra une fois assis, et le camion
  bouge de façon lisse pour tout le monde (conducteur compris).
  Message « Driver seat taken » quand le siège conducteur est occupé ; l'invite pour
  monter ne s'affiche plus quand on est déjà assis. On ressort à côté du siège utilisé.
  Correction : le chargement ne disparaît plus quand on le pose dans la benne en multijoueur.
  L'interface du véhicule est désormais en anglais.
- Les rochers minables peuvent contenir différents minéraux (or ajouté) ; l'aspect du minerai est piloté par des données.
- Réduction du calcul de collision de 50 fois (testé sur 200 boites et rochers)
- Ajout d'un camion réseau pilotable (sièges conducteur et passager, groupe motopropulseur, tableau de bord, vue libre) ; l'outil de nettoyage d'administration peut désormais supprimer les véhicules et les caisses de dépôt.
  Fluidification des véhicules et des joueurs en réseau (interpolation côté client), et possibilité pour l'outil de nettoyage d'administration de supprimer les véhicules et les caisses de dépôt.
- Correction du problème de disparition des objets transportés (caisses, minerai) pour les autres joueurs au fil de la distance.
- Corrige le problème des collisions fantômes laissées par l'outil de nettoyage d'administration après la suppression d'un élément.
- Ajout d'un outil de nettoyage pour les administrateurs : un rayon partant de la main du joueur, une ligne de visée rouge/jaune, cliquez pour supprimer l'élément ciblé (rocher/boîte/dépôt uniquement).
  Suppression autorisée par le serveur : libère le nœud (ou le transfère à Horizon) -> supprimé de GORC et de la base de données. L'infrastructure du monde est protégée.
  Les outils 1 (perforateur) et 2 (nettoyage) sont désormais incompatibles.
  L'emplacement réservé au dépôt minier génère sa copie réseau sur le serveur de jeu (logique de collision et de collecte/envoi), avec un UUID déterministe (optionnel :
  stable_id) pour éviter l'accumulation de doublons ; placé dans Sandbox Capital.
- Unify how player and prop properties replicate to nearby players, and fix mining rocks sometimes appearing at the world origin.
- Appuyez sur F6 pour enregistrer l'écran de jeu (report de bug ou clips) ; les enregistrements sont sauvegardés en AVI dans Documents/DyingStar/records.
- Add a mining depot: deposit mined ore, refine it by volume (ore purity, stock and per-crate fill shown on the depot screen) and extract a carryable crate of ore.
- Les rochers miniers montrent désormais leur minerai : quelques petites traces en surface, et la vraie quantité se révèle en cassant le rocher — les morceaux les plus riches contiennent plus de minerai.
- E** pour **porter** ou **lâcher** un minerai (un seul à la fois).
  Seul un minerai **entièrement miné** (sans faille) est portable ; impossible de prendre celui d'un autre joueur.
  Porter **ralentit**, le minerai **flotte devant** soi (sans collision) et **tout est visible des autres joueurs**.
  Le **perforateur** est toujours là : **rangé** par défaut/pendant le port, **sorti** quand on l'équipe.
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
