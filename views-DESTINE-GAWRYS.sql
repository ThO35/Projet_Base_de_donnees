CREATE VIEW vue_nombre_ventes AS
SELECT entreprise.nom_entreprise AS entreprise,
COUNT(achete.id_jeu) AS nombre_ventes
FROM entreprise
LEFT JOIN jeu ON entreprise.id_entreprise = jeu.id_entreprise_edit
LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu
GROUP BY entreprise.nom_entreprise;

CREATE VIEW vue_nombre_jeux_partages AS
SELECT entreprise.nom_entreprise AS entreprise,
COUNT(joueur.id_jeu_partage) AS nombre_jeux_partages
FROM entreprise
LEFT JOIN jeu ON entreprise.id_entreprise = jeu.id_entreprise_edit
LEFT JOIN joueur ON jeu.id_jeu = joueur.id_jeu_partage
GROUP BY entreprise.nom_entreprise;

CREATE VIEW vue_chiffre_affaire AS
SELECT entreprise.nom_entreprise AS entreprise,
SUM(jeu.prix) AS chiffre_affaire
FROM entreprise
LEFT JOIN jeu ON entreprise.id_entreprise = jeu.id_entreprise_edit
LEFT JOIN achete ON jeu.id_jeu = achete.id_jeu
WHERE achete.date_achat IS NOT NULL
GROUP BY entreprise.nom_entreprise;

CREATE VIEW vue_notation_moyenne AS
SELECT entreprise.nom_entreprise AS entreprise,
AVG(commente.note) AS notation_moyenne
FROM entreprise
LEFT JOIN jeu ON entreprise.id_entreprise = jeu.id_entreprise_edit
LEFT JOIN commente ON jeu.id_jeu = commente.id_jeu
GROUP BY entreprise.nom_entreprise;

CREATE VIEW vue_succes_obtenus AS
SELECT entreprise.nom_entreprise AS entreprise,
COUNT(obtient.id_succes) AS nombre_succes_obtenus
FROM entreprise
LEFT JOIN jeu ON entreprise.id_entreprise = jeu.id_entreprise_edit
LEFT JOIN succes ON jeu.id_jeu = succes.id_jeu_s
LEFT JOIN obtient ON succes.id_succes = obtient.id_succes
GROUP BY entreprise.nom_entreprise;