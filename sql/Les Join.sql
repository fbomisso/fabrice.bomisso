-- Sélectionne la base de données DataLens,
-- puis récupère les informations des abonnements en les reliant aux entreprises.
-- La jointure INNER JOIN conserve uniquement les abonnements
-- qui possèdent une entreprise correspondante dans la table ENTREPRISES.
USE DataLens;
GO

SELECT 
    e.nom_entreprise,
    a.date_debut,
    a.date_fin,
    a.prix_mensuel
FROM ABONNEMENTS a
INNER JOIN ENTREPRISES e 
    ON a.id_entreprise = e.id_entreprise;

GO