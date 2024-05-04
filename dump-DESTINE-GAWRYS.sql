DROP TABLE IF EXISTS entreprise CASCADE;
DROP TABLE IF EXISTS jeu CASCADE;
DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS entreprise CASCADE;
DROP TABLE IF EXISTS appartient CASCADE;
DROP TABLE IF EXISTS joueur CASCADE;
DROP TABLE IF EXISTS est_ami_avec CASCADE;
DROP TABLE IF EXISTS achete CASCADE;
DROP TABLE IF EXISTS succes CASCADE;
DROP TABLE IF EXISTS obtient CASCADE;
DROP TABLE IF EXISTS commente CASCADE;
DROP TABLE IF EXISTS partage CASCADE;



CREATE TABLE entreprise (
id_entreprise serial PRIMARY KEY,
nom_entreprise varchar (100) UNIQUE,
pays varchar(35)
);


CREATE TABLE jeu (
id_jeu serial PRIMARY KEY,
titre varchar (51) UNIQUE,
prix int NOT NULL,
date_sortie date,
age_min int,
description text,
id_entreprise_dev int,
id_entreprise_edit int,
FOREIGN KEY (id_entreprise_dev) REFERENCES entreprise(id_entreprise),
FOREIGN KEY (id_entreprise_edit) REFERENCES entreprise(id_entreprise),
CONSTRAINT realage CHECK (age_min >= 0 AND age_min <= 18),
CONSTRAINT realprix CHECK (prix >= 0)
);

CREATE TABLE genre (
id_genre serial PRIMARY KEY,
nom_genre varchar (30) UNIQUE
);

CREATE TABLE appartient (
id_genre int,
id_jeu int,
FOREIGN KEY (id_genre) REFERENCES genre (id_genre),
FOREIGN KEY (id_jeu) REFERENCES jeu (id_jeu),
PRIMARY KEY (id_genre,id_jeu)
);

CREATE TABLE joueur (
pseudonyme varchar (35)  PRIMARY KEY,
motdepasse varchar(200) NOT NULL,
nom varchar (25) NOT NULL,
email varchar(150) UNIQUE NOT NULL,
date_naissance date NOT NULL,
argent int
);

CREATE TABLE est_ami_avec (
pseudonyme1 varchar (35),
pseudonyme2 varchar (35),
FOREIGN KEY (pseudonyme1) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE,
FOREIGN KEY (pseudonyme2) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE,
PRIMARY KEY (pseudonyme1,pseudonyme2)
);

CREATE TABLE achete (
pseudonyme varchar(35),
id_jeu int,
date_achat date,
FOREIGN KEY (id_jeu) REFERENCES jeu (id_jeu),
FOREIGN KEY (pseudonyme) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE,
PRIMARY KEY (pseudonyme,id_jeu)
);
CREATE TABLE succes (
id_succes serial PRIMARY KEY,
intitule varchar (50) UNIQUE,
description_succes text,
id_jeu_s int,
FOREIGN KEY (id_jeu_s) REFERENCES jeu (id_jeu)
);

CREATE TABLE obtient (
pseudonyme varchar(35),
id_succes int,
FOREIGN KEY (pseudonyme) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE,
FOREIGN KEY (id_succes) REFERENCES succes (id_succes),
PRIMARY KEY (pseudonyme,id_succes)
);

CREATE TABLE commente (
pseudonyme varchar(35),
id_jeu int,
note int,
commentaire text,
FOREIGN KEY (id_jeu) REFERENCES jeu (id_jeu),
FOREIGN KEY (pseudonyme) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE,
PRIMARY KEY (pseudonyme,id_jeu),
CONSTRAINT realnote CHECK (note >= 0 AND note <= 20),
CONSTRAINT unique_comment_par_jeu UNIQUE (pseudonyme, id_jeu)
);


CREATE TABLE partage (
pseudonyme1 varchar(35),
pseudonyme2 varchar(35),
id_jeu int,
FOREIGN KEY (id_jeu) REFERENCES jeu (id_jeu),
FOREIGN KEY (pseudonyme1) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (pseudonyme2) REFERENCES joueur (pseudonyme) ON UPDATE CASCADE ON DELETE CASCADE,
PRIMARY KEY (pseudonyme1,pseudonyme2,id_jeu)
);

INSERT INTO entreprise (nom_entreprise, pays) VALUES
('Sony Interactive Entertainment', 'Japon'), -- Ligne 1
('Microsoft Xbox', 'États-Unis'), -- Ligne 2
('Electronic Arts', 'États-Unis'), -- Ligne 3
('Ubisoft', 'France'), -- Ligne 4
('Activision Blizzard', 'États-Unis'), -- Ligne 5
('Valve Corporation', 'États-Unis'), -- Ligne 6
('Epic Games', 'États-Unis'), -- Ligne 7
('Take-Two Interactive', 'États-Unis'), -- Ligne 8
('Capcom', 'Japon'), -- Ligne 9
('Bandai Namco Entertainment', 'Japon'), -- Ligne 10
('Sega', 'Japon'), -- Ligne 11
('Bethesda Softworks', 'États-Unis'), -- Ligne 12
('CD Projekt', 'Pologne'), -- Ligne 13
('Konami', 'Japon'), -- Ligne 14
('Rockstar Games', 'États-Unis'), -- Ligne 15
('Cloud Imperium Games studio', 'États-Unis'), -- Ligne 16

