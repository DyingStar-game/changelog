# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Added

- **Bâtiments** : Les logements d'arrivée sont des conteneurs d'habitation, chacun avec un lit, une table de chevet et une armoire.
- **Bâtiments** : Les logements en conteneurs montent sur plusieurs étages, desservis par des coursives et des escaliers.
- **Bâtiments** : La plaque d'un conteneur affiche son numéro, en rouge s'il est occupé et en vert s'il est libre, et le nom de son occupant est sur la porte.
- **Objets** : Les portes, les tiroirs et la lampe de chevet de votre logement s'ouvrent, se ferment et s'allument, et tout le monde les voit comme vous les avez laissés.
- **Objets** : Les étagères de l'armoire accueillent ce que vous portez.
- **Joueur** : Vous pouvez vous allonger sur votre lit et vous relever.
- **Joueur** : Les garde-corps et les barrières peuvent être franchis d'un saut.
- **Carte stellaire** : Votre logement apparaît sur la carte stellaire, depuis n'importe où sur sa planète.
- **Interface** : Toucher un écran y porte votre main, avec un son de contact.
- **Audio** : Les portes de conteneur, les armoires et les tiroirs ont leurs propres sons.
- **Bâtiments** : Chaque logement a une douche, des toilettes et un miroir.
- **Objets** : Le miroir montre la pièce et vous-même, et ses lumières s'allument comme un néon.
- **Objets** : La lumière de la douche et des toilettes s'allume quand leur porte s'ouvre et s'éteint quand plus personne n'est dedans.
- **Bâtiments** : Un village minier compte environ 250 logements.

### Changed

- **Interface** : Les écrans se cliquent de plus près.
- **Interface** : Un meuble qui ne vous appartient pas affiche une invite en rouge.
- **Objets** : Les portes s'arrêtent quand elles rencontrent un mur ou un meuble.
- **Interface** : L'invite d'interaction s'affiche à côté du viseur.
- **Performances** : Seuls les logements proches de vous sont meublés : un village de logements coûte moins cher à afficher.

### Fixed

- **Graphismes** : Un village de logements ne manque plus de place pour ses effets de shader.

## [0.1.0-dev.202610201627] - 2026-10-20

### Changed

- **Performances** : Les serveurs restent fluides autour des villages animés : les foules de personnages ne recalculent plus leur trajet toutes en même temps.

## [0.1.0-dev.202610201544] - 2026-10-20

### Added

- **Interface** : L'écran de chargement affiche votre place dans la file quand les serveurs sont pleins.
- **Objets** : Lit
- **Objets** : Table de chevet
- **Objets** : Armoire
- **Objets** : Cabine de douche
- **Objets** : Cabine de toilettes
- **Objets** : Lavabo
- **Objets** : Miroir

### Changed

- **Objets** : Les conteneurs standard ont leurs vraies dimensions, avec des collisions qui épousent leur forme.
- **Objets** : Les conteneurs standard coûtent moins cher à afficher de loin.

### Fixed

- **Objets** : Les conteneurs standard ne disparaissent plus quand on les regarde de loin.
- **Objets** : La peinture jaune des conteneurs s'affiche de nouveau correctement.

## [0.1.0-dev.202610192155] - 2026-10-19

### Fixed

- **Performances** : Les serveurs de jeu sans personne dessus n'occupent plus chacun un cœur de processeur entier.

## [0.1.0-dev.202610192045] - 2026-10-19

### Added

- **Joueur** : Un DataPad porté au poignet gauche : levez-le pour lire la tablette des services sur son écran, même au volant ; un voyant vert et un bip signalent qu'un message attend.
- **Véhicules** : Le régulateur de vitesse maintient la vitesse à laquelle vous roulez : activez-le avec Ctrl+T, ajustez-le à la molette, et reprenez la main en appuyant sur une pédale.
- **Véhicules** : L'écran central du camion peut afficher la carte stellaire ou la caméra de recul, ou rester en veille avec le logo ARES Hauling : visez-le et appuyez sur F pour changer, pour tout l'équipage.
- **Véhicules** : En marche arrière, l'écran central affiche la caméra de recul, quel que soit son mode.
- **Véhicules** : La carte stellaire de l'écran du camion est partagée : quand un passager zoome ou la déplace, tout l'équipage voit la même vue.
- **Carte stellaire** : Les bâtiments, distributeurs, ascenseurs, téléporteurs et véhicules apparaissent sur la carte stellaire, avec leur pictogramme et leur nom au survol.
- **Carte stellaire** : La carte stellaire se zoome jusqu'au mètre autour de vous.
- **Carte stellaire** : La carte stellaire se manie comme une carte en ligne : glisser pour tourner, glisser au clic droit pour zoomer, clic droit pour copier les coordonnées ou poser un repère, Tab pour chercher.
- **Audio** : L'ascenseur à véhicules fait retentir une alarme aux deux paliers pendant qu'il roule.
- **Audio** : Les suspensions des véhicules émettent un choc pneumatique sur une bosse, un nid-de-poule ou une réception de saut, entendu par tous les joueurs proches depuis la roue concernée, plus fort et plus grave selon la violence du choc.

### Changed

- **Véhicules** : Les véhicules subissent une vraie résistance de l'air et du roulement : le moteur travaille encore à pleine vitesse, et un air plus rare laisse aller un peu plus vite.
- **Joueur** : Votre personnage se lance et s'arrête de courir plus vivement, et avance de façon fluide au lieu de petites saccades.
- **Joueur** : Passer de la marche à la course ne donne plus d'à-coup à la vue.
- **Objets** : Les caisses métalliques, batteries et moteurs sonnent comme du métal quand on les prend et qu'on les pose.
- **Commandes** : Le limiteur de vitesse se règle désormais à la molette seule.
- **Audio** : Le bruit des pneus devient plus fort et plus aigu avec la vitesse, et s'efface quand les roues quittent le sol.
- **Audio** : Le frottement des pneus quand on braque est plus discret.
- **Véhicules** : Les phares du camion éclairent la route devant lui au lieu d'une tache juste devant le pare-chocs.

### Fixed

- **Véhicules** : Les caisses déposées dans la benne du camion sont détectées là où se trouve vraiment la benne.
- **Carte stellaire** : Les routes et les canyons ne tremblent plus sur la carte stellaire en zoom rapproché.
- **Performances** : Le serveur de jeu ralentit beaucoup moins quand beaucoup de joueurs arrivent ou quand une région du monde passe sur un autre serveur.
- **Serveur** : Le serveur de jeu ne plante plus au hasard pendant le chargement des villages.
- **Audio** : Le conducteur n'entend plus les pneus à plein volume quelle que soit la vitesse.
- **Véhicules** : L'écran de recul du camion montre la route derrière dans le bon sens, comme les rétroviseurs.
- **Graphismes** : Les routes goudronnées renvoient la lumière des phares au lieu de rester d'un noir total la nuit.

## [0.1.0-dev.202610161255] - 2026-10-16

### Added

- **Audio** : Les propulseurs de la combinaison soufflent quand on se déplace dans l'espace, et les joueurs proches les entendent.
- **Audio** : Les vêtements froissent quand on ramasse un objet, actionne une porte, monte ou descend d'un siège, s'accroupit ou s'allonge.
- **Joueur** : Le conducteur tient le volant à deux mains, et ses mains le suivent quand il tourne.
- **Véhicules** : La barre de puissance du tableau de bord passe du vert au rouge selon la puissance demandée aux moteurs.

### Changed

- **Véhicules** : Les portes s'ouvrent quand la main atteint la poignée, plus à l'instant de l'appui.
- **Véhicules** : Le conducteur du camion est assis un peu plus près du volant.

### Fixed

- **Performances** : Le serveur de jeu ralentit moins quand beaucoup de personnages arrivent en même temps.
- **Véhicules** : Un camion qui tombe d'une falaise n'ajoute plus de vitesse ni de distance à son tableau de bord.
- **Véhicules** : La poussière des roues s'arrête quand le camion quitte le sol.
- **Joueur** : Les joueurs assis peuvent de nouveau utiliser les écrans.
- **Audio** : Les bruits de pas ne rejouent jamais deux fois de suite le même son.
- **Interface** : La liste des crédits affiche de nouveau chaque auteur à côté de son œuvre.
- **Bâtiments** : Le distributeur de rations repose sur un sol aplani.

## [0.1.0-dev.202610151839] - 2026-10-15

### Fixed

- **Bâtiments** : L'ascenseur à véhicules n'a plus de morceaux manquants à certaines distances quand la distance d'affichage des structures n'est pas à sa valeur par défaut.
- **Joueur** : Monter sur l'ascenseur à véhicules ne vous fait plus faire de salto aux yeux des autres joueurs et ne vous ralentit plus.
- **Performances** : Plus de petit gel en montant sur l'ascenseur à véhicules ou en entrant dans un bâtiment.
- **Véhicules** : Un camion qui monte sur l'ascenseur à véhicules ne reste plus bloqué comme s'il était cassé.

## [0.1.0-dev.202610142314] - 2026-10-14

### Added

- **PlanetTech** : Nouvelle vue de débogage des filets de sécurité sous le sol (Réglages > Debug), en rouge là où le sol de secours dépasse du terrain, en magenta là où le rattrapage de chute passe au-dessus.
- **Carte stellaire** : Sous 6 500 km, la vue suit la rotation de la planète : le sol ne glisse plus.
- **Objets** : Distributeurs ARES : pièces de véhicule au garage, rations dans les villages miniers, outil de minage au dépôt de cargo. Choisissez sur l'écran, attendez la livraison, prenez vos objets dans la trappe.
- **Audio** : L'ascenseur à ses sons: son treuil, le roulement de la plateforme sur le rail, et un lourd choc au départ et à l'arrêt.
- **Véhicules** : Nouveau tableau de bord pour le camion
- **Véhicules** : Une porte ouverte clignote et bipe au tableau de bord, de plus en plus vite quand le vent va la claquer.
- **Véhicules** : « Relevez-vous pour installer ou retirer un composant » quand on est accroupi ou allongé devant une pièce.
- **Joueur** : Votre propre tête projette maintenant son ombre.
- **Interface** : L'écran d'accueil indique que le jeu est en développement et que beaucoup d'éléments sont provisoires.
- **Véhicules** : Ajout d'un dossier "vehicle_lift" et son contenu dans "addons" (scripts, modèles, textures...)
- **Interface** : Ajout d'un test dans guid_3d pour être certain de la présence d'un viewport
- **Économie** : « Mes contrats » liste ce que tu as créé, et un objectif à validation manuelle se confirme.
- **Joueur** : Franchissement automatique** : le personnage franchit les obstacles tout seul — vault par-dessus les bas, grimpe sur les rebords (y compris surélevés), et enjambe en douceur les petites marches qui bloquaient.

