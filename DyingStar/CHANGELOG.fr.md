# Changelog

Toutes les modifications notables du projet sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

- Les autres planètes et lunes montrent désormais leur atmosphère de loin : un monde voilé paraît plus clair, un air épais plus pâle ou plus blanc, et le bord de l'air s'illumine quand il est assez grand à l'écran.
- ajoute de la connection client au service de jeux
  ajout du service social
  ajout du service economie
  ajout du service mission
  ajout du service inventory
  ajout du service market
  création d'une interface (F3)  avec des application qui appel ces service
  init du code pour que le server godot puisse s'authentifier sur keycloak pour acceder a des api interne des services
- Les planètes et lunes vues d'orbite sont désormais entièrement éclairées : plus de carrés noirs sur les régions rocheuses ou herbeuses, ni de quadrillage dans l'air des mondes voilés.
- Corrigé : la lumière du soleil ne suivait plus l'heure ni le trajet une fois assis dans un véhicule, et sautait à la sortie.
- Une courte liste à gauche de l'écran montre les touches utiles du moment — à pied, au volant, en portant, foreuse en main — et apprend : chaque ligne disparaît une fois sa touche utilisée, puis les suivantes (limiteur de vitesse, allure de marche, roulis…) arrivent après les bases.
  La carte stellaire affiche ses commandes de la même façon, à sa gauche.
  Composants de véhicule : « Installer » s'affiche en vert, « Enlever » en jaune, et chaque invite d'interaction repose sur un fond sombre qui la garde lisible.
  Un volume à part pour la musique du menu (Paramètres > Audio), et la musique ne se coupe plus net en arrivant dans une ville.
  Accélérer et ralentir au volant ont leurs propres commandes configurable à lamanette : on peut les mettre sur les gâchettes de la manette sans changer les actions à pied.
- On monte dans un véhicule en regardant le siège, plus besoin d'être dans la zone, qui interférait parfois avec les composants et la benne
  Une porte de véhicule restée ouverte claque toute seule au-delà d'une certaine vitesse — plus tôt dans un air épais, plus tard sur les plateaux.
  Chaque planète et chaque lune dotée d'une atmosphère a maintenant son propre ciel basé sur les calculs de physique des matériaux, gazs présents, taille etc...
- fix crash du jeu dans certaines conditions
- Le camion n'a plus de lumière dans sa cabine.
- Carte stellaire : cliquer sur une planète, une lune ou un point d'intérêt affiche de nouveau sa fiche.
- Les conteneurs reposent désormais sur des aires de stockage aplanies dans les villages miniers et les villes-usines, et ne flottent plus ni ne s'enfoncent dans les pentes.
  Les lampadaires, projecteurs et enseignes néon s'allument quand il fait sombre, plus seulement au coucher du soleil : dans les vallées sous le voile de corindon, ils s'allument en plein jour.
  Projecteurs plus lumineux.
- Les villages miniers reçoivent des parcs à conteneurs, empilés jusqu'à trois, et des bennes à minerai.
  Villes-usines : zones industrielles avec dépôts miniers, dépôts de fret, garages, deux téléporteurs et parcs à conteneurs.
  Les conteneurs portent le logo ARES et gardent leurs détails bien plus loin.
- Chaque village minier a sa cabine de téléportation, et la station orbitale retrouve la sienne.
  La téléportation vers la station orbitale fonctionne de nouveau.
  Les bâtiments des villages portent des enseignes néon (garage, téléporteur, dépôts de fret et minier), dans votre langue.
  Lampadaires, projecteurs et enseignes s'allument au crépuscule et s'éteignent à l'aube, l'un après l'autre.
  Les villages miniers reçoivent projecteurs, lampadaires et caisses ; les groupes électrogènes des projecteurs ronronnent.
  Les caisses moyennes ne se portent plus à la main, et l'invite « Porter » n'apparaît que sur ce qu'on peut porter.
- Le faisceau de votre lampe torche n'est plus coupé par l'ombre de vos propres épaules.
- fix(vehicle) : plus de crash serveur sur une batterie supprimée
  batteries() et l'affichage véhicule ignorent une batterie déjà supprimée.
  L'écran de bord ne tourne plus sur le serveur, ce qui supprime aussi le spam « String formatting error ».
  fix(vehicle) : une pièce montée ne collisionne plus avec son camion
  La pièce (batterie, moteur) exclut la collision avec son camion dès sa création, ce qui supprime l'envol du camion au changement de serveur.
  fix(server) : un camion qui change de serveur continue de rouler
  À la frontière, le camion reçu reprend son état et sa vitesse. Ce n'est pas fait au chargement depuis la base.
  La vitesse est appliquée dès que le camion n'est plus figé, dans la limite de 1,5 s.
  Une copie restée active est adoptée, ce qui supprime le retour en arrière du conducteur.
  Le gel « pas de sol » est levé à l'adoption.
- Nouvelle aide des commandes : F1 (ou maintenir View à la manette) affiche vos touches et ce que fait chacune.
  Le camion se démarre et se coupe à toute vitesse, et son régime suit maintenant ses roues.
  Les composants d'un véhicule ne peuvent plus être retirés moteur allumé.
  Corrigé : le personnage pouvait continuer à monter une pente après avoir relâché la touche.
  Corrigé : les captures prises après avoir redimensionné la fenêtre étaient coupées.
  Corrigé : en AZERTY et autres dispositions, l'aide F1 allumait la touche du micro au mauvais endroit.
  Dev : les touches + / - de l'heure changent à nouveau l'heure instantanément.