('Bungie', 'États-Unis'), -- Ligne 17
('Turn 10 Studios', 'États-Unis'), -- Ligne 18
('Lionhead Studios', 'Royaume-Uni'), -- Ligne 19
('Moon Studios', 'Autriche'), -- Ligne 20
('RARE', 'Royaume-Uni'), -- Ligne 21
('Remedy Entertainment', 'Finlande'), -- Ligne 22
('Undead Labs', 'États-Unis'), -- Ligne 23
('Studio MDHR', 'Canada'), -- Ligne 24
('Insomniac Games', 'États-Unis'), -- Ligne 25
('Asobo Studio', 'France'), -- Ligne 26
('DICE', 'Suède'), -- Ligne 27
('Respawn Entertainment', 'États-Unis'), -- Ligne 28
('Maxis', 'États-Unis'), -- Ligne 29
('EA Vancouver', 'Canada'), -- Ligne 30
('Ubisoft Montreal', 'Canada'), -- Ligne 31
('Ubisoft Toronto', 'Canada'), -- Ligne 32
('Blizzard Entertainment', 'États-Unis'), -- Ligne 33
('Valve', 'États-Unis'), -- Ligne 34
('The Coalition', 'Canada'), -- Ligne 35
('Epic Games ST', 'États-Unis'), -- Ligne 36
('Visual Concepts', 'États-Unis'), -- Ligne 37
('Irrational Games', 'États-Unis'), -- Ligne 38
('Gearbox SoftwareS', 'États-Unis'), -- Ligne 39
('Hangar 13', 'États-Unis'), -- Ligne 40
('Firaxis Games', 'États-Unis'), -- Ligne 41
('Rockstar Studios', 'États-Unis'), -- Ligne 42
('Bethesda Game Studios', 'États-Unis'), -- Ligne 43
('CD Projekt Red', 'Pologne'), -- Ligne 44
('Kojima Productions', 'Japon'), -- Ligne 45
('PES Productions', 'Japon'), -- Ligne 46
('FromSoftware', 'Japon'), -- Ligne 47
('Ryu Ga Gotoku Studio', 'Japon'), -- Ligne 48
('Creative Assembly', 'Royaume-Uni'), -- Ligne 49
('Atlus', 'Japon'), -- Ligne 50
('Cloud Imperium Games', 'États-Unis'), -- Ligne 51
('Naughty Dog','États-Unis'),--Ligne 52
('Santa Monica Studio','États-Unis'),--Ligne53
('Sucker Punch Productions','États-Unis'),--Ligne54
('Guerrilla Games',' Pays-Bas'),--Ligne55
('Infinity Ward','États-Unis'),--Ligne56
('People Can Fly','Pologne'),--Ligne57
('Chair Entertainment','États-Unis'),--Ligne58
('Epic MegaGames','États-Unis'),--Ligne59
('Gearbox Software','États-Unis'),--Ligne60
('Turtle Rock Studios','États-Unis'),--Ligne61
('Capcom studio','Japon'),--Ligne62
('CyberConnect2','Japon'),--Ligne63
('Headcannon','États-Unis'),--Ligne64
('id Software','États-Unis'),--Ligne65
('Tango Gameworks','Japon'),--Ligne66
('Konami studio ','Japon'),--Ligne67
('Rockstar North','Royaume-Uni'),--Ligne68
('Larian Studios','Belgique');--Ligne 69


INSERT INTO genre (nom_genre) VALUES
('Action'), --l1
('Adventure'),--l2
('Role-Playing'),--l3
('Simulation'),--l4
('Strategy'),--l5
('Sports'),--l6
('Horror'),--l7
('Shooter'),--l8
('Fighting'),--l9
('Platform'),--l10
('Racing'),--l11
('Open World'),--l12
('Puzzle'),--l13
('MOBA'),--l14
('RPG'),--l15
('Survival'), --l16
('Super-héros'),--l17
('Tir a la 3 personne'),--l18
('Samourai'),--l19
('Mythologie'),--l20
('science-fiction'),--l21
('Metroidvania'),--l22
('Pirate'),--l23
('Difficile');--L24

INSERT INTO jeu (titre, prix, date_sortie, age_min, description, id_entreprise_dev, id_entreprise_edit)
VALUES