### Changed

- **Commandes** : La lampe torche a sa propre touche, U (croix haut à la manette) : allumer les phares n'allume plus la torche.
- **Commandes** : Les phares des véhicules restent sur L et passent sur la croix bas à la manette.
- **Carte stellaire** : Les canyons sont plus légers et tracés en courbes, comme le sol les montre.
- **Minage** : On ne commence plus avec un outil de minage : allez le chercher à la machine ARES Mining du dépôt de cargo. La touche d'action le prend ou le pose ; il reste à vous.
- **Interface** : Les écrans 3D s'utilisent au viseur : passer devant une console ne bloque plus la vue.
- **Objets** : Les petits objets posés au sol se ramassent debout.
- **Véhicules** : Les pièces moteur et batterie portent les mêmes icônes que le tableau de bord.
- **Bâtiments** : Téléporteur : destinations regroupées par type et triées, astres marqués planète / lune / géante, utilisable à la manette.
- **Bâtiments** : Les lumières des bâtiments s'allument au crépuscule (1900 lux), le garage est éclairé la nuit.
- **Météo** : La poussière soulevée par le vent prend la couleur du sol et passe en douceur d'un biome à l'autre
- **Véhicules** : Activation de l'addon dans les paramètres du projet
- **Serveur** : Modification du paramètre "rollForward" du fichier global.json pour laisser le projet C# se construire si le SDK est dans une version supérieur à celle recommandée
- **Serveur** : La ligne "websocket_url" du fichier "client.ini" a également été modifiée, elle ne devrait probablement pas l'être
- **Interface** : Regroupe les onze apps de la tablette en Social, Économie et Propriétés — huit onglets à la barre, Signalements et Système restent dans Plus.
- **Carte stellaire** : Les points d'intérêt ne demandent plus de coordonnées — prends ta position, ou place le point sur la carte.
- **Économie** : Les zones de mission acceptent un système ou un de tes POI ; les anciens kinds scène et aire étaient toujours rejetés.
- **Économie** : La ligne de partage par groupe n'apparaît que sur tes missions, et nomme le groupe.
- **Bâtiments** : Bâtiments collés : quand deux bâtiments sont assez proches pour que leurs zones plates se touchent, le plus petit se met au niveau du plus grand.
- **Véhicules** : Écrans de cabine** des véhicules (rétroviseurs et tableau de bord) : éteints moteur coupé, rallumés à l'allumage.

### Fixed

- **PlanetTech** : La paroi du canyon n'a plus de grand trou triangulaire à côté de la route.
- **PlanetTech** : Le sol ne scintille plus au bord des canyons.
- **PlanetTech** : Le canyon sous un pont n'est plus comblé de terrain.
- **Minage** : Les tapis du dépôt amènent les roches et les caisses jusqu'au bout, même quand le serveur est chargé.
- **Interface** : Avec une taille d'interface agrandie, les réglages ne sortent plus par la gauche de l'écran : les noms de réglages trop longs passent sur deux lignes.
- **Joueur** : Le joueur ne sautille plus sur place sur les crêtes de montagne et les bords de cratère.
- **Véhicules** : Un camion garé sur une crête de montagne n'est plus relâché dessus en boucle.
- **PlanetTech** : Sur Tarsis 3, plus de trous dans le sol au bord des routes qui longent une fissure.
- **PlanetTech** : Sur Tarsis 3, les petites marches et fentes là où deux portions de sol se rejoignent ont disparu, en pleine nature comme dans les villages.
- **Interface** : Les noms de périphériques audio trop longs ne font plus sortir les réglages Audio par la gauche de l'écran ; ils sont raccourcis et affichés en entier au survol.
- **Interface** : Dès le lancement du jeu, Paramètres, Crédits et Retour fonctionnent de nouveau dans le menu principal.
- **Joueur** : Un joueur qui a quitté le jeu accroupi, allongé, en apesanteur ou au volant n'est plus bloqué dans cette posture à la reconnexion.
- **Minage** : Les joueurs n'apparaissent plus avec l'outil de minage à la ceinture avant de l'avoir pris à la machine ARES Mining.
- **Bâtiments** : Les joueurs ne restent plus sur « Apparition » près du dépôt de cargo, dont le sol était recalculé sans fin.
- **Carte stellaire** : Le panneau de debug s'affiche de nouveau par-dessus la carte stellaire.
- **Carte stellaire** : Les canyons n'ont plus de taches plus foncées là où ils se rejoignent.
- **Interface** : Les bulles d'aide ne couvrent plus le chat ni les boutons vocaux ; Échap ferme la tablette ouverte par F2.
- **Interface** : Corrige une tablette qui ne dessinait rien : une section hébergée était imbriquée trop profond et n'avait pas de hauteur.
- **Objets** : Étagères des cargo_depot : chaque dépôt crée une seule fois ses 193 étagères réseau, et un drapeau enregistré empêche de les recréer au redémarrage du serveur.
- **Bâtiments** : Apron des bâtiments : la zone plate autour d'un bâtiment n'est plus déformée par les bâtiments voisins.
- **PlanetTech** : Texture du sol : elle ne s'étire plus sur les pentes raides autour des bâtiments.
- **Social** : Corrige les joueurs affichés hors ligne dans la liste des contacts et sur les profils : le client
  utilise désormais le `sub` du token comme identifiant, au lieu d'un UUID aléatoire régénéré à
  chaque session. Cela supprime aussi la duplication de profils (`Player_xxxxxxx`) à chaque
  reconnexion.
  Corrige les noms des joueurs dans le social : ils viennent désormais du compte
  (`preferred_username`) au lieu du pseudo généré par le serveur de jeu.
  Corrige la position de présence qui utilisait le nom réseau de la planète : un joueur sur SandBox
  annonce maintenant `tarsis · tarsis_3` au lieu d'un système vide et d'une scène inconnue.
  Corrige le chat qui ne s'ouvrait pas avec F12. Le chat n'était jamais relié au broker de messages :
  aucun message ne pouvait donc être reçu ni envoyé.
  Messages privés : une conversation épinglée à la fois dans la zone de message, avec le nom du
  correspondant. L'en-tête est cliquable et liste toutes les conversations, celles ayant un nouveau
  message en premier, et se ferme avec le ✕.
  Le journal n'affiche plus que la conversation épinglée au lieu de mélanger tous les messages privés.
  Écrire à un contact directement depuis sa fiche, Entrée pour envoyer, sans quitter la fiche.
  Les notifications sociales (demande d'ami, demande acceptée, adhésion à une corporation)
  s'affichent en pile en haut de l'écran. Un clic ouvre l'écran où elles peuvent être traitées.
  Diagnostics : un nouveau bloc indiquant l'état de la connexion au broker du chat et de la salle
  vocale, rafraîchi chaque seconde tant que le panneau est ouvert.
- **Interface** : Menu pause** : plus possible de bouger, agir, percer ou regarder autour tant qu'il est ouvert.

## [0.1.0-dev.202610112359] - 2026-10-11

### Added

- **Météo** : Le vent soulève la poussière des plaines : elle défile autour de vous, voile le relief lointain et s'illumine dans le faisceau des lampes la nuit.
- **Météo** : La poussière des pas et des roues dérive avec le vent.
- **Météo** : On entend le vent, étouffé dans une cabine ou derrière un mur.
- **Graphismes** : Nouveau réglage « Poussière soulevée par le vent » (Désactivé / Bas / Élevé).
- **Météo** : Les véhicules et les joueurs soulèvent désormais la poussière du sol : une traînée derrière les roues du camion et une bouffée à chaque pas, plus épaisse sur le sable et la terre, plus légère sur la roche, aucune sur le métal. Les phares du camion projettent maintenant des ombres.
- **Graphismes** : Les autres planètes et lunes montrent désormais leur atmosphère de loin : un monde voilé paraît plus clair, un air épais plus pâle ou plus blanc, et le bord de l'air s'illumine quand il est assez grand à l'écran.
- **Social** : Ajoute de la connection client au service de jeux
  ajout du service social
  ajout du service economie
  ajout du service mission
  ajout du service inventory
  ajout du service market
  création d'une interface (F3)  avec des application qui appel ces service
  init du code pour que le server godot puisse s'authentifier sur keycloak pour acceder a des api interne des services
- **Interface** : Une courte liste à gauche de l'écran montre les touches utiles du moment — à pied, au volant, en portant, foreuse en main — et apprend : chaque ligne disparaît une fois sa touche utilisée, puis les suivantes (limiteur de vitesse, allure de marche, roulis…) arrivent après les bases.
- **Carte stellaire** : La carte stellaire affiche ses commandes de la même façon, à sa gauche.
- **Audio** : Un volume à part pour la musique du menu (Paramètres > Audio), et la musique ne se coupe plus net en arrivant dans une ville.
- **Commandes** : Accélérer et ralentir au volant ont leurs propres commandes configurable à lamanette : on peut les mettre sur les gâchettes de la manette sans changer les actions à pied.
- **Véhicules** : Une porte de véhicule restée ouverte claque toute seule au-delà d'une certaine vitesse — plus tôt dans un air épais, plus tard sur les plateaux.
- **Graphismes** : Chaque planète et chaque lune dotée d'une atmosphère a maintenant son propre ciel basé sur les calculs de physique des matériaux, gazs présents, taille etc...
- **Bâtiments** : Les villages miniers reçoivent des parcs à conteneurs, empilés jusqu'à trois, et des bennes à minerai.
- **Bâtiments** : Villes-usines : zones industrielles avec dépôts miniers, dépôts de fret, garages, deux téléporteurs et parcs à conteneurs.
- **Bâtiments** : Chaque village minier a sa cabine de téléportation, et la station orbitale retrouve la sienne.
- **Bâtiments** : Les bâtiments des villages portent des enseignes néon (garage, téléporteur, dépôts de fret et minier), dans votre langue.
- **Bâtiments** : Les villages miniers reçoivent projecteurs, lampadaires et caisses ; les groupes électrogènes des projecteurs ronronnent.
- **Commandes** : Nouvelle aide des commandes : F1 (ou maintenir View à la manette) affiche vos touches et ce que fait chacune.
- **Interface** : Nouvel écran Crédits dans le menu principal et le menu pause : toutes celles et ceux qui ont fait les musiques, sons, modèles et textures du jeu, en défilement comme un générique de film, sur une musique de la communauté.
- **Interface** : Chaque musique de l'écran Crédits a un bouton pour l'écouter.
- **Audio** : Dix nouvelles musiques : dans l'espace, en pleine nature, au menu, et dans les villages miniers et usines, jusqu'ici sans musique. Les morceaux dont on ne connaît pas l'auteur le disent dans les crédits : si l'un d'eux est à toi, contacte-nous sur Discord.

### Changed

- **PlanetTech** : Le cache terrain passe en v60 pour prendre en compte les routes ré-exportées.
- **Performances** : Chaque export (serveur, Linux, Windows) reçoit son propre numéro de build (date, heure et nombre aléatoire), qui invalide le cache de chunks au premier lancement. Dans l'éditeur, il n'y a pas de numéro et rien ne change.
- **PlanetTech** : Modifications QGIS : les nouveaux types de POI, le remplissage auto de population/radius et les zones colorées par roche.
- **PlanetTech** : Nouvel export de tarsis_3 depuis QGIS
- **Minage** : Poids des rochers : un facteur réduit la densité des rochers (WEIGHT_REDUCTION_FACTOR, réglé à 25). Ils sont plus légers, on peut les porter plus tôt et il faut moins de découpes.
- **Minage** : Couleur des rochers : les rochers prennent la couleur du sol où ils apparaissent, avec sa luminosité et son aspect mat. Les morceaux cassés gardent cette couleur.
- **Véhicules** : Le camion atteint la même vitesse maximale quel que soit le nombre de moteurs installés (environ 100 km/h) ; plus de moteurs donnent plus de force en côte, pas plus de vitesse.
- **Véhicules** : Le camion ralentit toujours de lui-même quand on lâche l'accélérateur.
- **Carte stellaire** : La carte stellaire s'ouvre désormais dans l'onglet Navigation du DataPad (F2, ou F3 ▸ Navigation), dans le cadre de la tablette.
- **Commandes** : Le DataPad (F3) apparaît maintenant dans Réglages > Contrôles sous son nom, dans l'aide des commandes (F1) et dans les indications de jeu.
- **Joueur** : Le vol libre de développement s'appelle désormais « Mode Dieu » : la molette règle sa vitesse (affichée en haut de l'écran) et le clic molette vous pose au sol juste en dessous ; votre corps est masqué pendant le vol.
- **Performances** : Les bâtiments des villages passent par le streaming au lieu d'être tous construits d'un coup ;
- **Bâtiments** : $BoxDetectorEnd est retiré de mining_depot.gd ;
- **PlanetTech** : Feat(planet), ton travail en cours (85 fichiers) : la convention de longitude alignée sur QGIS, avec les scènes et les tests qui suivent, plus le nouvel export de tarsis_3 et son grade_profiles.pack re-baké.
- **Véhicules** : La touche de décélération freine désormais en roulant vers l'avant et ne recule qu'une fois à l'arrêt, et les freins arrêtent un camion chargé aussi fort qu'un camion vide.
- **Véhicules** : Composants de véhicule : « Installer » s'affiche en vert, « Enlever » en jaune, et chaque invite d'interaction repose sur un fond sombre qui la garde lisible.
- **Véhicules** : On monte dans un véhicule en regardant le siège, plus besoin d'être dans la zone, qui interférait parfois avec les composants et la benne
- **Bâtiments** : Les lampadaires, projecteurs et enseignes néon s'allument quand il fait sombre, plus seulement au coucher du soleil : dans les vallées sous le voile de corindon, ils s'allument en plein jour.
- **Bâtiments** : Projecteurs plus lumineux.
- **Objets** : Les conteneurs portent le logo ARES et gardent leurs détails bien plus loin.
- **Bâtiments** : Lampadaires, projecteurs et enseignes s'allument au crépuscule et s'éteignent à l'aube, l'un après l'autre.
- **Véhicules** : Le camion se démarre et se coupe à toute vitesse, et son régime suit maintenant ses roues.
- **Véhicules** : Les composants d'un véhicule ne peuvent plus être retirés moteur allumé.
- **Audio** : Les pas sur le sable, la terre et le gravier jouent un son provisoire pour l'instant (leurs sons n'avaient pas de source connue).

