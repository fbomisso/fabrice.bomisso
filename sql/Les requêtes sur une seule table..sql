-- Sélection de la base de données DataLens
USE DataLens;
GO


-- Récupère le nom de l'entreprise, le pays et le secteur d'activité
-- pour toutes les entreprises présentes dans la table ENTREPRISES.
SELECT nom_entreprise, pays, secteur_activite
FROM ENTREPRISES;


-- Récupère le nom et le pays des entreprises
-- uniquement lorsque le pays correspond à "FR" (France).
SELECT nom_entreprise, pays
FROM ENTREPRISES
WHERE pays = 'FR';

-- Affiche le nom et le prix catalogue des plans
-- dont le prix catalogue est supérieur à 100.
SELECT nom_plan, prix_catalogue
FROM PLANS
WHERE prix_catalogue > 100;

-- Affiche le nom des entreprises et leur date d'inscription,
-- puis classe les entreprises par date d'inscription dans l'ordre croissant.
SELECT nom_entreprise, date_inscription
FROM ENTREPRISES
ORDER BY date_inscription;

-- Affiche le nom des entreprises et leur date d'inscription,
-- puis les classe par date d'inscription dans l'ordre décroissant,
-- de la date la plus récente à la plus ancienne.
SELECT nom_entreprise, date_inscription
FROM ENTREPRISES
ORDER BY date_inscription DESC;

-- Affiche le nom des entreprises et leur secteur d'activité
-- pour les entreprises appartenant au secteur "Technologie" ou "Logiciels".
-- Les résultats sont ensuite classés par nom d'entreprise dans l'ordre alphabétique.
SELECT nom_entreprise, secteur_activite
FROM ENTREPRISES
WHERE secteur_activite = 'Technologie'
   OR secteur_activite = 'Logiciels'
ORDER BY nom_entreprise;

-- Affiche toutes les colonnes et toutes les lignes de la table PLANS.
SELECT *
FROM PLANS;

-- Affiche les 2 premières entreprises selon leur date d'inscription,
-- en commençant par la date la plus ancienne.
SELECT TOP 2 nom_entreprise, date_inscription
FROM ENTREPRISES
ORDER BY date_inscription;

-- Affiche les 3 plans les plus chers,
-- en classant les plans par prix catalogue du plus élevé au plus faible.
SELECT TOP 3 nom_plan, prix_catalogue
FROM PLANS
ORDER BY prix_catalogue DESC;

-- Affiche la liste des pays présents dans la table ENTREPRISES,
-- en supprimant les doublons pour ne conserver qu'une seule occurrence par pays.
SELECT DISTINCT pays
FROM ENTREPRISES;

-- Affiche la liste des secteurs d'activité présents dans la table ENTREPRISES,
-- en supprimant les doublons pour obtenir chaque secteur une seule fois.
SELECT DISTINCT secteur_activite
FROM ENTREPRISES;

-- Affiche le nom et le secteur d'activité des entreprises
-- dont le pays est soit la France ("FR"), soit l'Allemagne ("DE").
SELECT nom_entreprise, secteur_activite
FROM ENTREPRISES
WHERE pays IN ('FR', 'DE');

-- Affiche le nom et le prix catalogue des plans
-- dont le prix est compris entre 100 et 1000 inclus.
SELECT nom_plan, prix_catalogue
FROM PLANS
WHERE prix_catalogue BETWEEN 100 AND 1000;

-- Affiche le nom des entreprises dont le nom contient le mot "Data".
SELECT nom_entreprise
FROM ENTREPRISES
WHERE nom_entreprise LIKE '%Data%';

-- Affiche le nom des entreprises dont le nom contient "Pro".
SELECT nom_entreprise
FROM ENTREPRISES
WHERE nom_entreprise LIKE '%Pro%';