-- Sony
('The Last of Us Part II', 59, '2020-06-19', 18, 'Une aventure émotionnelle post-apocalyptique.', 52, 1),
('God of War', 49, '2018-04-20', 17, 'La renaissance épique du guerrier Kratos.', 53, 1),
('Spider-Man Miles Morales', 49, '2020-11-12', 13, 'Explorez New York avec le nouveau Spider-Man.', 25, 1),
('Uncharted 4 A Thief''s End', 39, '2016-05-10', 16, 'Chasse au trésor et aventure intense.', 52, 1),
('Ghost of Tsushima', 59, '2020-07-17', 17, 'Un récit de samouraïs et de combat.', 54, 1),
('Horizon Zero Dawn', 39, '2017-02-28', 13, 'Affrontez des machines dans un monde post-apocalyptique.', 55, 1),
('Spider-Man', 49, '2018-09-07', 13, 'L''araignée sympa du quartier se balance à travers New York pour sauver la ville.', 25, 1),
('The Last of Us', 39, '2013-06-14', 18, 'Une histoire émotionnelle de survie dans un monde post-apocalyptique.', 52, 1),
('God of War Ragnarok', 69, '2022-12-31', 18, 'Kratos se prépare pour un affrontement épique contre les dieux nordiques.', 53, 1),

-- Microsoft Xbox
('Halo Master Chief Collection', 39, '2014-11-11', 17, 'Compilation des jeux de la série Halo.', 17, 2),
('Forza Motorsport 7', 59, '2017-10-03', 3, 'Simulation de course automobile.', 18, 2),
('Fable III', 14.99, '2010-10-26', 17, 'Jeu de rôle d action.', 19, 2),
('Ori and the Blind Forest', 19, '2015-03-11', 7, 'Plateforme et aventure.', 20, 2),
('Sea of Thieves', 39, '2018-03-20', 12, 'Jeu d aventure en monde ouvert multijoueur.', 21, 2),
('Quantum Break', 39, '2016-04-05', 17, 'Jeu de tir à la troisième personne.', 22, 2),
('State of Decay 2', 29, '2018-05-22', 17, 'Jeu de survie en monde ouvert.', 23, 2),
('Cuphead', 19, '2017-09-29', 7, 'Jeu de plateforme run and gun.', 24, 2),
('Sunset Overdrive', 29, '2014-10-28', 17, 'Jeu d action en monde ouvert.', 25, 2),
('Microsoft Flight Simulator', 59, '2020-08-18', 3, 'Simulation de vol.', 26, 2),

--Electronic Arts
('Battlefield V', 39, '2018-11-20', 18, 'Tir intense à la première personne, plongeant les joueurs au cœur de la Seconde Guerre mondiale.', 27, 3),
('Star Wars Jedi Fallen Order', 49, '2019-11-15', 16, 'Plongez dans l univers de Star Wars.', 28, 3),
('The Sims 4', 40, '2014-09-02', 12, 'Construisez des maisons, établissez des relations et explorez des carrières passionnantes dans ce jeu de simulation de vie captivant.', 29, 3),
('FIFA23', 60, '2022-10-01', 3, 'Plongez dans l excitation du football.', 30, 3),

--Ubisoft
('Assassins Creed Valhalla', 60, '2020-11-10', 18, 'Explorez lâge des Vikings.', 31, 4),
('Far Cry 6', 60, '2021-10-07', 18, 'Affrontez le dictateur.', 32, 4),
('Watch Dogs Legion', 40, '2020-10-29', 18, 'Hackez et résistez dans un Londres dystopique.', 32, 4),
('Rainbow Six Siege', 40, '2015-12-01', 18, 'Une expérience tactique multijoueur intense avec Rainbow Six Siege.', 31, 4),

--Activision Blizzard
('Call of Duty Warzone', 0, '2020-03-10', 18, 'Plongez dans le champ de bataille en constante évolution.',56, 5),
('World of Warcraft Shadowlands', 0, '2020-11-23', 12, 'Explorez de nouvelles zones, affrontez des ennemis redoutables et découvrez une histoire captivante.', 33, 5),
('Overwatch', 0, '2016-05-24', 12, 'Jeu de tir en équipe où les joueurs choisissent parmi un large éventail de héros aux compétences uniques.', 33, 5),
('Diablo III Reaper of Souls', 20, '2014-03-25', 16, 'Partez en quête dâmes perdues et affrontez les forces démoniaques dans cet action-RPG.', 33, 5),

--Valve Corporation,États-Unis
('Half-Life 2', 19, '2004-11-16', 16, 'Un jeu de tir à la première personne révolutionnaire.', 34, 6),
('Counter-Strike Global Offensive', 14, '2012-08-21', 16, 'Jeu de tir compétitif en ligne.', 34, 6),
('Portal 2', 9, '2011-04-18', 12, 'Un puzzle-platformer avec une histoire captivante.', 34, 6),
('Left 4 Dead 2', 9, '2009-11-17', 17, 'Un jeu de tir coopératif de survie de zombies.', 34, 6),
('Team Fortress 2', 0, '2007-10-10', 17, 'Un jeu de tir multijoueur en équipe.', 34, 6),
('Dota 2', 0, '2013-07-09', 12, 'Un jeu de stratégie en ligne multijoueur.', 34, 6),
('Half-Life Alyx', 59, '2020-03-23', 16, 'Un jeu de réalité virtuelle dans l univers Half-Life.', 34, 6),
('Artifact', 19, '2018-11-28', 12, 'Un jeu de cartes à collectionner basé sur Dota 2.', 34, 6),
('Counter-Strike Source', 9, '2004-11-01', 16, 'Une version améliorée du légendaire Counter-Strike.', 34, 6),
('Half-Life', 9, '1998-11-19', 16, 'Le jeu qui a introduit le moteur Source.', 34, 6),