### Fixed

- **Minage** : Portage : un morceau cassé est maintenant tenu par son centre réel, et non plus par l'origine du rocher entier. Il n'est plus décalé dans les mains et tourne sur lui-même.
- **Minage** : Éclairage des rochers : le relief des textures est corrigé. Un rocher n'est plus tout clair ou tout noir selon la façon dont il est posé.
- **Véhicules** : Les moteurs et batteries du camion rentrent dans leurs trappes (60 × 40 × 30 cm) au lieu de dépasser du flanc.
- **Joueur** : Correction reparent en sortie d'habitation ou ça nous propulsait dans l'espace
- **Interface** : Menu principal : Correction de la scène du menu après réimport QGIS
- **Performances** : Plus d'à-coup de 400 ms toutes les 2 s côté client ;
- **PlanetTech** : L'outil de bake et hole_probe.gd sont réparés.
- **Graphismes** : Les planètes et lunes vues d'orbite sont désormais entièrement éclairées : plus de carrés noirs sur les régions rocheuses ou herbeuses, ni de quadrillage dans l'air des mondes voilés.
- **Graphismes** : La lumière du soleil ne suivait plus l'heure ni le trajet une fois assis dans un véhicule, et sautait à la sortie.
- **Serveur** : Fix crash du jeu dans certaines conditions
- **Véhicules** : Le camion n'a plus de lumière dans sa cabine.
- **Carte stellaire** : Cliquer sur une planète, une lune ou un point d'intérêt affiche de nouveau sa fiche.
- **Objets** : Les conteneurs reposent désormais sur des aires de stockage aplanies dans les villages miniers et les villes-usines, et ne flottent plus ni ne s'enfoncent dans les pentes.
- **Bâtiments** : La téléportation vers la station orbitale fonctionne de nouveau.
- **Objets** : Les caisses moyennes ne se portent plus à la main, et l'invite « Porter » n'apparaît que sur ce qu'on peut porter.
- **Joueur** : Le faisceau de votre lampe torche n'est plus coupé par l'ombre de vos propres épaules.
- **Véhicules** : Plus de crash serveur sur une batterie supprimée
  batteries() et l'affichage véhicule ignorent une batterie déjà supprimée.
  L'écran de bord ne tourne plus sur le serveur, ce qui supprime aussi le spam « String formatting error ».
  fix(vehicle) : une pièce montée ne collisionne plus avec son camion
  La pièce (batterie, moteur) exclut la collision avec son camion dès sa création, ce qui supprime l'envol du camion au changement de serveur.
  fix(server) : un camion qui change de serveur continue de rouler
  À la frontière, le camion reçu reprend son état et sa vitesse. Ce n'est pas fait au chargement depuis la base.
  La vitesse est appliquée dès que le camion n'est plus figé, dans la limite de 1,5 s.
  Une copie restée active est adoptée, ce qui supprime le retour en arrière du conducteur.
  Le gel « pas de sol » est levé à l'adoption.
- **Joueur** : Le personnage pouvait continuer à monter une pente après avoir relâché la touche.
- **Interface** : Les captures prises après avoir redimensionné la fenêtre étaient coupées.
- **Commandes** : En AZERTY et autres dispositions, l'aide F1 allumait la touche du micro au mauvais endroit.
- **Commandes** : Dev : les touches + / - de l'heure changent à nouveau l'heure instantanément.

## [0.1.0-dev.202610042359] - 2026-10-04

### Added

- **Serveur** : Nouveau système lors de la création d'un nouveau serveur (maillage de serveurs dynamique) et transfert des objets et des joueurs vers ce nouveau serveur
- **Bâtiments** : Ajout du garage
- **Véhicules** : Nouveau : la batterie T1. Le camion roule désormais à l'énergie : il ne démarre pas sans batterie chargée, et la batterie se vide selon l'effort des moteurs (les pentes et les lourdes charges la vident plus vite).
- **Véhicules** : Un camion utilise une batterie à la fois et passe à la suivante quand elle est vide ; la batterie en service ne peut pas être retirée moteur allumé.
- **Véhicules** : Chaque batterie affiche sa charge (en kWh) sur ses flancs, et le tableau de bord du camion montre une barre par batterie avec son pourcentage (vert, orange, rouge).
- **Véhicules** : Les batteries peuvent être apparues avec la roue d'apparition.
- **Audio** : Nouvelles musiques : « Balade » (LRC), « A starry night » et « Meloncholia » (Koothka), « EVA Atmo 1 » (Solstium), « Syd where are you » (spaceman), en EVA, en station spatiale et en pleine nature.
- **Carte stellaire** : Toutes les commandes (clic, double-clic, clic droit, clic molette, molette, manette) sont réassignables dans Paramètres > Contrôles, et la ligne d'aide en bas de la carte affiche vos propres touches.
- **Carte stellaire** : Le bouton X de la manette réinitialise la vue.
- **Véhicules** : Le camion a une plaque d'immatriculation.
- **Audio** : Nouvelle musique en pleine nature, par Plx.
- **Bâtiments** : Villages POI : le serveur crée les bâtiments d'un village et peut le réveiller quand Horizon demande des logements pour de nouveaux joueurs.
- **Bâtiments** : Ajout d'un sous-sol et d'un escalier pour y accéder.
- **Graphismes** : Création d'une nouvelle scène de lumière "led_panel_1x1m.tscn".
- **Graphismes** : Si vous rencontrez des problèmes de perf, nouveau benchmark en jeu (Paramètres > Graphismes > Benchmark) : la vue tourne lentement sur place pendant que chaque option graphique est baissée tour à tour, puis vos réglages sont remis. Il écrit un rapport de ce que coûte chaque option sur votre machine (copié aussi dans le presse-papiers) à envoyer à WarpZone/KiFouine ; « Ouvrir le dossier » affiche les rapports.
- **Commandes** : Support de la manette : jouer à la manette (disposition Xbox par défaut), réattribuer ses boutons dans Contrôles (colonnes Clavier / souris et Manette séparées), et les indications à l'écran suivent l'appareil utilisé.
  Les menus se pilotent à la manette : croix / stick pour se déplacer, A pour valider, B pour revenir, LB / RB pour les catégories, LT / RT pour la barre du haut.
  La carte stellaire affiche longitude, latitude et altitude sous le curseur près d'un astre.
  FPS / GPU affichés dans la rangée d'onglets des paramètres ; nouveau curseur de volume Interface.
  Menu Audio : nouveau slider pour changer le volume de l'interface