- Nouvel écran Crédits dans le menu principal et le menu pause : toutes celles et ceux qui ont fait les musiques, sons, modèles et textures du jeu, en défilement comme un générique de film, sur une musique de la communauté.
  Les pas sur le sable, la terre et le gravier jouent un son provisoire pour l'instant (leurs sons n'avaient pas de source connue).
  Chaque musique de l'écran Crédits a un bouton pour l'écouter.
  Dix nouvelles musiques : dans l'espace, en pleine nature, au menu, et dans les villages miniers et usines, jusqu'ici sans musique. Les morceaux dont on ne connaît pas l'auteur le disent dans les crédits : si l'un d'eux est à toi, contacte-nous sur Discord.
- nouveau système lors de la création d'un nouveau serveur (maillage de serveurs dynamique) et transfert des objets et des joueurs vers ce nouveau serveur
- Si ton corps sort de l'arbre de scène pendant un transfert, il est remis sous le camion recréé (sinon sous la planète).
  Tu es rassis au volant et la caméra revient sur toi. Tu ne vois plus à travers les yeux d'un autre joueur.
  Le siège est libéré avant d'effacer un conducteur transféré, et son corps est retiré du camion.
  Le camion est détruit au moins 2 frames physiques après son conducteur, et sorti de l'espace physique avant. Ça doit corriger les crashs du serveur Godot.
  Le conducteur enregistré en base est maintenant l'occupant réel du siège. Un conducteur parti est effacé au bout de 10 s
- ajout du garage
- Nouveau : la batterie T1. Le camion roule désormais à l'énergie : il ne démarre pas sans batterie chargée, et la batterie se vide selon l'effort des moteurs (les pentes et les lourdes charges la vident plus vite).
  Un camion utilise une batterie à la fois et passe à la suivante quand elle est vide ; la batterie en service ne peut pas être retirée moteur allumé.
  Chaque batterie affiche sa charge (en kWh) sur ses flancs, et le tableau de bord du camion montre une barre par batterie avec son pourcentage (vert, orange, rouge).
  Les camions sortent désormais d'usine avec deux moteurs T1 et une batterie T1.
  Les batteries peuvent être apparues avec la roue d'apparition.
  Nouvelles musiques : « Balade » (LRC), « A starry night » et « Meloncholia » (Koothka), « EVA Atmo 1 » (Solstium), « Syd where are you » (spaceman), en EVA, en station spatiale et en pleine nature.
- Carte stellaire : toutes les commandes (clic, double-clic, clic droit, clic molette, molette, manette) sont réassignables dans Paramètres > Contrôles, et la ligne d'aide en bas de la carte affiche vos propres touches.
  Carte stellaire : le bouton X de la manette réinitialise la vue.
  Carte stellaire : ses chiffres de debug passent dans le panneau de debug, avec leur propre case dans Paramètres > Debug.
  Les boutons de la souris sont nommés dans votre langue dans la page des contrôles.
  Plus de balancement de la caméra : la vue à la première personne reste stable en marchant, en courant, à l'arrêt ou en tournant sur place, et descend toujours quand vous vous accroupissez ou vous couchez.
  Le camion a une plaque d'immatriculation.
  Les moteurs remis dans un camion restent dans leur baie après un redémarrage du serveur.
  Le OK de la fenêtre « Manette détectée » a l'allure d'un bouton.
  Nouvelle musique en pleine nature, par Plx.
  Chaque réglage de l'inspecteur Godot s'explique désormais au survol (pour les créateurs).
- Beaucoup moins d'à-coups à pied et en véhicule : le niveau de détail du terrain est désormais calculé en arrière-plan.
  Au premier lancement, le sol autour de vous apparaît en premier au lieu du paysage lointain.
  Voler vite (EVA) ne fige plus le jeu pendant des secondes le temps que le terrain suive.
  Plus de trous qui clignotent dans le sol devant vous quand vous avancez.
  Plus de gel du jeu quand vous vous éloignez d'une zone chargée.
  Le terrain se charge environ trois fois plus vite au premier lancement ou dans une nouvelle zone.
  En vol rapide, le sol nouveau est affiché avec moins de détails pour suivre votre vitesse ; le sol déjà vu reste détaillé, et le détail complet revient quand vous ralentissez.
  Correction d'un plantage quelques secondes après l'ouverture du menu principal au premier lancement.
  Le terrain que vous regardez arrive désormais en premier.
  Plus de long gel en ralentissant ou en arrivant sur un sol déjà vu.
  Décollage et arrêt plus fluides en vol rapide.
- Le terrain se charge environ trois fois plus vite au premier lancement ou dans une nouvelle zone : ses données sont désormais téléchargées par plusieurs connexions à la fois.
- Villages POI : le serveur crée les bâtiments d'un village et peut le réveiller quand Horizon demande des logements pour de nouveaux joueurs.
  Terrain : sur une pente, les bâtiments reposent bien sur leur plateau et le sol entre eux n'est plus en dents de scie.
  Perf serveur : le TPS remonte de 7 à 55 environ et les entrées des joueurs ne sont plus en retard.
  NPC bloqués : ils espacent leurs nouvelles tentatives, ce qui divise environ par 10 les requêtes de navigation.
  NPC en attente de route : ils passent en veille comme les NPC inactifs, pour économiser de la physique.