--Epic Games,États-Unis
('Gears of War 5', 59, '2019-09-10', 18, 'Un jeu de tir à la troisième personne dans l univers Gears of War.',35, 7),
('Bulletstorm', 29, '2011-02-22', 18, 'Un jeu de tir d action à la première personne.', 57, 7),
('Shadow Complex', 14, '2009-08-03', 16, 'Un jeu d action-aventure en 2.5D.', 58, 7),
('Infinity Blade', 5, '2010-12-09', 12, 'Un jeu d action épique pour appareils mobiles.',58, 7),
('Jazz Jackrabbit', 4.99, '1994-01-01', 7, 'Un jeu de plateforme classique.', 59, 7),

--Take-Two Interactive,États-Unis
('NBA 2K22', 59, '2021-09-10', 3, 'Le dernier opus de la célèbre franchise de jeux de basketball.', 37, 8),
('BioShock Infinite', 29, '2013-03-26', 17, 'Un jeu de tir à la première personne avec une histoire captivante.', 38, 8),
('Borderlands 3', 59, '2019-09-13', 18, 'Un jeu de tir en vue subjective avec des éléments de RPG.',60,8),
('Mafia III', 29, '2016-10-07', 18, 'Un jeu d action en monde ouvert se déroulant dans les années 1960.',40, 8),
('Civilization VI', 59, '2016-10-21', 12, 'Un jeu de stratégie au tour par tour.', 41, 8),
('Evolve', 19, '2015-02-10', 17, 'Un jeu de tir asymétrique en ligne.',61, 8),
('WWE 2K22', 59, '2022-03-11', 16, 'Le dernier jeu de la série WWE 2K.', 37, 8),


--Capcom,Japon
('Resident Evil Village', 59, '2021-05-07', 18, 'Un jeu d horreur et de survie à la première personne.', 62, 9),
('Resident Evil 3 Remake', 39, '2020-04-03', 18, 'Une réimagination du classique Resident Evil 3 Nemesis.',  62, 9),
('Resident Evil 2 Remake', 39, '2019-01-25', 18, 'Une réinterprétation du jeu classique Resident Evil 2.',  62, 9),
('Resident Evil 7 Biohazard', 29, '2017-01-24', 18, 'Un retour aux sources de l horreur dans la série Resident Evil.',  62, 9),
('Resident Evil 6', 19, '2012-10-02', 17, 'Une expérience d horreur-action mettant en vedette plusieurs personnages.',  62, 9),
('Resident Evil 5', 19, '2009-03-05', 17, 'Un jeu d horreur en coopération se déroulant en Afrique.', 62, 9),
('Resident Evil 4', 19, '2005-10-25', 17, 'Un jeu d horreur-action révolutionnaire.',62, 9),
('Resident Evil Outbreak', 14, '2003-12-11', 17, 'Un jeu d horreur en ligne avec plusieurs scénarios.',62, 9),
('Resident Evil Code Veronica', 14, '2000-02-03', 17, 'Un épisode classique de la série Resident Evil.',62, 9),
('Resident Evil 3 Nemesis', 9, '1999-09-22', 17, 'Un classique de l horreur avec le poursuivant implacable, Nemesis.',62, 9),
('Resident Evil 2', 9, '1998-01-21', 17, 'Le jeu qui a établi la formule classique de Resident Evil.',  62, 9),
('Resident Evil', 9, '1996-03-22', 17, 'Le jeu fondateur de la série Resident Evil.',  62, 9),
('Street Fighter V', 19, '2016-02-16', 13, 'Le dernier opus de la célèbre franchise de jeux de combat.',  62, 9),
('Monster Hunter World', 29, '2018-01-26', 16, 'Un action-RPG épique avec la chasse de monstres comme thème central.',  62, 9),


--Bandai Namco Entertainment,Japon
('Dark Souls III', 59, '2016-04-12', 17, 'Un action-RPG célèbre pour sa difficulté.', 47, 10),
('Dragon Ball Z Kakarot', 59, '2020-01-17', 13, 'Un RPG d action qui retrace l histoire de Dragon Ball Z.',63, 10),
('Elden Ring', 59, '2022-02-25', 18, 'Un RPG d action développé en collaboration avec Hidetaka Miyazaki et George R. R. Martin.', 47, 10),

--Sega,Japon
('Sonic Mania', 19, '2017-08-15', 3, 'Un retour aux racines de la série Sonic avec de nouveaux niveaux.',64,11),
('Yakuza Like a Dragon', 59, '2020-11-10', 18, 'Un RPG d action se déroulant dans l univers de la mafia japonaise.', 48, 11),
('Total War Three Kingdoms', 59, '2019-05-23', 16, 'Un jeu de stratégie en temps réel se déroulant en Chine.',49,11),
('Persona 5', 59, '2017-04-04', 17, 'Un RPG japonais acclamé avec des éléments de simulation de vie.',50, 11),