- **Audio** : La musique change selon où vous êtes : menu, espace, points d'intérêt et lieux avec leur propre musique, avec des fondus entre les morceaux. Mise en place de l'architecture permettant l'ajout facile de nouvelles musiques.
- **Audio** : Nouveaux morceaux : Beyond the Horizon et Tin Can.
- **Audio** : Bruits de pas sur le métal.
- **Audio** : Panneau de debug : une section Musique indique quel morceau joue et pourquoi.
- **Serveur** : Ajout de l'ESG (EntityStreamingGodot)
- **Carte stellaire** : Carte stellaire (F2) : les canyons sont maintenant visibles, en vrai relief près du sol et en bandes sombres vus de plus haut.
  Carte stellaire : les tunnels et les ponts sont indiqués sur les routes et les voies ferrées quand on est assez près (environ 30 km d'altitude) ; les voies ferrées sont dessinées avec leurs traverses.
  Carte stellaire : les points d'intérêt qui se chevauchent sont regroupés sous un seul repère avec leur nombre ; ils se séparent en zoomant, et un clic sur un groupe zoome dessus.
  Carte stellaire : au-dessus d'une station orbitale sélectionnée, le clic molette fait tourner la vue autour de la station.
  Corrigé : les routes et les voies ferrées apparaissaient en morceaux sur la carte vue de haut.
  Contrôles : on peut attribuer des combinaisons de touches (Ctrl, Alt, Maj + une touche) et n'importe quel bouton de souris, clic molette compris.
  Contrôles : une combinaison ne déclenche plus aussi l'action liée à la touche seule (Ctrl+E ne déclenche plus E).
  Paramètres graphiques : les FPS et le temps GPU s'affichent en haut de l'onglet, avec un code couleur ; le curseur d'heure est de retour dans le menu.
  Corrigé : le détail du sol en Moyen perdait le pavage hexagonal du terrain.
  Panneau de debug : la Boîte serveur liste toutes les zones dans un tableau qui défile tout seul.
  Camion : direction plus douce.
  Fusion du travail de The_Moye sur les panel de debug
- **Interface** : Nouveau réglage : taille de l'interface (Paramètres > Général).
- **Interface** : Le menu principal est maintenant une scène vivante sur Tarsis 3 au lever du soleil, avec un avant-poste, des ouvriers et des camions sur la route ; la caméra se déplace selon l'écran du menu. Désactivable dans Paramètres > Général.
- **Graphismes** : Une scène de réglage pour comparer les options graphiques sur le vrai terrain, à toute heure, depuis Paramètres > Graphismes ou l'accueil.
- **Interface** : Une barre de progression sur les écrans de chargement.
- **Graphismes** : Nouvelles options graphiques : préréglages (détectés selon votre carte au premier lancement), mise à l'échelle FSR 1 / FSR 2.2, échelle de rendu, MSAA / FXAA / SMAA / TAA, qualité des ombres, SSAO / SSIL / SSR, halo lumineux, filtrage anisotrope, réduction du banding, qualité de l'atmosphère et du sol, et distances d'affichage du terrain / des bâtiments / de la végétation. Chaque option s'explique au survol.
- **Graphismes** : Un panneau graphique en jeu (Paramètres > Général) pour comparer les options en direct, avec FPS et temps GPU ; maintenir AltGr pour utiliser la souris.
- **Interface** : Les dossiers de captures et de vidéos s'ouvrent depuis le haut de Paramètres > Graphismes.
- **PlanetTech** : Bords organiques : méandres (domain warp) et bords rongés (fBm)
- **PlanetTech** : [volcans] Nouveaux types de pack : volcans (8), coulées de lave (9), fumerolles (10), dessinés dans QGIS
- **PlanetTech** : [volcans] Volcans : 5 presets (strato, bouclier, caldera, cône de scories, dôme), lac de lave et panache côté client
- **PlanetTech** : [volcans] Lave : ne remonte jamais les pentes (règle DESCENT), shader actif / en refroidissement / solide
- **PlanetTech** : [volcans] Fumerolles : évents placés de façon déterministe, dépôts de gaz dans les couleurs de sommets
- **Performances** : [Performances ] Précalcul : un nouvel outil, tools/bake_grade_profiles.tscn, calcule une fois pour toutes les profils des lignes, les franchissements de crevasses et les tabliers de pont. Il les écrit dans grade_profiles.pack, que le jeu charge au démarrage : 827 ms au lieu de plusieurs minutes.
- **Bâtiments** : Nouveau : la Station orbitale Palaka-Pital, sur une vraie orbite autour de SandBox (400 km, 1 h 44 par tour), accessible par téléporteur avec une cabine à bord pour revenir, et des anneaux qui tournent pour donner de la gravité à leur plancher.
- **Joueur** : Nouveau : une EVA avec une vraie inertie : roulis (A/E), monter/descendre (Espace/Ctrl), frein (X), un onglet EVA dans les touches, une animation de flottement, et la dérive orbitale près d'une station.
- **Carte stellaire** : Nouveau : la carte stellaire montre les stations et un cône de vue, et s'ouvre sur vous la première fois et après un voyage.

### Changed

- **Véhicules** : Les camions sortent désormais d'usine avec deux moteurs T1 et une batterie T1.
- **Carte stellaire** : Ses chiffres de debug passent dans le panneau de debug, avec leur propre case dans Paramètres > Debug.
- **Commandes** : Les boutons de la souris sont nommés dans votre langue dans la page des contrôles.
- **Joueur** : Plus de balancement de la caméra : la vue à la première personne reste stable en marchant, en courant, à l'arrêt ou en tournant sur place, et descend toujours quand vous vous accroupissez ou vous couchez.
- **Interface** : Le OK de la fenêtre « Manette détectée » a l'allure d'un bouton.
- **Interface** : Chaque réglage de l'inspecteur Godot s'explique désormais au survol (pour les créateurs).
- **PlanetTech** : Au premier lancement, le sol autour de vous apparaît en premier au lieu du paysage lointain.
- **Performances** : Le terrain se charge environ trois fois plus vite au premier lancement ou dans une nouvelle zone.
- **PlanetTech** : En vol rapide, le sol nouveau est affiché avec moins de détails pour suivre votre vitesse ; le sol déjà vu reste détaillé, et le détail complet revient quand vous ralentissez.
- **PlanetTech** : Le terrain que vous regardez arrive désormais en premier.
- **Joueur** : Décollage et arrêt plus fluides en vol rapide.
- **Performances** : Le terrain se charge environ trois fois plus vite au premier lancement ou dans une nouvelle zone : ses données sont désormais téléchargées par plusieurs connexions à la fois.
- **Performances** : Perf serveur : le TPS remonte de 7 à 55 environ et les entrées des joueurs ne sont plus en retard.
- **Performances** : NPC bloqués : ils espacent leurs nouvelles tentatives, ce qui divise environ par 10 les requêtes de navigation.
- **Performances** : NPC en attente de route : ils passent en veille comme les NPC inactifs, pour économiser de la physique.
- **Graphismes** : Mise à jour de la scène de lumière "led_panel_1x0.3m.tscn" (notamment un ajustement de l'intensité lumineuse).
- **Performances** : Fréquence d'images bien plus élevée dans une atmosphère : le ciel et le voile sont calculés avec une table précalculée au lieu d'une boucle par pixel (environ 41 → 70 FPS en Ultra sur une RTX 3090 au spawn).
- **Performances** : Moins d'à-coups réguliers dus à la rotation de la planète.
- **Performances** : Les tableaux de bord des camions et la StarMap sont dessinés que quand on les regarde.
- **Commandes** : Couper tout le son du jeu (N) et couper votre micro (M) apparaissent dans Contrôles > Général et peuvent être réattribués.
- **Interface** : Le chat et le HUD sont masqués quand le menu pause est ouvert.
- **PlanetTech** : Cache disque des chunks : il est passé de v56 à v58, donc les anciens chunks troués ou décalés sont reconstruits.
- **Interface** : Rework complet des menus
- **Interface** : Échap en jeu ouvre directement les paramètres, par-dessus le jeu.
- **Interface** : Les options de débogage ont leur propre onglet Debug.
- **Interface** : Les menus tiennent dans une zone centrale 16:9 sur les écrans larges, et suivent le passage entre fenêtré et plein écran.
- **Interface** : Les boutons de l'accueil et du menu pause partagent le même style ; ceux de l'accueil sont sur une seule ligne.
- **Interface** : Les panneaux de débogage (Alt+²) forment maintenant un seul panneau à droite, sans chevauchement, qui regroupe les relevés du sol, du déplacement et du véhicule, et le nombre de chunks de terrain affichés.
- **Interface** : L'alerte d'horloge de dev apparaît désormais dans ce panneau.
- **PlanetTech** : [Crevasses] Murs verticaux nets : diagonale des quads corrigée, portée du snap 1,6 pas, normales dédiées aux murs
- **PlanetTech** : [Crevasses] Hash entier à la place de sin : résultat identique au bit près sur toutes les plateformes
- **PlanetTech** : [Crevasses] Jumeaux C# bit-exacts (TileFrameNative, CrackVoronoiNative)
- **PlanetTech** : [volcans] Le bord du cratère s'abaisse du côté de la coulée : la lave déborde de 2 m au lieu de creuser un canyon de 203 m
- **Performances** : [Performances ] Creusement des lignes en C# (GradeCarveNative) : 32 → 12 µs par appel
- **Performances** : [Performances ] Chunks sous une coulée de lave : de −30 à −50 % de temps de génération
- **Performances** : [Performances ] Passe des chunks périmés indexée : 200–440 ms → 1–5 ms (le 1–3 FPS près de la lave)
- **Performances** : [Performances ] Cache disque des chunks lu et écrit hors du thread principal : ~330 ms/s → < 7 ms/s
- **Performances** : [Performances ] Construction d'un chunk près d'une ligne : elle ne lit plus que le morceau de profil qui la concerne, au lieu de reparcourir toute la ligne (212 000 nœuds pour le rail en anneau). Le résultat est identique au bit près.
- **Performances** : [Performances ] Mémoire : les relevés de terrain tous les 5 m ne sont plus gardés une fois le profil calculé, soit ~140 Mo de libérés.
- **PlanetTech** : [Performances ] Données périmées : si le bake ne correspond plus aux données (nouvel export, crevasses ou routes modifiées), le jeu recalcule lui-même et affiche un avertissement. Un test échoue, et link_modifiers.py rappelle la commande à relancer.
- **Serveur** : [Divers] limite de lint portée à 6 000 lignes, et deux nouvelles suites de tests (découpage des profils, bake).
- **Commandes** : Modifié : `action` passe de E à F, et la touche `interact` séparée disparaît : F ne fait qu'une chose à la fois.

### Removed

- **Graphismes** : La scène de réglage graphique disparaît : on voit le jeu à droite
- **PlanetTech** : [volcans] Suppression des anciens biomes volcaniques (script de migration fourni)
- **Bâtiments** : Retiré : le bouton Retour du téléporteur.

### Fixed

- **Serveur** : Si ton corps sort de l'arbre de scène pendant un transfert, il est remis sous le camion recréé (sinon sous la planète).
- **Serveur** : Tu es rassis au volant et la caméra revient sur toi. Tu ne vois plus à travers les yeux d'un autre joueur.
- **Serveur** : Le siège est libéré avant d'effacer un conducteur transféré, et son corps est retiré du camion.
- **Serveur** : Le camion est détruit au moins 2 frames physiques après son conducteur, et sorti de l'espace physique avant. Ça doit corriger les crashs du serveur Godot.
- **Serveur** : Le conducteur enregistré en base est maintenant l'occupant réel du siège. Un conducteur parti est effacé au bout de 10 s
- **Véhicules** : Les moteurs remis dans un camion restent dans leur baie après un redémarrage du serveur.
- **Performances** : Beaucoup moins d'à-coups à pied et en véhicule : le niveau de détail du terrain est désormais calculé en arrière-plan.
- **Performances** : Voler vite (EVA) ne fige plus le jeu pendant des secondes le temps que le terrain suive.
- **PlanetTech** : Plus de trous qui clignotent dans le sol devant vous quand vous avancez.
- **Performances** : Plus de gel du jeu quand vous vous éloignez d'une zone chargée.
- **Interface** : Correction d'un plantage quelques secondes après l'ouverture du menu principal au premier lancement.
- **Performances** : Plus de long gel en ralentissant ou en arrivant sur un sol déjà vu.
- **Bâtiments** : Terrain : sur une pente, les bâtiments reposent bien sur leur plateau et le sol entre eux n'est plus en dents de scie.
- **Graphismes** : Les lampes des bâtiments ne clignotent plus : seules les plus proches projettent une ombre (les autres éclairent toujours), ce qui est aussi plus rapide la nuit.
- **Interface** : Mise à jour du menu avec la position des PNJ et des camions
- **PlanetTech** : Un corps planétaire attend sa collision avec le terrain avant de devenir dynamique.
- **Commandes** : N et M ne pouvaient pas être tapés dans les champs de texte, comme la recherche des touches.
- **Interface** : Paramètres : la ligne survolée est de nouveau visible, et le fond derrière les paramètres est plus sombre et s'estompe plus doucement.
- **PlanetTech** : Trous devant le téléporteur : au village, les sommets du terrain n'étaient plus décalés vers la lèvre d'une fissure qui n'est pas creusée, et le terrain autour des bâtiments se rejoint à nouveau, en mesh comme en collision.
- **PlanetTech** : Marche entre chunks : de chaque côté d'une frontière de tuile élaguée, les deux chunks lisent maintenant la même hauteur. La marche de 24,5 cm a disparu, en GDScript comme en C#.
- **Interface** : Les infobulles sont lisibles : fond sombre, texte à la ligne.
- **Interface** : Les menus ne se redimensionnaient pas en passant du mode fenêtré au plein écran.
- **Performances** : Le jeu pouvait se figer en entrant dans l'univers depuis le menu principal.
- **Interface** : Le décalage de l'horloge de dev restait actif à la connexion suivante.
- **Commandes** : Maintenir AltGr faisait descendre en EVA ; les photos F7 montraient le panneau graphique.
- **Performances** : [Performances ] Bug de performance corrigé : le cache des tuiles de modificateurs faisait un parcours linéaire, sous verrou, à chaque lecture de hauteur. Tous les threads s'attendaient les uns les autres, et c'était de pire en pire avec le temps.
- **Joueur** : Quitter l'atmosphère d'une planète ne vous envoie plus au milieu du système.
- **Objets** : Une caisse portée à travers le téléporteur (ou le chargement d'un camion envoyé vers un autre astre) n'est plus supprimée et peut être posée.

## [0.1.0-dev.202609272359] - 2026-09-27

### Added

- **Véhicules** : Direction progressive. Un appui bref ou maintenu sur les flèches tourne les roues petit à petit ; elles gardent leur angle quand on relâche, et se redressent doucement en roulant.
- **Véhicules** : Limiteur de vitesse. T l'active ou le désactive, Alt + molette règle la limite par crans de 5 km/h. Affiché sur le tableau de bord : vert quand il est actif, rouge quand il retient le camion.
- **Véhicules** : Compteur kilométrique sur le tableau de bord, conservé entre les sessions et les redémarrages du serveur.
- **Interface** : F7 prend une photo sans aucune interface ; F8 prend une capture avec les panneaux de débogage pour les rapports de bug. Les deux sont rangées dans le dossier screenshots du jeu et copiées dans le presse-papiers.
- **Interface** : Réglages › Vidéo : un bouton ouvre la galerie de captures.
- **Carte stellaire** : Amélioration de la StarMap. Les planètes ont leur biomes, leur reliefs, leur ville, villages, gare, routes etc....
- **Graphismes** : Les objets posés sur une planète se fondent désormais dans le sol : la couleur et la texture du terrain remontent sur la base des bâtiments, rochers, caisses et props, avec une limite irrégulière façonnée par le vent. Les murs intérieurs et les surfaces horizontales restent propres, et la frange est éclairée comme le sol qu'elle imite. Elle ne s'assombrit donc pas contre un mur à l'ombre.
- **Interface** : Ajout d'un choix de langue (Automatique / Anglais / Français) dans Paramètres ▸ Général, appliqué immédiatement et conservé d'une session à l'autre.
- **Véhicules** : Le HUD de debug des véhicules affiche désormais la pente sur laquelle vous êtes, à côté des stats que vos moteurs peuvent franchir. Les composants de véhicule portent le pictogramme et numéro de série de ce qu'ils sont,  lisible des deux côtés du camion, et du dessus quand la pièce est posée au sol.
- **Véhicules** : Les véhicules sont mus par des moteurs qu'on peut voir. Le moteur T1 est un objet qu'on ramasse, qu'on porte et qu'on boulonne dans l'une des quatre trappes du camion — et ce qui est installé détermine sa force de traction, la pente qu'il franchit et son accélération. Retirez-en un et le camion s'essouffle ; retirez-les tous et il ne démarre plus. Une nouvelle option des réglages masque le tableau de bord du conducteur.
- **Bâtiments** : Ajout d'une cabine de téléportation pour les tests : on choisit un système, un corps et un point
  d'intérêt sur son écran, ou on saisit une longitude, une latitude et une hauteur, et on est posé au
  sol à cet endroit. Les véhicules garés dans la cabine et les joueurs qui s'y trouvent voyagent avec
  vous, et RETOUR ramène au point de départ. Corrige aussi un défaut préexistant qui faisait
  disparaître un véhicule pour le passager qui venait d'en descendre. Remplace les sept anciens pads fixes. Limite connue :
  descendre du véhicule avant de sauter — la vue et les commandes d'un passager assis peuvent ne pas
  survivre au trajet.

### Changed

- **Performances** : Amélioration des performances sur les segments
  Amélioration de la StarMap
  Ajout/correction de l'intégration continue pour les tests GUT
- **Interface** : Les enregistrements F6 sont désormais rangés dans screenshots/records.
- **PlanetTech** : Modification de la route pour qu'elle ne dépasse pas une pente de 10 degrés.
- **Interface** : L'interface en jeu est désormais traduite en anglais et en français. Les invites d'interaction affichent la touche réellement configurée, selon votre disposition de clavier, au lieu d'une touche figée.
- **Interface** : Les menus sont désormais entièrement traduits en anglais et en français. Les touches sont regroupées par familles (Général, À pied, En véhicule, En vol, Débogage), et les lignes de réglages se surlignent au survol.
- **PlanetTech** : Gestion du snap à la surface de la planète + mise à jour du mesh de terrain dans l'éditeur et runtime
- **Performances** : Optimistions joueur quand on a beaucoup de joueurs près de nous
- **Minage** : Impuretés rocheuses : couleur et minerai issus de la montagne pour chaque corindon
- **PlanetTech** : Mise à jour des montagnes pour intégrer des canyons dans les zones de corindon ; correction des bordures des canyons et raccordement à la base des montagnes

### Fixed

- **Commandes** : Une touche souris avec modificateur (ex. Alt + molette) perdait son modificateur une fois remappée.
- **Interface** : Panneaux de débogage affichant « Soon™ » juste après leur activation.
- **Interface** : S'approcher d'un écran n' "aspire" plus votre regard en mode sticky. Vous pouvez désormais déplacez le pointeur contre le bord de la fenêtre pour balayer un écran trop large, la vue reste stable pendant la lecture, et taper dans un champ ne déclenche plus les touches de jeu . Échap rend le clavier. Les panneaux ne se redessinent plus que lorsqu'ils sont visibles, et une touche frappée va à la console utilisée, non à tous les écrans du monde (oupsy)
- **Carte stellaire** : Le téléporteur et la carte du système affichent de nouveau la liste des planètes dans les builds exportés.
- **Audio** : Les pas sur le sable et la pierre ont enfin leur son, au lieu d'un marqueur d'erreur. Les pas sur le métal jouent toujours ce marqueur, en attendant un son sous licence libre.
- **Véhicules** : Fix le problème lié au siège du véhicule.
- **Véhicules** : Fix du dispositif de sécurité du véhicule : il semble ne pas monter suffisamment au-dessus du chunk lorsqu'il passe en dessous.

## [0.1.0-dev.202609202359] - 2026-09-20

### Added

- **Serveur** : [serveur] Ajout une sécurité pour les véhicules (similaire à celle des joueurs)
- **PlanetTech** : Ajout des montagnes
- **Serveur** : Rig de perf serveur ([debug] perf=true) : anatomie de la frame ([Perf/frame]), attribution par script ([Perf/bands], opt-in), recensement des nœuds, messages Horizon, ventilation du tick PNJ — chacun de ces postes a été trouvé grâce à lui.

### Changed

- **Serveur** : [serveur] Augmentation du nombre d'objets gérés dans Jolt
- **Serveur** : Cache de fichiers atomique pour le server meshing dynamic  (mesh de collision pour le serveur)
- **Performances** : Cache navmesh partagé (NpcNavCache) : tuiles de 72 m sur un treillis, une map par bloc de 5×5 cellules pour que les routes traversent les tuiles ; géométrie collectée par requête physique et extraite sur un worker ; TTL, invalidation, éviction ; les camions garés creusent le mesh.
- **Performances** : PNJ allégés : tick à 30 Hz entrelacé, sous-arbres inutiles désactivés côté serveur (UI, outil de minage, rayons, NavigationAgent3D), réplication seulement quand la pose change.
- **Performances** : Coûts annexes réduits : props statiques et véhicules garés à 6 Hz, anneaux HEALPix des pins mis en cache, balayage des pins cadencé au temps, planificateur de minage sans les PNJ.
- **Performances** : Mesuré : 47 PNJ → de 5 fps / 43 TPS à 60 / 60 ; 93 PNJ → 60 TPS.

### Fixed

- **Serveur** : [serveur] Correction stdout
- **Performances** : Problème : 50 à 90 PNJ marcheurs faisaient tomber le serveur à 5 fps. Chaque PNJ bakait son propre navmesh (parse de toute la planète sur le main thread, bake Recast à 0,1 m, re-bake tous les 18 m).
- **PlanetTech** : Correction d'un problème de « chunk »
  Correction du maillage de sécurité du joueur pour les tunnels
  Optimisations : évitement du rendu des rails et des routes trop éloignés et invisibles
  Correction du sol du tunnel
- **PlanetTech** : Autoroute en relief
  Correction : activation des éléments de débogage
  Correction : tuiles hexagonales sur les cartes AMD

## [0.1.0-dev.202609132359] - 2026-09-13

### Added

- **PlanetTech** : PlanetTech avec routes, exportation QGIS, refactorisation
- **PlanetTech** : Éditeur uniquement : un bouton « Fly in planet frame » dans la barre d'outils de la vue 3D fait survoler un corps avec le haut toujours en haut et l'avance qui suit la courbure, au lieu de la caméra alignée sur le monde qui part de travers dès qu'on s'éloigne du pôle.

### Changed

- **Performances** : Amelioration du calcul des chunks de -26 a -66 %
- **PlanetTech** : Utilisation des tuiles (points) sur un serveur web et utiisation en streaming.
- **Performances** : Amélioration du débogage des performances côté client

### Fixed

- **Véhicules** : Correction de la vue passager trop basse en véhicule : les poses conducteur et passager ne placent pas la tête au même endroit, et chacune a désormais sa propre hauteur d'œil.
- **Véhicules** : Un joueur à bord d'un véhicule appartient désormais au repère de ce véhicule : le trajet est fluide pour le conducteur comme pour le passager, et sa position n'est plus renvoyée sur le réseau à chaque tick pendant que le véhicule roule.
- **Interface** : Le panneau de debug affiche désormais l'altitude réelle au-dessus de la sphère de référence en plus de la hauteur au-dessus du sol, et les coordonnées du joueur continuent de se mettre à jour en véhicule.
- **Interface** : Correction du menu pause qui pouvait s'ouvrir par-dessus un jeu resté actif (la caméra continuait de tourner en dessous), de l'impossibilité de quitter Réglages > Contrôles avec Échap, et des étiquettes de nom qui restaient à hauteur d'homme debout quand le joueur était accroupi ou allongé. Les touches réassignées sont de nouveau appliquées au démarrage, et non plus seulement après avoir ouvert la page des contrôles. Échap annule désormais une réassignation de touche au lieu d'être assigné, et la touche de saut s'appelle « Jump / Vault ».
- **Joueur** : Le dernier cran de la molette ne fait plus passer le personnage au petit trot : toute la plage reste une marche, jouée plus vite, et seul le sprint change de démarche.
- **Véhicules** : Un joueur assis dans un véhicule est désormais affiché assis pour tout le monde, y compris pour les joueurs qui se connectent ou qui s'approchent après qu'il se soit assis.
- **Performances** : Correction du blocage du client à 6 FPS : la taille de la file d'attente du micro LiveKit était exprimée en millisecondes et non en échantillons
  Ajout de code de débogage
- **Joueur** : La vue à la première personne ne dérive plus quand on regarde autour de soi, et on ne voit plus son propre cou en courant ou en tournant la tête.
- **Joueur** : Les marches basses, bordures et escaliers se franchissent de façon fiable, y compris dans les portes et sous les plafonds bas où ils bloquaient.
- **Véhicules** : Les camions ne se retournent plus en virage serré, leurs roues bougent désormais avec la suspension pour tous ceux qui les voient, et leurs pneus s'entendent — ils crissent quand on braque sur place et roulent quand on prend de la vitesse. Le mini camion arrive avec un nouveau modèle et quatre bennes interchangeables.

## [0.1.0-dev.202609062359] - 2026-09-06

### Added

- **Performances** : Les utilisateurs peuvent activer le débogage des performances dans les journaux lorsqu'ils ont peu d'images par seconde.
- **Audio** : Les bruits de pas et les caisses posées sonnent selon la surface — métal, sable, pierre, béton — au lieu d'un échantillon unique partout. Les caisses s'entendent à la prise et à l'impact.

### Changed

- **Joueur** : Les joueurs sont desormais representes par un vrai modele de personnage au lieu du mannequin provisoire, en conservant toutes les animations existantes. La lampe torche est fixee a la tete, son faisceau suit donc le corps.
- **Joueur** : Le franchissement et l'escalade se déclenchent maintenant en APPUYANT SUR SAUT devant un obstacle, au lieu de se produire tout seuls quand on marche dedans. Les marches et petits rebords se montent toujours automatiquement.
- **Véhicules** : On ne peut plus monter dans un véhicule les mains pleines, et monter range vos outils.
- **PlanetTech** : Sandbox est desormais le troisieme monde du systeme Tarsis, plus proche de son etoile et protegee par son voile de corindon ; Gaea prend la quatrieme orbite. Sandbox et ses lunes Korax et Xarok sont renommees en consequence.
- **Graphismes** : Le ciel est désormais calculé à partir de l'atmosphère réelle de chaque monde — ses gaz, sa pression,
  sa poussière — au lieu d'un dégradé peint. Les couchers d'étoile, la couleur de l'éloignement et le
  voile sur les montagnes lointaines découlent tous de la même physique, et changent d'une planète à
  l'autre. Deux bugs qui éclairaient le monde la nuit, et donnaient aux bâtiments et aux sommets
  lointains un air rétroéclairé, sont corrigés.

### Fixed

- **PlanetTech** : Correction des ponts
  Désactivation de l'apparition de ressources par le joueur
  Augmentation de la probabilité d'apparition de rochers sur un chunk de 70 % à 90 %
- **PlanetTech** : Correction de la détection des falaises : les parois raides sont désormais reconnues correctement partout, au lieu que tout l'hémisphère éclairé soit rendu comme une falaise et que de vraies parois verticales soient ignorées.
- **Carte stellaire** : La carte stellaire (F2) et les affichages de debug fonctionnent désormais assis dans un véhicule, et la carte est réellement modale : plus rien ne réagit tant qu'elle est ouverte, et le camion se met en roue libre au lieu de garder les gaz.
- **Commandes** : Alt+L et Alt+I n'allument plus les phares et le moteur en même temps que leur outil de debug.
- **Audio** : Le curseur de volume SFX agit enfin sur tous les sons du jeu, et le réglage propre à un son fonctionne même quand il vient de vos mains ou de vos pieds.
- **Véhicules** : Un camion dont une porte est restée ouverte ne vous éjecte plus quand vous essayez de vous y asseoir.
- **Serveur** : Correction d'un démarrage du serveur de jeu sans aucun monde, qui laissait les joueurs immobiles.
- **Serveur** : Fix la rotation joueur et joueurs sort de sa zone (gorc)

## [0.1.0-dev.202608232359] - 2026-08-23

### Added

- **Carte stellaire** : Les planètes et les lunes du système Tarsis parcourent leurs véritables orbites, et une carte du système, sur F2, montre où se trouve chaque astre — et vous avec.
- **Graphismes** : Les nuits ont un ciel étoilé, et le crépuscule dure, en s'éteignant au-dessus du point où l'étoile s'est couchée.
- **PlanetTech** : Ajout de bornes kilométrique (posé à la main donc c'est du à peu près)

### Changed

- **Performances** : Limitation du nombre de threads pour le serveur pour améliorer les performances sur Kubernetes.
- **Serveur** : Mise à jour de la version de Godot sur le serveur vers la 4.7 ; j'avais oublié d'utiliser la 4.7 comme pour le client ;(

### Removed

- **Interface** : La roue de spawn de développement, l'outil de suppression d'objets et le vol libre EVA ne sont plus accessibles en jeu, et leurs raccourcis n'apparaissent plus dans les réglages de contrôles.

### Fixed

- **Interface** : Correction du problème de chargement infini de la page
- **Performances** : Les performances du serveur près des villes sont nettement améliorées, et les joueurs comme les véhicules ne tremblent plus sur place.
- **Véhicules** : Les camions placés dans le monde apparaissent enfin, au lieu de traverser le sol sans que personne ait pu les voir.
- **Joueur** : On ne traverse plus le sol de son habitation à la première connexion suivant un redémarrage du serveur.
- **Interface** : Les écrans 3D, comme celui du dépôt minier, sont de nouveau utilisables : le curseur ne tremble plus et ne revient plus se coller au milieu de l'écran, et les boutons se cliquent sur toute la surface.
- **Bâtiments** : Emprunter un téléporteur s'affiche maintenant correctement pour les autres joueurs.
- **Serveur** : Correction de la compilation et de la version. Le problème est désormais identique pour les clients Linux et Windows (essayez de corriger le lanceur et de mettre à jour le jeu).

## [0.1.0-dev.202608162359] - 2026-08-16

### Added

- **Serveur** : Gestion des PNJ
  ajout des propsync (objet réseau)
- **Audio** : Nouveaux sons** : les 3 types de vault, le perforateur (boucle de perçage, fin, raté, équiper/ranger), la torche du joueur, les phares du camion / moteur électrique.

### Changed

- **Joueur** : La marche, le sprint et l'accroupi se déplacent désormais aux vitesses décrites dans le document de design, et la vitesse de marche à la molette progresse régulièrement entre 0,5 et 3 m/s au lieu de faire des bonds.
- **Social** : Chat** : affiché par défaut, ordre des messages plus clair, lisible sur fond clair.
- **Interface** : Les icônes son/micro à l'écran sont en bas à gauche et plus petites.

### Fixed

- **Interface** : La roue d'emotes (T) ne fait plus apparaître d'objet lorsque la roue de spawn (Alt+T) a été utilisée auparavant.
- **Joueur** : Enchaîner les sauts en sprintant n'accumule plus une vitesse illimitée : un saut conserve l'élan qu'on avait au décollage.
- **Joueur** : L'animation des personnages ne clignote plus entre la marche et le trot lorsqu'on se déplace à allure constante près d'un changement d'allure.
- **Social** : Chat : maintenir TAB ne fait plus défiler les boutons de l'interface, et taper un message ne déclenche plus d'actions de jeu comme s'accroupir ou s'allonger.
- **Social** : Chat vocal : couper son micro coupe réellement l'émission, et la voix n'est plus captée en double.
- **Social** : Chat vocal : à plusieurs, toutes les voix sont entendues, et un joueur qui s'en va cesse d'être audible au lieu de persister ou d'être entendu deux fois à son retour.
- **Joueur** : Spawn** : un écran « Spawning... » tient jusqu'à ce que le monde soit prêt — plus de flash de jour ni de caméra qui se redresse juste après l'apparition.

## [0.1.0-dev.202608092359] - 2026-08-09

### Added

- **Joueur** : Les personnages ont un corps animé : vous voyez votre propre corps en 1re personne et les autres joueurs sont entièrement animés — marche/course/saut, accroupi (C) et allongé (W), pivot sur place, assis/conduite en véhicule, emotes (roue T) et port d'objets. Porter une caisse n'est possible que debout, et les outils rangés suivent le corps.

## [0.1.0-dev.202608022359] - 2026-08-02

### Added

- **Graphismes** : 🌌 Système stellaire
  Le monde est désormais entièrement éclairé par Starsis, l'étoile du système.
  Le cycle jour/nuit est maintenant calculé à partir de la position réelle de Starsis.
  Les couleurs des levers et couchers de l'étoile sont désormais dynamiques et physiquement cohérentes.
  Les planètes et les lunes sont correctement éclairées, même à des distances astronomiques.
  Le ciel suit désormais la position de Starsis, aussi bien dans la vue principale que dans les rétroviseurs des véhicules.
  La voûte céleste s'estompe progressivement vers le noir de l'espace en fonction de l'altitude.
  Chaque corps céleste tourne désormais sur son axe selon sa période de rotation réelle.
  🛰️ Interface
  Le HUD affiche maintenant la longitude, la latitude et l'heure locale du corps céleste sur lequel vous vous trouvez. (Debug)
  🛠️ Outils
  Ajout d'un mode de vol libre ($) pour explorer le système sans contrainte.
  Ajout de marqueurs de navigation permettant d'inspecter rapidement les planètes, lunes et autres objets du système stellaire. (A activer dans les settings)

## [0.1.0-dev.202607192359] - 2026-07-19

### Added

- **Graphismes** : Ajout de réglages Graphics pour activer/désactiver les ombres temps réel et régler la distance d'affichage des ombres du soleil (persistés, appliqués en direct).
- **Objets** : Les nouveaux containers de stockage verrouillent toute caisse qui se pose sur leur sol (impossible à bouler) ; on la reprend pour la libérer.
- **Audio** : Les joueurs ont du son : bruits de pas (échantillons aléatoires, cadence qui suit votre vitesse), interrupteur de la lampe torche et saut. Ils sont spatialisés et répliqués : vous entendez les joueurs autour de vous marcher, sauter et allumer leur lampe.

### Changed

- **Serveur** : Mise à jour des URL des serveurs vers la nouvelle infrastructure.
- **Objets** : Le portage d'objets est bien plus agréable : plus de « snap » dans les mains à la prise — l'objet rejoint la main en douceur et traîne quand on bouge, réagit aux chocs, et est solide tout de suite. Regarde en bas pour poser un objet au sol, en haut pour le placer en hauteur.
- **Joueur** : La portée d'interaction est désormais une valeur configurable sur le joueur.
- **Objets** : La roue de spawn de dev est désormais gérée par le serveur : les objets apparaissent devant vous, posés au sol et droits, et c'est le serveur qui décide où. La molette tourne un objet porté par paliers de 15°, et maintenir le clic molette permet de le faire pivoter librement sur tous les axes à la souris — le tout autour du centre de l'objet.
- **Minage** : Le dépôt de minerai n'est plus spawnable et empaquette son minerai dans une caisse de transport.
- **Véhicules** : Les véhicules se braquent et freinent moteur éteint, et le moteur peut être coupé à toute vitesse.
- **Interface** : Dans le menu des paramètres, Échap fait maintenant « retour » au lieu de libérer la souris.
- **PlanetTech** : Mise à jour des technologies planétaires. Génération de cartes de hauteur pour chaque niveau de détail. Correction du téléporteur vers une autre planète/un autre point.
- **Serveur** : Sur le réseau, les planètes sont désormais des objets génériques.

### Fixed

- **Social** : Correction du chat texte (connexion avec le serveur)
- **Performances** : Correction d'un pic de charge CPU physique au démarrage du serveur : les props rechargés depuis la persistance ne recalculent plus tous leurs collisions d'un coup — ils repartent gelés et se réveillent à l'approche d'un joueur.
- **Objets** : Un objet porté ne te repousse plus, et lever la tête dans un container ne l'envoie plus sur le toit.
- **Joueur** : Utiliser un écran 3D ne laisse plus votre caméra perdue dans l'espace.
- **Véhicules** : Une caisse qui tombe ou est jetée dans la benne d'un camion est désormais pesée comme si elle avait été chargée à la main.
- **Objets** : On ne peut plus attraper un objet ni ouvrir une porte de véhicule à travers un mur de bâtiment.
- **Véhicules** : Les phares de camion plus lumineux et une famille de crashs client corrigée.

## [0.1.0-dev.202607122359] - 2026-07-12

### Added

- **Audio** : Les véhicules ont du son : portes, démarrage et coupure du moteur, un régime moteur qui monte avec les tours, un klaxon (H) et un klaxon spécial (Alt+H), frein à main et phares. Le moteur doit désormais être démarré avec la clé de contact (I), à l'arrêt, avant que le véhicule puisse rouler.
- **Interface** : Le changement de résolution d'écran nécessite désormais une confirmation sous 10 secondes et est automatiquement annulé en cas de non-respect de cette consigne. Ainsi, une résolution trop élevée ne peut plus vous bloquer.
- **Interface** : Vous pouvez désormais afficher/masquer les panneaux de débogage à l'écran depuis Paramètres → Général, ou avec une touche réattribuable (par défaut Alt+²) disponible dans le menu Commandes.
- **Objets** : Les conteneurs de test sont désormais sensibles aux collisions.

### Changed

- **Véhicules** : Le modèle du mini-camion a été mis à jour (correction de l'axe de rotation des roues et de la zone de poids de la benne).
- **Objets** : Les objets transportés interagissent désormais physiquement avec le monde : vous pouvez les heurter et les poser contre le sol, les murs et les véhicules, et les empiler en regardant vers le haut ou vers le bas pour lever ou abaisser un objet tenu. Un objet hors de portée (par exemple, coincé derrière un mur) est automatiquement lâché.
- **Interface** : La roue d'apparition des développeurs (T) est désormais un menu à deux niveaux (catégorie → variante)
- **Objets** : Les caisses-palettes qu'elle génère peuvent être ramassées et transportées.
- **Performances** : Mise à jour de la physique à 60 FPS.
  Correction des collisions par chunk pour Jolt aux coordonnées astronomiques.
  Correction de l'exportation des données de terrain, de la validation du cache et de la mise en veille de la physique en cas d'inactivité.

### Fixed

- **Interface** : Le menu pause ne se ferme plus lorsque vous cliquez dans le vide : utilisez la touche Échap ou le bouton Reprendre.
- **Véhicules** : Camion : le volant tourne désormais dans le bon sens à une vitesse raisonnable, et l'image de la caméra de recul n'est plus inversée.
- **Véhicules** : Correction d'un bug : les portes des camions pouvaient refuser de s'ouvrir lorsqu'un élément de décor apparaissait à proximité, et le transport des caisses à distance normale est désormais possible les objets tenus en main flottent désormais un peu plus loin.

## [0.1.0-dev.202607052359] - 2026-07-05

### Added

- **PlanetTech** : Mise à jour de la planet tech, ajout de vallées, texture...
- **Objets** : Éditeur uniquement : ajout d'un outil DyingStar pour importer/exporter les props serveur d'une scène vers le startup_items.json d'horizonserver.

### Changed

- **PlanetTech** : Mettre à jour les options d'exportation pour les planètes
- **Véhicules** : La direction du véhicule est désormais progressive et auto-centrante, avec un angle de braquage sensible à la vitesse (plus précis à basse vitesse, plus stable à haute vitesse).

### Fixed

- **PlanetTech** : Correction du dossier de la planète et compilation
  Ajout de la maison Bardok pour les tests
  Ajout des conteneurs Kankan pour les tests
- **Objets** : Vous ne pouvez plus interagir avec quelque chose que vous ne pouvez pas voir : ramasser un objet nécessite désormais une ligne de vue dégagée, et une portière de véhicule ne s'ouvre par la poignée de votre côté (à l'extérieur à pied, à l'intérieur en position assise) que si elle n'est pas obstruée.
- **Joueur** : Un joueur qui se connecte voit désormais l'état actuel de tous les joueurs déjà présents (lampe allumée/éteinte, outil équipé, objet porté…), au lieu de ne le voir qu'au prochain changement.
- **Véhicules** : Corrections véhicule : un véhicule sans conducteur ne repart plus tout seul (il ralentit jusqu'à l'arrêt), les véhicules apparaissent frein à main serré, une porte laissée ouverte est visible par les joueurs qui se connectent ensuite, et le volant du camion tourne correctement autour de sa colonne.

## [0.1.0-dev.202606282359] - 2026-06-28

### Added

- **Véhicules** : Les véhicules peuvent désormais utiliser un vrai modèle 3D : roues et volant animés, portes ouvrables via leur poignée (visée + E), collision réalisée sous Blender, et écrans dans la cabine. Il faut ouvrir une porte (viser la poignée + E) avant de pouvoir monter ou descendre.
- **Bâtiments** : Test des conteneur / habitations

### Fixed

- **Bâtiments** : Correction du LOD de l'appartement VIP qui causait un soucis visuel. Le bon modèle est désormais affiché quand le joueur est proche de celui-ci.

## [0.1.0-dev.202606212359] - 2026-06-21

### Added

- **Minage** : Fonctionnalité : les zones minières génèrent des champs rocheux côté serveur à l’entrée du joueur (ensemencés et renouvelables).
  Fonctionnalité : variantes de roches exploitables de petite, moyenne et grande taille.
  Fonctionnalité : chaque zone contient un minéral répliqué via `mineral_id` (or, fer, cryptonite).
- **Graphismes** : Ajout d'un cycle jour/nuit de 30 minutes et d'un ciel physique (couleurs de lever/coucher) au sandbox.
- **Graphismes** : Feat: FPS limit + field-of-view graphics settings (persisted)
- **Audio** : Feat: working audio settings (bus volumes, input/output device, mic test)
- **Joueur** : On voit désormais les autres joueurs allumer et éteindre leur lampe torche.
- **Véhicules** : Modification du fret : déposez un objet dans la benne d'un camion (ou par-dessus le bord) pour le charger, roulez avec, et renversez le camion pour le décharger. Modif des rétroviseurs / caméra de recul au niveau des perf client.
- **Interface** : Nouvelle case "Dev mode" dans les réglages Vidéo : elle ignore la résolution/plein écran sauvegardés au lancement (pratique pour lancer plusieurs fenêtres de jeu en même temps).
- **Véhicules** : Allumer/éteindre sa lampe torche assis dans un véhicule (conducteur ou passager).
- **Véhicules** : Se tenir dans la benne ajoute son poids à la charge, et on charge une caisse en la déposant dans la benne ; porter une caisse ne renverse plus un camion.
- **Social** : Ajout d'un chat textuel en jeu : affiché par défaut à gauche, F12 pour masquer/afficher, Entrée pour écrire et envoyer, Échap pour annuler, Tab pour changer de canal.
- **Objets** : Ajout des props de rations alimentaires (biscuit, nutrigris).
- **Interface** : Écran d'accueil : bouton Quitter. Le curseur apparaît à l'ouverture du menu pause. L'overlay de debug reste dans le coin à toute résolution.
- **Véhicules** : Les véhicules peuvent afficher une caméra de recul et des rétroviseurs en direct sur des écrans de cabine (drop-in RearCamera réutilisable ; "mirror" inverse gauche/droite). Le camion embarque une caméra de recul + deux rétros.
- **Véhicules** : Phares de véhicule : le dev pose juste des Light3D dans le groupe "vehicle_light" de sa scène (aucun code) ; le conducteur les bascule avec L. Affichés sur le HUD et le tableau de bord.
- **Véhicules** : La benne déverse tout son chargement quand le véhicule se renverse.

### Changed

- **Serveur** : Mise jour du projet sous Godot 4.7
  Activation du HDR
- **Interface** : Tes réglages vidéo (moniteur, résolution, plein écran, v-sync) sont conservés d'une session à l'autre.
- **Minage** : Les morceaux de rocher pèsent désormais selon leur taille, et en porter un dans la benne ajoute son poids à la charge.
- **Commandes** : Toutes les touches gameplay (reset/phares véhicule, frein & frein à main, l'outil « Zapette », la roue de spawn) sont reconfigurables dans Réglages → Contrôles.
- **Commandes** : E permet d'embarquer ; Y pour descendre ; une seule roue de spawn sur T.
- **Interface** : Menu pause réordonné (Reprendre / Réglages / Retour menu / Quitter) ; Réglages ouvre le menu complet.
- **Commandes** : L est contextuel : phares en conduite, torche du joueur à pied. La torche est maintenant visible par les autres joueurs et démarre éteinte.

### Fixed

- **Minage** : Fix bug visuel quand joueur sort de l'appartement
  fix rocher insaisissable (petit morceau)
  optimisation du réseau
  ajout du moteur frein sur le camion
  amélioration de l'affichage de l'écran de chargement
- **Minage** : Corrige la duplication des dépôts de minage en base à chaque redémarrage du serveur.
- **Interface** : Fix: settings menu active-category highlight + title; V-Sync label fix: main-menu and ERROR 1337 layouts no longer shift on window resize fix: pause menu button SFX
- **Joueur** : Le pseudo des autres joueurs ne tremble plus, et se masque quand ils sont trop loin.
- **Véhicules** : Spammer la touche de reset du véhicule ne fait plus décoller le camion.
- **Objets** : On ne peut plus ramasser d'objets à travers les murs ; l'invite de ramassage n'apparaît que si l'objet est réellement atteignable.
- **Interface** : Le menu réglages fonctionne : liste des contrôles, plein écran/fenêtré, résolution auto-remplie depuis ton écran, choix du moniteur.
- **Véhicules** : Un camion à l'arrêt ne flue plus avec le frein à main (il se fige une fois stoppé).

## [0.1.0-dev.202606142359] - 2026-06-14

### Added

- **Véhicules** : On peut désormais récupérer une caisse ou un rocher déposé dans la benne d'un véhicule.
- **Objets** : Invites « [E] Carry » / « [E] Drop » quand on vise un objet ou qu'on en porte un.
- **Véhicules** : Nouveau frein à main du camion : appui long sur Espace sous 3 km/h, relâché par l'accélération, reste actif quand on sort. Affiché sur le tableau de bord, le HUD et l'aide.
- **Minage** : Les rochers minables peuvent contenir différents minéraux (or ajouté) ; l'aspect du minerai est piloté par des données.
- **Véhicules** : Ajout d'un camion réseau pilotable (sièges conducteur et passager, groupe motopropulseur, tableau de bord, vue libre) ; l'outil de nettoyage d'administration peut désormais supprimer les véhicules et les caisses de dépôt.
- **Objets** : Ajout d'un outil de nettoyage pour les administrateurs : un rayon partant de la main du joueur, une ligne de visée rouge/jaune, cliquez pour supprimer l'élément ciblé (rocher/boîte/dépôt uniquement).
  Suppression autorisée par le serveur : libère le nœud (ou le transfère à Horizon) -> supprimé de GORC et de la base de données. L'infrastructure du monde est protégée.
  Les outils 1 (perforateur) et 2 (nettoyage) sont désormais incompatibles.
  L'emplacement réservé au dépôt minier génère sa copie réseau sur le serveur de jeu (logique de collision et de collecte/envoi), avec un UUID déterministe (optionnel :
  stable_id) pour éviter l'accumulation de doublons ; placé dans Sandbox Capital.
- **Interface** : Appuyez sur F6 pour enregistrer l'écran de jeu (report de bug ou clips) ; les enregistrements sont sauvegardés en AVI dans Documents/DyingStar/records.
- **Minage** : Add a mining depot: deposit mined ore, refine it by volume (ore purity, stock and per-crate fill shown on the depot screen) and extract a carryable crate of ore.
- **Minage** : Les rochers miniers montrent désormais leur minerai : quelques petites traces en surface, et la vraie quantité se révèle en cassant le rocher — les morceaux les plus riches contiennent plus de minerai.

### Changed

- **Véhicules** : Les passagers comptent dans la charge du véhicule (SURCHARGE).
- **Objets** : Les objets portés sont solides pour le monde et les autres joueurs (pas pour le porteur).
- **Véhicules** : Les passagers assis ajoutent leur poids (75 kg) à la charge et au poids total ;
- **Véhicules** : SURCHARGE prend en compte passagers + chargement de la benne.
- **Interface** : L'interface du véhicule est désormais en anglais.
- **Performances** : Réduction du calcul de collision de 50 fois (testé sur 200 boites et rochers)
- **Véhicules** : Fluidification des véhicules et des joueurs en réseau (interpolation côté client), et possibilité pour l'outil de nettoyage d'administration de supprimer les véhicules et les caisses de dépôt.

### Fixed

- **Véhicules** : Le chargement posé en benne ne disparaît plus en multijoueur.
- **Véhicules** : Un véhicule ne peut plus être chargé dans la benne d'un autre véhicule.
- **Véhicules** : Un siège de véhicule se libère quand son occupant se déconnecte.
- **Véhicules** : Conduite plus fluide : plus de tremblement de caméra une fois assis, et le camion bouge de façon lisse pour tout le monde (conducteur compris).
- **Véhicules** : Message « Driver seat taken » quand le siège conducteur est occupé ; l'invite pour monter ne s'affiche plus quand on est déjà assis. On ressort à côté du siège utilisé.
- **Véhicules** : Correction : le chargement ne disparaît plus quand on le pose dans la benne en multijoueur.
- **Objets** : Correction du problème de disparition des objets transportés (caisses, minerai) pour les autres joueurs au fil de la distance.
- **Objets** : Corrige le problème des collisions fantômes laissées par l'outil de nettoyage d'administration après la suppression d'un élément.
- **Minage** : Unify how player and prop properties replicate to nearby players, and fix mining rocks sometimes appearing at the world origin.

## [0.1.0-dev.202606072359] - 2026-06-07

### Added

- **Minage** : E** pour **porter** ou **lâcher** un minerai (un seul à la fois).
- **Minage** : Extraction minière V0 : équipez-vous d'un perforateur, visez les failles prédéfinies d'une roche et forez pour la briser en morceaux, visible et synchronisé en multijoueur
- **Interface** : Ajout d'un bouton dans l'UI de pause pour retourner au menu (déconnexion du serveur)
- **PlanetTech** : Ajout du téléchargement des données planète pour le build et en local pour les développeurs

### Changed

- **Minage** : Seul un minerai **entièrement miné** (sans faille) est portable ; impossible de prendre celui d'un autre joueur.
- **Minage** : Porter **ralentit**, le minerai **flotte devant** soi (sans collision) et **tout est visible des autres joueurs**.
- **Minage** : Le **perforateur** est toujours là : **rangé** par défaut/pendant le port, **sorti** quand on l'équipe.
- **Minage** : Voir https://github.com/DyingStar-game/DyingStar/pull/186
- **Serveur** : Amélioration des messages d'erreur du serveur
- **Serveur** : Mise à jour vers dotnet 9, suppression de la page de connexion (auth par JWT)
- **Audio** : Suppression de Wwise, remplacé par l'audio natif Godot
- **Interface** : Révision de l'interface et des paramètres : son, livekit (proximité vocale)

### Removed

- **Joueur** : Supprime également la caméra à la troisième personne (F4) qui entrait en conflit avec l'extraction minière basée sur la visée

### Fixed

- **Joueur** : Correction du pseudo sur le joueur et le parent lors du changement de parent (correctif serveur et client)
- **Bâtiments** : Correction du spawn dans les appartements
- **Serveur** : Correction du crash sur le jeu compilé (mauvaise version dotnet)
- **Serveur** : Correction de la suppression du joueur à la déconnexion

## [0.1.0-dev.202605312359] - 2026-05-31

### Added

- **Bâtiments** : Gestion du spawn dans les appartements

### Fixed

- **Graphismes** : Correction de la lumière de l'univers
- **Serveur** : Correction du serveur Godot (nombreuses erreurs)

## [0.1.0-dev.202605102359] - 2026-05-10

### Added

- **Serveur** : Ajout du build du jeu dans GitHub Actions
- **PlanetTech** : Planet tech v1

### Changed

- **Serveur** : Installation du runtime dotnet dans le docker serveur
- **Serveur** : Réécriture du code pour les joueurs hors zone serveur
- **Serveur** : Mise à jour Godot 4.6.1
- **Serveur** : Mise à jour du docker pour le build serveur
- **Serveur** : Nouvelle architecture

### Fixed

- **Serveur** : Correction des logs dans /tmp (crash sur Windows)
- **Serveur** : Correction du déploiement SSH
- **Serveur** : Correction du build et du déploiement
- **Serveur** : Correction de Wwise pour le serveur dédié

## [0.0.1-test5] - 2025-12-16

- Version pour le test5
