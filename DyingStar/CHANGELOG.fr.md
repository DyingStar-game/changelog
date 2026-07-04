# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

- La direction du véhicule est désormais progressive et auto-centrante, avec un angle de braquage sensible à la vitesse (plus précis à basse vitesse, plus stable à haute vitesse).
- Un joueur qui se connecte voit désormais l'état actuel de tous les joueurs déjà présents (lampe allumée/éteinte, outil équipé, objet porté…), au lieu de ne le voir qu'au prochain changement.
- Corrections véhicule : un véhicule sans conducteur ne repart plus tout seul (il ralentit jusqu'à l'arrêt), les véhicules apparaissent frein à main serré, une porte laissée ouverte est visible par les joueurs qui se connectent ensuite, et le volant du camion tourne correctement autour de sa colonne.
- Les véhicules peuvent désormais utiliser un vrai modèle 3D : roues et volant animés, portes ouvrables via leur poignée (visée + E), collision réalisée sous Blender, et écrans dans la cabine. Il faut ouvrir une porte (viser la poignée + E) avant de pouvoir monter ou descendre.
- Correction du LOD de l'appartement VIP qui causait un soucis visuel. Le bon modèle est désormais affiché quand le joueur est proche de celui-ci.
- Test des conteneur / habitations
- Fonctionnalité : les zones minières génèrent des champs rocheux côté serveur à l’entrée du joueur (ensemencés et renouvelables).
  Fonctionnalité : variantes de roches exploitables de petite, moyenne et grande taille.
  Fonctionnalité : chaque zone contient un minéral répliqué via `mineral_id` (or, fer, cryptonite).
- fix bug visuel quand joueur sort de l'appartement
  fix rocher insaisissable (petit morceau)
  optimisation du réseau
  ajout du moteur frein sur le camion
  amélioration de l'affichage de l'écran de chargement
- Mise jour du projet sous Godot 4.7
  Activation du HDR
- Corrige la duplication des dépôts de minage en base à chaque redémarrage du serveur.
- Ajout d'un cycle jour/nuit de 30 minutes et d'un ciel physique (couleurs de lever/coucher) au sandbox.
- feat: FPS limit + field-of-view graphics settings (persisted)
  feat: working audio settings (bus volumes, input/output device, mic test)
  fix: settings menu active-category highlight + title; V-Sync label
  fix: main-menu and ERROR 1337 layouts no longer shift on window resize
  fix: pause menu button SFX
- On voit désormais les autres joueurs allumer et éteindre leur lampe torche.
- Modification du fret : déposez un objet dans la benne d'un camion (ou par-dessus le bord) pour le charger, roulez avec, et renversez le camion pour le décharger. Modif des rétroviseurs / caméra de recul au niveau des perf client.
- Tes réglages vidéo (moniteur, résolution, plein écran, v-sync) sont conservés d'une session à l'autre.
  Nouvelle case "Dev mode" dans les réglages Vidéo : elle ignore la résolution/plein écran sauvegardés au lancement (pratique pour lancer plusieurs fenêtres de jeu en même temps).
  Le pseudo des autres joueurs ne tremble plus, et se masque quand ils sont trop loin.
- Allumer/éteindre sa lampe torche assis dans un véhicule (conducteur ou passager).
  Spammer la touche de reset du véhicule ne fait plus décoller le camion.
  Se tenir dans la benne ajoute son poids à la charge, et on charge une caisse en la déposant dans la benne ; porter une caisse ne renverse plus un camion.
  Les morceaux de rocher pèsent désormais selon leur taille, et en porter un dans la benne ajoute son poids à la charge.
- On ne peut plus ramasser d'objets à travers les murs ; l'invite de ramassage n'apparaît que si l'objet est réellement atteignable.
- Ajout d'un chat textuel en jeu : affiché par défaut à gauche, F12 pour masquer/afficher, Entrée pour écrire et envoyer, Échap pour annuler, Tab pour changer de canal.
- Ajout des props de rations alimentaires (biscuit, nutrigris).
- Toutes les touches gameplay (reset/phares véhicule, frein & frein à main, l'outil « Zapette », la
  roue de spawn) sont reconfigurables dans Réglages → Contrôles.
  Le menu réglages fonctionne : liste des contrôles, plein écran/fenêtré, résolution auto-remplie
  depuis ton écran, choix du moniteur.
  E permet d'embarquer ; Y pour descendre ; une seule roue de spawn sur T.
  Menu pause réordonné (Reprendre / Réglages / Retour menu / Quitter) ; Réglages ouvre le menu complet.
  Écran d'accueil : bouton Quitter. Le curseur apparaît à l'ouverture du menu pause. L'overlay de
  debug reste dans le coin à toute résolution.
- Les véhicules peuvent afficher une caméra de recul et des rétroviseurs en direct sur des écrans
  de cabine (drop-in RearCamera réutilisable ; "mirror" inverse gauche/droite). Le camion embarque
  une caméra de recul + deux rétros.
- Phares de véhicule : le dev pose juste des Light3D dans le groupe "vehicle_light" de sa scène
  (aucun code) ; le conducteur les bascule avec L. Affichés sur le HUD et le tableau de bord.
  L est contextuel : phares en conduite, torche du joueur à pied. La torche est maintenant visible
  par les autres joueurs et démarre éteinte.
  Un camion à l'arrêt ne flue plus avec le frein à main (il se fige une fois stoppé).
  La benne déverse tout son chargement quand le véhicule se renverse.
- On peut désormais récupérer une caisse ou un rocher déposé dans la benne d'un véhicule.
  Le chargement posé en benne ne disparaît plus en multijoueur.
  Un véhicule ne peut plus être chargé dans la benne d'un autre véhicule.
  Les passagers comptent dans la charge du véhicule (SURCHARGE).
  Invites « [E] Carry » / « [E] Drop » quand on vise un objet ou qu'on en porte un.
  Les objets portés sont solides pour le monde et les autres joueurs (pas pour le porteur).
  Un siège de véhicule se libère quand son occupant se déconnecte.
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