--Bethesda Softworks,États-Unis
('DOOM (2016)', 19, '2016-05-13', 18, 'Le redémarrage de la série DOOM, offrant un intense gameplay de tir à la première personne.',65,12),
('DOOM Eternal', 59, '2020-03-20', 18, 'La suite du DOOM (2016) avec encore plus de démons à éliminer et de niveaux à explorer.',65,12),
('DOOM 3 BFG Edition', 19, '2012-10-16', 18, 'Une édition améliorée de DOOM 3 avec des contenus supplémentaires.',65,12),
('DOOM (1993)', 4, '1993-12-10', 16, 'Le jeu qui a donné le coup d envoi à la série, offrant un gameplay révolutionnaire pour l époque.',65,12),
('DOOM II Hell on Earth', 4, '1994-09-30', 16, 'La suite du DOOM original avec de nouveaux niveaux et ennemis.',65,12),
('Starfield', 59, '2023-11-01', 18, 'Un jeu de rôle en monde ouvert situé dans l espace, développé par Bethesda Game Studios.',43,12),
('The Elder Scrolls V Skyrim', 39, '2011-11-11', 17, 'Un RPG en monde ouvert épique.',43,12),
('Fallout 4', 29, '2015-11-10', 17, 'Un RPG post-apocalyptique en monde ouvert.', 43,12),
('The Evil Within', 19, '2014-10-14', 18, 'Un jeu d horreur psychologique créé par Shinji Mikami.',66,12),

--CD red projekt
('The Witcher 3 Wild Hunt', 29, '2015-05-19', 18, 'Un RPG d action en monde ouvert basé sur la série de livres de Andrzej Sapkowski.',44,13),
('Cyberpunk 2077', 59, '2020-12-10', 18, 'Un RPG en monde ouvert se déroulant dans un futur dystopique, développé par CD Projekt Red.',44,13),
('The Witcher 2 Assassins of Kings', 19, '2011-05-17', 18, 'Le deuxième opus de la série The Witcher.',44,13),



-- Konami
('Metal Gear Solid V The Phantom Pain', 29, '2015-09-01', 18, 'Un jeu d infiltration en monde ouvert, dernier opus de la série Metal Gear Solid.', 45, 14),
('Silent Hill 2', 9, '2001-09-24', 17, 'Un jeu d horreur psychologique acclamé, faisant partie de la série Silent Hill.', 67,14),
('Castlevania Symphony of the Night', 9, '1997-10-02', 13, 'Un jeu d action-aventure classique, considéré comme l un des meilleurs de la série Castlevania.',67,14),
('Metal Gear Solid', 9, '1998-10-21', 17, 'Le premier opus de la série Metal Gear Solid, marquant le début de l ère 3D pour la série.', 67,14),
('Suikoden II', 9, '1999-12-17', 13, 'Un RPG japonais classique avec un système de recrutement de personnages vaste.', 67,14),
('Contra Hard Corps', 4, '1994-08-08', 13, 'Un jeu de tir d action intense, faisant partie de la série Contra.', 67,14),

--Rockstar Games,États-Unis 
('Grand Theft Auto V', 29, '2013-09-17', 18, 'Un jeu d action en monde ouvert acclamé, avec une histoire complexe et des possibilités de gameplay variées.', 68,15),
('Red Dead Redemption 2', 59, '2018-10-26', 18, 'Un western épique en monde ouvert, développé par les créateurs de Grand Theft Auto V.',42, 15),
('Max Payne 3', 19, '2012-05-15', 18, 'Un jeu de tir à la troisième personne captivant avec une histoire sombre et des mécaniques de tir innovantes.',42, 15),
('Bully Scholarship Edition', 14, '2008-10-21', 13, 'Un jeu d aventure en monde ouvert se déroulant dans un lycée, où le protagoniste Jimmy Hopkins doit naviguer dans la vie étudiante.', 68, 15),
('L.A. Noire', 39, '2011-11-08', 18, 'Un jeu d enquête se déroulant dans les années 1940 à Los Angeles, mettant en vedette des enquêtes criminelles réalistes.',68, 15),
('Grand Theft Auto San Andreas', 14, '2004-10-26', 17, 'Un classique de la série GTA, se déroulant dans l état fictif de San Andreas.',68, 15),
('Grand Theft Auto IV', 19, '2008-04-29', 18, 'Une histoire sombre de crime et de corruption à Liberty City.', 68, 15),

--Cloud Imperium Games,États-Unis
('Star Citizen', 59, '2022-11-8', 18, 'Un jeu de simulation spatiale en monde ouvert avec une approche sandbox, offrant une expérience immersive dans l univers spatial.',51, 16),

-- A venir ?
('Grand Theft Auto VI', 150, '2023-12-5', 18, 'Le jeu de la décennie.',68,15),

-- Larian Studios
('Baldur''s Gate III', 60, '2023-08-3', 18, 'Un RPG au style unique récompensé du meilleur jeu de l''année 2023.',69,69);