- Ajout d'un sous-sol et d'un escalier pour y accéder.
  Mise à jour de la scène de lumière "led_panel_1x0.3m.tscn" (notamment un ajustement de l'intensité lumineuse).
  Création d'une nouvelle scène de lumière "led_panel_1x1m.tscn".
- Fréquence d'images bien plus élevée dans une atmosphère : le ciel et le voile sont calculés avec une table précalculée au lieu d'une boucle par pixel (environ 41 → 70 FPS en Ultra sur une RTX 3090 au spawn).
  Les lampes des bâtiments ne clignotent plus : seules les plus proches projettent une ombre (les autres éclairent toujours), ce qui est aussi plus rapide la nuit.
  Moins d'à-coups réguliers dus à la rotation de la planète.
  Les tableaux de bord des camions et la StarMap sont dessinés que quand on les regarde.
  Mise à jour du menu avec la position des PNJ et des camions
- Si vous rencontrez des problèmes de perf, nouveau benchmark en jeu (Paramètres > Graphismes > Benchmark) : la vue tourne lentement sur place pendant que chaque option graphique est baissée tour à tour, puis vos réglages sont remis. Il écrit un rapport de ce que coûte chaque option sur votre machine (copié aussi dans le presse-papiers) à envoyer à WarpZone/KiFouine ; « Ouvrir le dossier » affiche les rapports.
- Support de la manette : jouer à la manette (disposition Xbox par défaut), réattribuer ses boutons dans Contrôles (colonnes Clavier / souris et Manette séparées), et les indications à l'écran suivent l'appareil utilisé.
  Les menus se pilotent à la manette : croix / stick pour se déplacer, A pour valider, B pour revenir, LB / RB pour les catégories, LT / RT pour la barre du haut.
  La carte stellaire affiche longitude, latitude et altitude sous le curseur près d'un astre.
  FPS / GPU affichés dans la rangée d'onglets des paramètres ; nouveau curseur de volume Interface.
  Menu Audio : nouveau slider pour changer le volume de l'interface
- Un corps planétaire attend sa collision avec le terrain avant de devenir dynamique.
- La musique change selon où vous êtes : menu, espace, points d'intérêt et lieux avec leur propre musique, avec des fondus entre les morceaux. Mise en place de l'architecture permettant l'ajout facile de nouvelles musiques.
  Nouveaux morceaux : Beyond the Horizon et Tin Can.
  Bruits de pas sur le métal.
  Contrôles : couper tout le son du jeu (N) et couper votre micro (M) apparaissent dans Contrôles > Général et peuvent être réattribués.
  Corrigé : N et M ne pouvaient pas être tapés dans les champs de texte, comme la recherche des touches.
  Paramètres : la ligne survolée est de nouveau visible, et le fond derrière les paramètres est plus sombre et s'estompe plus doucement.
  Le chat et le HUD sont masqués quand le menu pause est ouvert.
  Panneau de debug : une section Musique indique quel morceau joue et pourquoi.
- Trous devant le téléporteur : au village, les sommets du terrain n'étaient plus décalés vers la lèvre d'une fissure qui n'est pas creusée, et le terrain autour des bâtiments se rejoint à nouveau, en mesh comme en collision.
  Marche entre chunks : de chaque côté d'une frontière de tuile élaguée, les deux chunks lisent maintenant la même hauteur. La marche de 24,5 cm a disparu, en GDScript comme en C#.
  Cache disque des chunks : il est passé de v56 à v58, donc les anciens chunks troués ou décalés sont reconstruits.
- ajout de l'ESG (EntityStreamingGodot)
- Carte stellaire (F2) : les canyons sont maintenant visibles, en vrai relief près du sol et en bandes sombres vus de plus haut.
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
- Rework complet des menus
  Échap en jeu ouvre directement les paramètres, par-dessus le jeu.
  Nouveau réglage : taille de l'interface (Paramètres > Général).
  Les options de débogage ont leur propre onglet Debug.
  Les infobulles sont lisibles : fond sombre, texte à la ligne.
  La scène de réglage graphique disparaît : on voit le jeu à droite
  Corrigé : les menus ne se redimensionnaient pas en passant du mode fenêtré au plein écran.
- Corrigé : le jeu pouvait se figer en entrant dans l'univers depuis le menu principal.
  Corrigé : le décalage de l'horloge de dev restait actif à la connexion suivante.
- Le menu principal est maintenant une scène vivante sur Tarsis 3 au lever du soleil, avec un avant-poste, des ouvriers et des camions sur la route ; la caméra se déplace selon l'écran du menu. Désactivable dans Paramètres > Général.
  Une scène de réglage pour comparer les options graphiques sur le vrai terrain, à toute heure, depuis Paramètres > Graphismes ou l'accueil.
  Une barre de progression sur les écrans de chargement.
  Les menus tiennent dans une zone centrale 16:9 sur les écrans larges, et suivent le passage entre fenêtré et plein écran.
  Les boutons de l'accueil et du menu pause partagent le même style ; ceux de l'accueil sont sur une seule ligne.
- Les panneaux de débogage (Alt+²) forment maintenant un seul panneau à droite, sans chevauchement, qui regroupe les relevés du sol, du déplacement et du véhicule, et le nombre de chunks de terrain affichés.
  L'alerte d'horloge de dev apparaît désormais dans ce panneau.
- Nouvelles options graphiques : préréglages (détectés selon votre carte au premier lancement), mise à l'échelle FSR 1 / FSR 2.2, échelle de rendu, MSAA / FXAA / SMAA / TAA, qualité des ombres, SSAO / SSIL / SSR, halo lumineux, filtrage anisotrope, réduction du banding, qualité de l'atmosphère et du sol, et distances d'affichage du terrain / des bâtiments / de la végétation. Chaque option s'explique au survol.
  Un panneau graphique en jeu (Paramètres > Général) pour comparer les options en direct, avec FPS et temps GPU ; maintenir AltGr pour utiliser la souris.
  Les dossiers de captures et de vidéos s'ouvrent depuis le haut de Paramètres > Graphismes.
  Corrigé : maintenir AltGr faisait descendre en EVA ; les photos F7 montraient le panneau graphique.
- [Crevasses] Murs verticaux nets : diagonale des quads corrigée, portée du snap 1,6 pas, normales dédiées aux murs
  Bords organiques : méandres (domain warp) et bords rongés (fBm)
  [Crevasses] Hash entier à la place de sin : résultat identique au bit près sur toutes les plateformes
  [Crevasses] Jumeaux C# bit-exacts (TileFrameNative, CrackVoronoiNative)
  [volcans] Nouveaux types de pack : volcans (8), coulées de lave (9), fumerolles (10), dessinés dans QGIS
  [volcans] Volcans : 5 presets (strato, bouclier, caldera, cône de scories, dôme), lac de lave et panache côté client
  [volcans] Lave : ne remonte jamais les pentes (règle DESCENT), shader actif / en refroidissement / solide
  [volcans] Fumerolles : évents placés de façon déterministe, dépôts de gaz dans les couleurs de sommets
  [volcans] Suppression des anciens biomes volcaniques (script de migration fourni)
  [volcans] Le bord du cratère s'abaisse du côté de la coulée : la lave déborde de 2 m au lieu de creuser un canyon de 203 m
  [Performances ] Creusement des lignes en C# (GradeCarveNative) : 32 → 12 µs par appel
  [Performances ] Chunks sous une coulée de lave : de −30 à −50 % de temps de génération
  [Performances ] Passe des chunks périmés indexée : 200–440 ms → 1–5 ms (le 1–3 FPS près de la lave)
  [Performances ] Cache disque des chunks lu et écrit hors du thread principal : ~330 ms/s → < 7 ms/s
  [Performances ] Construction d'un chunk près d'une ligne : elle ne lit plus que le morceau de profil qui la concerne, au lieu de reparcourir toute la ligne (212 000 nœuds pour le rail en anneau). Le résultat est identique au bit près.
  [Performances ] Mémoire : les relevés de terrain tous les 5 m ne sont plus gardés une fois le profil calculé, soit ~140 Mo de libérés.
  [Performances ] Précalcul : un nouvel outil, tools/bake_grade_profiles.tscn, calcule une fois pour toutes les profils des lignes, les franchissements de crevasses et les tabliers de pont. Il les écrit dans grade_profiles.pack, que le jeu charge au démarrage : 827 ms au lieu de plusieurs minutes.
  [Performances ] Données périmées : si le bake ne correspond plus aux données (nouvel export, crevasses ou routes modifiées), le jeu recalcule lui-même et affiche un avertissement. Un test échoue, et link_modifiers.py rappelle la commande à relancer.
  [Performances ] Bug de performance corrigé : le cache des tuiles de modificateurs faisait un parcours linéaire, sous verrou, à chaque lecture de hauteur. Tous les threads s'attendaient les uns les autres, et c'était de pire en pire avec le temps.
  [Divers] limite de lint portée à 6 000 lignes, et deux nouvelles suites de tests (découpage des profils, bake).
- Nouveau : la Station orbitale Palaka-Pital, sur une vraie orbite autour de SandBox (400 km, 1 h 44 par tour), accessible par téléporteur avec une cabine à bord pour revenir, et des anneaux qui tournent pour donner de la gravité à leur plancher.
  Nouveau : une EVA avec une vraie inertie : roulis (A/E), monter/descendre (Espace/Ctrl), frein (X), un onglet EVA dans les touches, une animation de flottement, et la dérive orbitale près d'une station.
  Modifié : `action` passe de E à F, et la touche `interact` séparée disparaît : F ne fait qu'une chose à la fois.
  Nouveau : la carte stellaire montre les stations et un cône de vue, et s'ouvre sur vous la première fois et après un voyage.
  Retiré : le bouton Retour du téléporteur.
  Corrigé : quitter l'atmosphère d'une planète ne vous envoie plus au milieu du système.
  Corrigé : une caisse portée à travers le téléporteur (ou le chargement d'un camion envoyé vers un autre astre) n'est plus supprimée et peut être posée.
- Amélioration des performances sur les segments
  Amélioration de la StarMap
  Ajout/correction de l'intégration continue pour les tests GUT
- Véhicules : direction progressive. Un appui bref ou maintenu sur les flèches tourne les roues petit à petit ; elles gardent leur angle quand on relâche, et se redressent doucement en roulant.
  Véhicules : limiteur de vitesse. T l'active ou le désactive, Alt + molette règle la limite par crans de 5 km/h. Affiché sur le tableau de bord : vert quand il est actif, rouge quand il retient le camion.
  Véhicules : compteur kilométrique sur le tableau de bord, conservé entre les sessions et les redémarrages du serveur.
  F7 prend une photo sans aucune interface ; F8 prend une capture avec les panneaux de débogage pour les rapports de bug. Les deux sont rangées dans le dossier screenshots du jeu et copiées dans le presse-papiers.
  Les enregistrements F6 sont désormais rangés dans screenshots/records.
  Réglages › Vidéo : un bouton ouvre la galerie de captures.
  Corrigé : une touche souris avec modificateur (ex. Alt + molette) perdait son modificateur une fois remappée.
  Corrigé : panneaux de débogage affichant « Soon™ » juste après leur activation.
- Amélioration de la StarMap. Les planètes ont leur biomes, leur reliefs, leur ville, villages, gare, routes etc....
- Modification de la route pour qu'elle ne dépasse pas une pente de 10 degrés.
- L'interface en jeu est désormais traduite en anglais et en français. Les invites d'interaction affichent la touche réellement configurée, selon votre disposition de clavier, au lieu d'une touche figée.
- Les menus sont désormais entièrement traduits en anglais et en français. Les touches sont regroupées par familles (Général, À pied, En véhicule, En vol, Débogage), et les lignes de réglages se surlignent au survol.
- Gestion du snap à la surface de la planète + mise à jour du mesh de terrain dans l'éditeur et runtime
- Les objets posés sur une planète se fondent désormais dans le sol : la couleur et la texture du terrain remontent sur la base des bâtiments, rochers, caisses et props, avec une limite irrégulière façonnée par le vent. Les murs intérieurs et les surfaces horizontales restent propres, et la frange est éclairée comme le sol qu'elle imite. Elle ne s'assombrit donc pas contre un mur à l'ombre.
- Ajout d'un choix de langue (Automatique / Anglais / Français) dans Paramètres ▸ Général, appliqué immédiatement et conservé d'une session à l'autre.
- S'approcher d'un écran n' "aspire" plus votre regard en mode sticky. Vous pouvez désormais déplacez le pointeur contre le bord de la fenêtre pour balayer un écran trop large, la vue reste stable pendant la lecture, et taper dans un champ ne déclenche plus les touches de jeu . Échap rend le clavier. Les panneaux ne se redessinent plus que lorsqu'ils sont visibles, et une touche frappée va à la console utilisée, non à tous les écrans du monde (oupsy)
- Le téléporteur et la carte du système affichent de nouveau la liste des planètes dans les builds exportés.
- Le HUD de debug des véhicules affiche désormais la pente sur laquelle vous êtes, à côté des stats que vos moteurs peuvent franchir. Les composants de véhicule portent le pictogramme et numéro de série de ce qu'ils sont,  lisible des deux côtés du camion, et du dessus quand la pièce est posée au sol.
- Les pas sur le sable et la pierre ont enfin leur son, au lieu d'un marqueur d'erreur. Les pas sur le métal jouent toujours ce marqueur, en attendant un son sous licence libre.
- Fix le problème lié au siège du véhicule.
  Fix du dispositif de sécurité du véhicule : il semble ne pas monter suffisamment au-dessus du chunk lorsqu'il passe en dessous.
- optimistions joueur quand on a beaucoup de joueurs près de nous
- Impuretés rocheuses : couleur et minerai issus de la montagne pour chaque corindon
  Mise à jour des montagnes pour intégrer des canyons dans les zones de corindon ; correction des bordures des canyons et raccordement à la base des montagnes
- Les véhicules sont mus par des moteurs qu'on peut voir. Le moteur T1 est un objet qu'on ramasse, qu'on porte et qu'on boulonne dans l'une des quatre trappes du camion — et ce qui est installé détermine sa force de traction, la pente qu'il franchit et son accélération. Retirez-en un et le camion s'essouffle ; retirez-les tous et il ne démarre plus. Une nouvelle option des réglages masque le tableau de bord du conducteur.
- Ajout d'une cabine de téléportation pour les tests : on choisit un système, un corps et un point
  d'intérêt sur son écran, ou on saisit une longitude, une latitude et une hauteur, et on est posé au
  sol à cet endroit. Les véhicules garés dans la cabine et les joueurs qui s'y trouvent voyagent avec
  vous, et RETOUR ramène au point de départ. Corrige aussi un défaut préexistant qui faisait
  disparaître un véhicule pour le passager qui venait d'en descendre. Remplace les sept anciens pads fixes. Limite connue :
  descendre du véhicule avant de sauter — la vue et les commandes d'un passager assis peuvent ne pas
  survivre au trajet.
- [serveur] Augmentation du nombre d'objets gérés dans Jolt
  [serveur] Ajout une sécurité pour les véhicules (similaire à celle des joueurs)
  [serveur] Correction stdout
- Ajout des montagnes
- Cache de fichiers atomique pour le server meshing dynamic  (mesh de collision pour le serveur)
- Problème : 50 à 90 PNJ marcheurs faisaient tomber le serveur à 5 fps. Chaque PNJ bakait son propre navmesh (parse de toute la planète sur le main thread, bake Recast à 0,1 m, re-bake tous les 18 m).
  Cache navmesh partagé (NpcNavCache) : tuiles de 72 m sur un treillis, une map par bloc de 5×5 cellules pour que les routes traversent les tuiles ; géométrie collectée par requête physique et extraite sur un worker ; TTL, invalidation, éviction ; les camions garés creusent le mesh.
  PNJ allégés : tick à 30 Hz entrelacé, sous-arbres inutiles désactivés côté serveur (UI, outil de minage, rayons, NavigationAgent3D), réplication seulement quand la pose change.
  Coûts annexes réduits : props statiques et véhicules garés à 6 Hz, anneaux HEALPix des pins mis en cache, balayage des pins cadencé au temps, planificateur de minage sans les PNJ.
  Rig de perf serveur ([debug] perf=true) : anatomie de la frame ([Perf/frame]), attribution par script ([Perf/bands], opt-in), recensement des nœuds, messages Horizon, ventilation du tick PNJ — chacun de ces postes a été trouvé grâce à lui.
  Mesuré : 47 PNJ → de 5 fps / 43 TPS à 60 / 60 ; 93 PNJ → 60 TPS.
- Correction d'un problème de « chunk »
  Correction du maillage de sécurité du joueur pour les tunnels
  Optimisations : évitement du rendu des rails et des routes trop éloignés et invisibles
  Correction du sol du tunnel
- Autoroute en relief
  Correction : activation des éléments de débogage
  Correction : tuiles hexagonales sur les cartes AMD
- PlanetTech avec routes, exportation QGIS, refactorisation
- Correction de la vue passager trop basse en véhicule : les poses conducteur et passager ne placent pas la tête au même endroit, et chacune a désormais sa propre hauteur d'œil.
- Un joueur à bord d'un véhicule appartient désormais au repère de ce véhicule : le trajet est fluide pour le conducteur comme pour le passager, et sa position n'est plus renvoyée sur le réseau à chaque tick pendant que le véhicule roule.
- Éditeur uniquement : un bouton « Fly in planet frame » dans la barre d'outils de la vue 3D fait survoler un corps avec le haut toujours en haut et l'avance qui suit la courbure, au lieu de la caméra alignée sur le monde qui part de travers dès qu'on s'éloigne du pôle.
- Le panneau de debug affiche désormais l'altitude réelle au-dessus de la sphère de référence en plus de la hauteur au-dessus du sol, et les coordonnées du joueur continuent de se mettre à jour en véhicule.
- Correction du menu pause qui pouvait s'ouvrir par-dessus un jeu resté actif (la caméra continuait de tourner en dessous), de l'impossibilité de quitter Réglages > Contrôles avec Échap, et des étiquettes de nom qui restaient à hauteur d'homme debout quand le joueur était accroupi ou allongé. Les touches réassignées sont de nouveau appliquées au démarrage, et non plus seulement après avoir ouvert la page des contrôles. Échap annule désormais une réassignation de touche au lieu d'être assigné, et la touche de saut s'appelle « Jump / Vault ».
- Le dernier cran de la molette ne fait plus passer le personnage au petit trot : toute la plage reste une marche, jouée plus vite, et seul le sprint change de démarche.
- Un joueur assis dans un véhicule est désormais affiché assis pour tout le monde, y compris pour les joueurs qui se connectent ou qui s'approchent après qu'il se soit assis.
- Correction du blocage du client à 6 FPS : la taille de la file d'attente du micro LiveKit était exprimée en millisecondes et non en échantillons
  Ajout de code de débogage
- Amelioration du calcul des chunks de -26 a -66 %
- Utilisation des tuiles (points) sur un serveur web et utiisation en streaming.
- Amélioration du débogage des performances côté client
- La vue à la première personne ne dérive plus quand on regarde autour de soi, et on ne voit plus son propre cou en courant ou en tournant la tête.
- Les marches basses, bordures et escaliers se franchissent de façon fiable, y compris dans les portes et sous les plafonds bas où ils bloquaient.
- Les camions ne se retournent plus en virage serré, leurs roues bougent désormais avec la suspension pour tous ceux qui les voient, et leurs pneus s'entendent — ils crissent quand on braque sur place et roulent quand on prend de la vitesse. Le mini camion arrive avec un nouveau modèle et quatre bennes interchangeables.
- Correction des ponts
  Désactivation de l'apparition de ressources par le joueur
  Augmentation de la probabilité d'apparition de rochers sur un chunk de 70 % à 90 %
- Les utilisateurs peuvent activer le débogage des performances dans les journaux lorsqu'ils ont peu d'images par seconde.
- Les joueurs sont desormais representes par un vrai modele de personnage au lieu du mannequin provisoire, en conservant toutes les animations existantes. La lampe torche est fixee a la tete, son faisceau suit donc le corps.
- Correction de la détection des falaises : les parois raides sont désormais reconnues correctement
  partout, au lieu que tout l'hémisphère éclairé soit rendu comme une falaise et que de vraies parois
  verticales soient ignorées.
- La carte stellaire (F2) et les affichages de debug fonctionnent désormais assis dans un véhicule, et la carte est réellement modale : plus rien ne réagit tant qu'elle est ouverte, et le camion se met en roue libre au lieu de garder les gaz.
  Alt+L et Alt+I n'allument plus les phares et le moteur en même temps que leur outil de debug.
  Le franchissement et l'escalade se déclenchent maintenant en APPUYANT SUR SAUT devant un obstacle, au lieu de se produire tout seuls quand on marche dedans. Les marches et petits rebords se montent toujours automatiquement.
  Les bruits de pas et les caisses posées sonnent selon la surface — métal, sable, pierre, béton — au lieu d'un échantillon unique partout. Les caisses s'entendent à la prise et à l'impact.
  Le curseur de volume SFX agit enfin sur tous les sons du jeu, et le réglage propre à un son fonctionne même quand il vient de vos mains ou de vos pieds.
  Un camion dont une porte est restée ouverte ne vous éjecte plus quand vous essayez de vous y asseoir.
  On ne peut plus monter dans un véhicule les mains pleines, et monter range vos outils.
  Correction d'un démarrage du serveur de jeu sans aucun monde, qui laissait les joueurs immobiles.
- Sandbox est desormais le troisieme monde du systeme Tarsis, plus proche de son etoile et protegee par
  son voile de corindon ; Gaea prend la quatrieme orbite. Sandbox et ses lunes Korax et Xarok sont
  renommees en consequence.
- Fix la rotation joueur et joueurs sort de sa zone (gorc)
- Le ciel est désormais calculé à partir de l'atmosphère réelle de chaque monde — ses gaz, sa pression,
  sa poussière — au lieu d'un dégradé peint. Les couchers d'étoile, la couleur de l'éloignement et le
  voile sur les montagnes lointaines découlent tous de la même physique, et changent d'une planète à
  l'autre. Deux bugs qui éclairaient le monde la nuit, et donnaient aux bâtiments et aux sommets
  lointains un air rétroéclairé, sont corrigés.
- Limitation du nombre de threads pour le serveur pour améliorer les performances sur Kubernetes.
- Mise à jour de la version de Godot sur le serveur vers la 4.7 ; j'avais oublié d'utiliser la 4.7 comme pour le client ;(
- Correction du problème de chargement infini de la page
- Les performances du serveur près des villes sont nettement améliorées, et les joueurs comme les véhicules ne tremblent plus sur place.
  Les camions placés dans le monde apparaissent enfin, au lieu de traverser le sol sans que personne ait pu les voir.
  On ne traverse plus le sol de son habitation à la première connexion suivant un redémarrage du serveur.
  Les écrans 3D, comme celui du dépôt minier, sont de nouveau utilisables : le curseur ne tremble plus et ne revient plus se coller au milieu de l'écran, et les boutons se cliquent sur toute la surface.
  Emprunter un téléporteur s'affiche maintenant correctement pour les autres joueurs.
  Les planètes et les lunes du système Tarsis parcourent leurs véritables orbites, et une carte du système, sur F2, montre où se trouve chaque astre — et vous avec.
  Les nuits ont un ciel étoilé, et le crépuscule dure, en s'éteignant au-dessus du point où l'étoile s'est couchée.
  La roue de spawn de développement, l'outil de suppression d'objets et le vol libre EVA ne sont plus accessibles en jeu, et leurs raccourcis n'apparaissent plus dans les réglages de contrôles.
  Correction de la compilation et de la version. Le problème est désormais identique pour les clients Linux et Windows (essayez de corriger le lanceur et de mettre à jour le jeu).
  ajout de bornes kilométrique (posé à la main donc c'est du à peu près)
- La roue d'emotes (T) ne fait plus apparaître d'objet lorsque la roue de spawn (Alt+T) a été utilisée auparavant.
  Enchaîner les sauts en sprintant n'accumule plus une vitesse illimitée : un saut conserve l'élan qu'on avait au décollage.
  La marche, le sprint et l'accroupi se déplacent désormais aux vitesses décrites dans le document de design, et la vitesse de marche à la molette progresse régulièrement entre 0,5 et 3 m/s au lieu de faire des bonds.
  L'animation des personnages ne clignote plus entre la marche et le trot lorsqu'on se déplace à allure constante près d'un changement d'allure.
  Chat : maintenir TAB ne fait plus défiler les boutons de l'interface, et taper un message ne déclenche plus d'actions de jeu comme s'accroupir ou s'allonger.
  Chat vocal : couper son micro coupe réellement l'émission, et la voix n'est plus captée en double.
  Chat vocal : à plusieurs, toutes les voix sont entendues, et un joueur qui s'en va cesse d'être audible au lieu de persister ou d'être entendu deux fois à son retour.
- gestion des PNJ
  ajout des propsync (objet réseau)
- Franchissement automatique** : le personnage franchit les obstacles tout seul — vault par-dessus les bas, grimpe sur les rebords (y compris surélevés), et enjambe en douceur les petites marches qui bloquaient.
  Nouveaux sons** : les 3 types de vault, le perforateur (boucle de perçage, fin, raté, équiper/ranger), la torche du joueur, les phares du camion / moteur électrique.
  Écrans de cabine** des véhicules (rétroviseurs et tableau de bord) : éteints moteur coupé, rallumés à l'allumage.
  Spawn** : un écran « Spawning... » tient jusqu'à ce que le monde soit prêt — plus de flash de jour ni de caméra qui se redresse juste après l'apparition.
  Menu pause** : plus possible de bouger, agir, percer ou regarder autour tant qu'il est ouvert.
  Chat** : affiché par défaut, ordre des messages plus clair, lisible sur fond clair.
  Les icônes son/micro à l'écran sont en bas à gauche et plus petites.
- Les personnages ont un corps animé : vous voyez votre propre corps en 1re personne et les autres joueurs sont entièrement animés — marche/course/saut, accroupi (C) et allongé (W), pivot sur place, assis/conduite en véhicule, emotes (roue T) et port d'objets. Porter une caisse n'est possible que debout, et les outils rangés suivent le corps.
- 🌌 Système stellaire
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
- Correction du chat texte (connexion avec le serveur)
- Mise à jour des URL des serveurs vers la nouvelle infrastructure.
- Ajout de réglages Graphics pour activer/désactiver les ombres temps réel et régler la distance d'affichage des ombres du soleil (persistés, appliqués en direct).
- Correction d'un pic de charge CPU physique au démarrage du serveur : les props rechargés depuis la persistance ne recalculent plus tous leurs collisions d'un coup — ils repartent gelés et se réveillent à l'approche d'un joueur.
- Le portage d'objets est bien plus agréable : plus de « snap » dans les mains à la prise — l'objet rejoint la main en douceur et traîne quand on bouge, réagit aux chocs, et est solide tout de suite. Regarde en bas pour poser un objet au sol, en haut pour le placer en hauteur.
  Un objet porté ne te repousse plus, et lever la tête dans un container ne l'envoie plus sur le toit.
  La portée d'interaction est désormais une valeur configurable sur le joueur.
  Les nouveaux containers de stockage verrouillent toute caisse qui se pose sur leur sol (impossible à bouler) ; on la reprend pour la libérer.
- La roue de spawn de dev est désormais gérée par le serveur : les objets apparaissent devant vous, posés au sol et droits, et c'est le serveur qui décide où. La molette tourne un objet porté par paliers de 15°, et maintenir le clic molette permet de le faire pivoter librement sur tous les axes à la souris — le tout autour du centre de l'objet.
  Le dépôt de minerai n'est plus spawnable et empaquette son minerai dans une caisse de transport.
  Utiliser un écran 3D ne laisse plus votre caméra perdue dans l'espace.
  Les véhicules se braquent et freinent moteur éteint, et le moteur peut être coupé à toute vitesse.
  Dans le menu des paramètres, Échap fait maintenant « retour » au lieu de libérer la souris.
  Une caisse qui tombe ou est jetée dans la benne d'un camion est désormais pesée comme si elle avait été chargée à la main.
  On ne peut plus attraper un objet ni ouvrir une porte de véhicule à travers un mur de bâtiment.
  Les phares de camion plus lumineux et une famille de crashs client corrigée.
- Les joueurs ont du son : bruits de pas (échantillons aléatoires, cadence qui suit votre vitesse), interrupteur de la lampe torche et saut. Ils sont spatialisés et répliqués : vous entendez les joueurs autour de vous marcher, sauter et allumer leur lampe.
- Mise à jour des technologies planétaires. Génération de cartes de hauteur pour chaque niveau de détail. Correction du téléporteur vers une autre planète/un autre point.
  Sur le réseau, les planètes sont désormais des objets génériques.
- Les véhicules ont du son : portes, démarrage et coupure du moteur, un régime moteur qui monte avec les tours, un klaxon (H) et un klaxon spécial (Alt+H), frein à main et phares. Le moteur doit désormais être démarré avec la clé de contact (I), à l'arrêt, avant que le véhicule puisse rouler.
- Le modèle du mini-camion a été mis à jour (correction de l'axe de rotation des roues et de la zone de poids de la benne).
  Le menu pause ne se ferme plus lorsque vous cliquez dans le vide : utilisez la touche Échap ou le bouton Reprendre.
  Le changement de résolution d'écran nécessite désormais une confirmation sous 10 secondes et est automatiquement annulé en cas de non-respect de cette consigne. Ainsi, une résolution trop élevée ne peut plus vous bloquer.
- Les objets transportés interagissent désormais physiquement avec le monde : vous pouvez les heurter et les poser contre le sol, les murs et les véhicules, et les empiler en regardant vers le haut ou vers le bas pour lever ou abaisser un objet tenu. Un objet hors de portée (par exemple, coincé derrière un mur) est automatiquement lâché.
- Vous pouvez désormais afficher/masquer les panneaux de débogage à l'écran depuis Paramètres → Général, ou avec une touche réattribuable (par défaut Alt+²) disponible dans le menu Commandes.
- Camion : le volant tourne désormais dans le bon sens à une vitesse raisonnable, et l'image de la caméra de recul n'est plus inversée.
- La roue d'apparition des développeurs (T) est désormais un menu à deux niveaux (catégorie → variante)
  les caisses-palettes qu'elle génère peuvent être ramassées et transportées.
  Les conteneurs de test sont désormais sensibles aux collisions.
  Correction d'un bug : les portes des camions pouvaient refuser de s'ouvrir lorsqu'un élément de décor apparaissait à proximité, et le transport des caisses à distance normale est désormais possible
  les objets tenus en main flottent désormais un peu plus loin.
- Mise à jour de la physique à 60 FPS.
  Correction des collisions par chunk pour Jolt aux coordonnées astronomiques.
  Correction de l'exportation des données de terrain, de la validation du cache et de la mise en veille de la physique en cas d'inactivité.
- Mettre à jour les options d'exportation pour les planètes
- Correction du dossier de la planète et compilation
  Ajout de la maison Bardok pour les tests
  Ajout des conteneurs Kankan pour les tests
- Mise à jour de la planet tech, ajout de vallées, texture...
- Éditeur uniquement : ajout d'un outil DyingStar pour importer/exporter les props serveur d'une scène vers le startup_items.json d'horizonserver.
- Vous ne pouvez plus interagir avec quelque chose que vous ne pouvez pas voir : ramasser un objet nécessite désormais une ligne de vue dégagée, et une portière de véhicule ne s'ouvre par la poignée de votre côté (à l'extérieur à pied, à l'intérieur en position assise) que si elle n'est pas obstruée.
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