INSERT INTO succes (intitule,description_succes,id_jeu_s) VALUES 
    ('Maître de la Survie', 'Survivez à toutes les rencontres difficiles sans utiliser de kits de soins.', 1),
    ('Liens Indestructibles', 'Complétez le jeu sans perdre aucun membre du groupe de survivants.',1),
    
    ('Forge Divine', 'Améliorez toutes les pièces de l ensemble d armure à leur niveau maximal.', 2),
    ('Héraut des Dieux', 'Accomplissez toutes les quêtes secondaires et collectez toutes les reliques mythiques.', 2),
    
    ('Voltige Virtuose', 'Parcourez lensemble de New York sans toucher le sol pendant plus de 5 minutes.', 3),
    ('Protecteur du Quartier', 'Éliminez tous les crimes dans chaque district de Harlem.', 3),
    
    ('Explorateur Intrépide', 'Découvrez tous les lieux secrets d Uncharted 4 A Thief s End.', 4),
    ('Maître de la Discrétion', 'Terminez une section entière sans être détecté dans Uncharted 4 A Thief s End.', 4),
   
    ('Ombre du Samouraï', 'Infiltration réussie de 5 camps ennemis sans être repéré dans Ghost of Tsushima.', 5),
    ('Maitre de la Katana', 'Débloquez toutes les compétences du katana dans Ghost of Tsushima.', 5),
   
    ('Ingénieur de la Nature', 'Créez et améliorez 10 types de pièges différents dans Horizon Zero Dawn.', 6),
    ('Survivant des Machines', 'Éliminez avec succès toutes les machines dangereuses dans Horizon Zero Dawn.', 6),
    
    ('Photographe Aérien', 'Prenez une photo en plein vol depuis le haut d un gratte-ciel dans Spider-Man.', 7),
    ('Le Tisseur de Toiles', 'Capturez toutes les photos emblématiques de Spider-Man à travers New York.', 7),
    
    ('Dernier Rayon d Espoir', 'Terminez The Last of Us sans utiliser de munitions à feu.', 8),
    ('Historien du Monde Post-Apocalyptique', 'Collectez tous les journaux et documents dispersés dans The Last of Us.', 8),
    
    ('Voyageur des Neuf Royaumes', 'Visitez chaque royaume au moins une fois dans God of War Ragnarok.', 9),
    ('Champion Divin', 'Vainquez tous les boss optionnels dans God of War Ragnarok.', 9);




INSERT INTO joueur (pseudonyme, motdepasse, nom, email, date_naissance, argent) VALUES
('player1', '$2b$12$rPMhATN.mz26kN3i2B.PA.bNB6KI7TvdgsABXC6Tk62MhVXkfTJyq', 'Doe', 'john@example.com', '1990-01-01', 10),
('player2', '$2b$12$RMIIOmYmWsgKqUT.v7Z6zOSNyZJKeSi6PBzx1nuJfCY0p2p/1HqH.', 'Doe', 'jane@example.com', '1992-03-15', 150),
('gamer123', '$2b$12$Jx7c1Vs9aCdOkgY7E2QbieUHgkB2Z0qTtdeSTDct793A9kN139RXi', 'Smith', 'alice@gmail.com', '1985-08-20', 200),
('proGamer', '$2b$12$3s4smA6yZAEadG7hGBkfu.VpiGwywL36WF3Z4SsqIMhOGd/25e9XC', 'Johnson', 'bob@yahoo.com', '1998-12-05', 120),
('gameMaster', '$2b$12$wgYRaOn9F6MfnVsuTyCcCOH4REG4S8zUWMzT2HeicBPDilOzTg3OC', 'White', 'eva@example.com', '1989-07-10', 10),
('playNow', '$2b$12$ei.parzmzJk5oJfOQ8nNpuZYlaOyX0CcIBLES.C9EDKD5uGnvPgVG', ' Brown', 'michael@hotmail.com', '1995-04-25', 90),
('onlinePlayer', '$2b$12$sMq1rRguU96VA.3h0t/4TeuWC0vaRqF5rpPJWBH8m3Yah8klKK45q', 'Green', 'sophie@gmail.com', '1987-11-30', 100),
('gamingFan', '$2b$12$LaOaqOvE5UPP/T0YMNVgeeUkLv08716Lc4MtVU0lbT3Gyt6lpFa5i', 'Turner', 'chris@yahoo.com', '1993-09-18', 13),
('gameAddict', '$2b$12$axk8M7Da.XMzuPJsm2rEIOFpVZAttMlT7ZRHgxW9hJCFCdhm3C6by', 'Davis', 'emily@example.com', '1986-06-22', 11),
('superGamer', '$2b$12$AtiDVFKTyy4j2LVC/mFA3.xSM0mil5kh8xqxC4Yju.MrFuQ8FV9de', 'Wilson', 'alex@gmail.com', '1991-02-14', 1),
('gameOn', '$2b$12$2IDcMK.w0EsJa35mSGlpkOgM20Yt7hak6kk/5fILXgyA0IZj17xnW', 'Robinson', 'mia@hotmail.com', '1997-10-08', 17),
('playerX', '$2b$12$Q89CksMZuetD22C2mtwzkOELuqO3UGxNBWwJD4VafmAD.vPFmu05K', 'Lee', 'daniel@example.com', '1984-12-12', 0),
('Xxx_DarkSasuke_xxX', '$2b$12$xjKohl2ODMVsiRoff.Jb6uc50asuawHj8DAF2EDsPyqoeAOsKYBLe', 'Hall', 'olivia@gmail.com', '1994-06-02', 0),
('gameMastermind', '$2b$12$kipm6txeFj.7nCKv.Kh5U.aL0FcldmDfNolx.qBZbg7mgAOnfuRCm', 'Taylor', 'william@yahoo.com', '1988-05-28',30),
('gameChanger', '$2b$12$5A5iFZiJYxY98cgPD.4tLOtiqhxHIqjkYgFntaW6f7pie2Dy5G5N.', 'Adams', 'ava@example.com', '1996-08-15', 156),
('playfulGamer', '$2b$12$ejdW1B4iDs2445KxWwtXrOcnrU1or1qxThDrZQZMr/1IEkMWBMqW.', 'Clark', 'henry@hotmail.com', '1999-04-10', 0),
('gamerGirl', '$2b$12$HM41aCFnKKChOl8gvs8zSu1UaPCUWmDLaGT7Te9eY1qbSASRSbaRS', ' Wright', 'sophia@gmail.com', '1985-03-03', 15),
('player3', '$2b$12$pihJvPNlQOrTtE5nprVPZOe6TNqcTqD2XzYtrmb2bDZ2FazxlSKpG', 'Harris', 'liam@example.com', '1992-07-21', 40),
('gameLover', '$2b$12$n46xAvkUpnA0CprIIlGZb.tNP0B1LA7MFS5j78ziPAyAi5tPTihfm', ' Martinez', 'emma@yahoo.com', '1989-09-09', 60),
('playHard', '$2b$12$02b.2Ei8apBUqcx50I0IXOySSeoObxpQA/OHeWSIrd.nF0lplEExe', 'Rodriguez', 'noah@hotmail.com', '1993-11-12', 70);
 

INSERT INTO obtient (pseudonyme,id_succes) VALUES 
('Xxx_DarkSasuke_xxX',1),
('Xxx_DarkSasuke_xxX',3);

INSERT INTO est_ami_avec(pseudonyme1,pseudonyme2) VALUES
('player1','player2'),
('gameOn','playerX'),
('gamer123','player1'),
('player1','Xxx_DarkSasuke_xxX');

INSERT INTO achete (pseudonyme, id_jeu, date_achat) VALUES
('player2',2,'2020-04-20'),
('gameMastermind', 4, '2022-12-15'),
('gameChanger', 7, '2022-11-20'),
('playfulGamer', 11, '2022-10-05'),
('gamerGirl', 13, '2022-09-12'),
('gameLover', 6, '2022-07-22'),
('playHard', 8, '2022-06-30'),
('player1', 10, '2022-05-10'),
('player2', 31, '2022-04-05'),
('gamer123', 3, '2022-03-15'),
('proGamer', 5, '2022-02-20'),
('playNow', 9, '2022-01-02'),
('onlinePlayer', 14, '2021-12-14'),
('gamingFan', 2, '2021-11-28'),
('gameAddict', 12, '2021-10-10'),
('superGamer', 7, '2021-09-15'),
('gameOn', 1, '2021-08-22'),
('playerX', 5, '2021-07-30'),
('Xxx_DarkSasuke_xxX', 3, '2021-07-05'),
('gameMastermind', 8, '2021-06-15'),
('gameChanger', 2, '2021-05-20'),
('playfulGamer', 14, '2021-04-05'),
('gamerGirl', 6, '2021-03-12'),
('gameLover', 1, '2021-01-22'),
('playHard', 1, '2020-12-30'),
('player1', 7, '2020-11-10'),
('player2', 9, '2020-10-05'),
('gamer123', 13, '2020-09-15'),
('proGamer', 10, '2020-08-20'),
('playNow', 4, '2020-07-02'),
('onlinePlayer', 5, '2020-06-14'),
('gamingFan', 12, '2020-05-28'),
('gameAddict', 15, '2020-04-10'),
('superGamer', 3, '2020-03-15'),
('gameOn', 6, '2020-02-22'),
('playerX', 8, '2020-01-30'),
('Xxx_DarkSasuke_xxX', 1, '2019-12-05'),
('Xxx_DarkSasuke_xxX', 80, '2019-12-06'),
('gameMaster', 101, '2023-12-05'),
('Xxx_DarkSasuke_xxX', 2, '2021-07-05'),
('Xxx_DarkSasuke_xxX', 5, '2021-07-05');

INSERT INTO commente (pseudonyme,id_jeu,note,commentaire) VALUES 
('playerX',5,20,'Quel jeu incroyable !'),
('playerX',8,19,'Le meilleur jeu de l"histoire. Tout simplement'),
('gameLover',1,8,'J"ai beaucoup aimé le premier, mais la suite n"est pas du tout au même niveau pour moi'),
('Xxx_DarkSasuke_xxX',80,0,'Ce jeu est moisi, N"Y JOUEZ PAS !!!!!');

INSERT INTO partage (pseudonyme1,pseudonyme2,id_jeu) VALUES
('player1','player2',7),
('player1','Xxx_DarkSasuke_xxX',10);



INSERT INTO appartient (id_genre,id_jeu) VALUES
(1,1),
(2,1),
(7,1),
(16,1),

(1,2),
(2,2),
(20,2),

(1,3),
(2,3),
(17,3),

(1,4),
(2,4),
(18,4),

(1,5),
(2,5),
(12,5),
(19,5),

(1,6),
(15,6),
(12,6),

(1,7),
(2,7),
(17,7),

(1,8),
(2,8),
(7,8),
(16,8),

(1,9),
(2,9),
(20,9),

(18,10),
(21,10),

(6,11),
(4,11),
(11,11),

(1,12),
(15,12),
(2,12),

(10,13),
(2,13),
(22,13),

(1,14),
(2,14),
(12,14),
(23,14),

(1,15),
(2,15),
(18,15),

(1,16),
(15,16),
(16,16),
(12,16),
(7,16),

(10,17),

(1,18),
(18,18),


(4, 19),
(18, 20),
(8, 20),
(1, 21),
(2, 21),
(21, 21),
(4, 22),
(4, 23),
(6, 23),
(1, 24),
(15, 24),
(12, 24),
(20, 24),
(1, 25),
(2, 25),
(12, 25),
(18, 25),
(1, 26),
(2, 26),
(12, 26),
(1, 27),
(5, 27),
(18, 27),
(8, 27),
(18, 28),
(8, 28),
(15, 29),
(18, 30),
(17, 30),
(8, 30),
(1, 31),
(15, 31),
(18, 32),
(21, 32),
(18, 33),
(8, 33),
(13, 34),
(18, 34),
(21, 34),
(18, 35),
(16, 35),
(7, 35),
(18, 36),
(8, 36),
(1, 36),
(14, 37),
(18, 38),
(21, 38),
(5, 39),
(18, 40),
(8, 40),
(18, 41),
(21, 41),
(18, 42),
(1, 42),
(18, 43),
(1, 43),
(1, 44),
(2, 44),
(10, 44),
(1, 45),
(15, 45),
(10, 46),
(6, 47),
(4, 47),
(1, 48),
(2, 48),
(18, 48),
(1, 49),
(15, 49),
(18, 49),
(1, 50),
(2, 50),
(12, 50),
(5, 51),
(4, 51),
(18, 52),
(1, 52),
(6, 53),
(4, 53),
(16, 54),
(7, 54),
(1, 54),
(13, 54),
(16, 55),
(7, 55),
(1, 55),
(13, 55),
(16, 56),
(7, 56),
(1, 56),
(13, 56),
(16, 57),
(7, 57),
(1, 57),
(13, 57),
(16, 58),
(7, 58),
(1, 58),
(13, 58),
(16, 59),
(7, 59),
(1, 59),
(13, 59),
(16, 60),
(7, 60),
(1, 60),
(13, 60),
(16, 61),
(7, 61),
(1, 61),
(13, 61),
(16, 62),
(7, 62),
(1, 62),
(13, 62),
(16, 63),
(7, 63),
(1, 63),
(13, 63),
(16, 64),
(7, 64),
(1, 64),
(13, 64),
(16, 65),
(7, 65),
(1, 65),
(13, 65),
(9, 66),
(1, 67),
(15, 67),
(1, 68),
(15, 68),
(24, 68),
(1, 69),
(15, 69),
(12, 69),
(1, 70),
(15, 70),
(24, 70),
(12, 70),
(10, 71),
(1, 71),
(1, 72),
(15, 72),
(12, 72),
(5, 73),
(15, 74),
(4, 74),
(1, 75),
(18, 75),
(1, 76),
(18, 76),
(1, 77),
(18, 77),
(1, 78),
(18, 78),
(1, 79),
(18, 79),
(1, 80),
(2, 80),
(21, 80),
(18, 80),
(12, 80),
(1, 81),
(12, 81),
(15, 81),
(1, 82),
(15, 82),
(7, 82),
(16, 83),
(1, 83),
(7, 83),
(1, 84),
(2, 84),
(15, 84),
(12, 84),
(1, 85),
(2, 85),
(15, 85),
(12, 85),
(21, 85),
(1, 86),
(2, 86),
(15, 86),
(12, 86),
(1, 87),
(2, 87),
(16, 88),
(7, 88),
(1, 89),
(2, 89),
(10, 89),
(1, 90),
(2, 90),
(1, 91),
(15, 91),
(1, 92),
(10, 92),
(24, 92),
(1, 93),
(2, 93),
(12, 93),
(1, 94),
(2, 94),
(12, 94),
(1, 95),
(2, 95),
(1, 96),
(2, 96),
(12, 96),
(1, 97),
(2, 97),
(1, 98),
(2, 98),
(12, 98),
(1, 99),
(2, 99),
(12, 99),
(2, 100),
(12, 100),
(21, 100),
(1, 100),
(1, 101),
(2, 101),
(12, 101),
(2,102),
(3,102),
(15,102);