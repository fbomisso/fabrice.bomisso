---
title: "💳 Pilotage du Risque de Crédit | Analyse de Prêts Bancaires"
layout: "single"
hideMeta: true
---

## 🎯 Objectif

Construire un dashboard Power BI dédié au **pilotage du risque de crédit** permettant à une institution financière de suivre la santé de son portefeuille de prêts : volume prêté, taux de défaut, rentabilité et profil de risque selon le grade, l'objet du prêt, le statut de vérification et le profil de l'emprunteur.

## 🧩 Contexte

Le dataset couvre **38 576 contrats de prêt**, répartis dans les **50 États américains**.

Les prêts ont été émis sur l'année **2021**, du 1er janvier au 12 décembre 2021. Le suivi des paiements, du dernier paiement, du prochain paiement et du dernier tirage de crédit s'étend jusqu'en janvier 2022. L'année 2021 est donc la seule période pleinement exploitable pour l'analyse des tendances temporelles.

La table calendrier du modèle couvre volontairement une période plus large, d'octobre 2021 à janvier 2024. Cette approche permet d'anticiper l'arrivée de nouvelles données sans devoir reconstruire le modèle.

## 🔗 Sources de données

* `LOANS_FACT` : table de faits principale contenant les informations sur les contrats de prêt : montant, statut, grade, taux d'intérêt, objet, durée, etc.
* Dimensions : État américain, Grade (A à G), Statut de vérification, Statut de propriété, Ancienneté d'emploi et Métier.
* `Date_Dimension_tab` : table calendrier dédiée aux analyses temporelles.

## 📈 KPIs

| KPI                        | Ce qu'il mesure                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| Montant Total Prêté        | Volume total du portefeuille                                                                  |
| Nombre Total de Prêts      | Nombre total de contrats                                                                      |
| Montant Moyen par Prêt     | Taille moyenne d'un contrat                                                                   |
| Taux de Défaut             | Pourcentage de prêts en défaut (Charged Off), soit **13,82 %** sur l'ensemble du portefeuille |
| Taux de Remboursement      | Montant Total Remboursé / Montant Total Prêté                                                 |
| Taux d'Intérêt Moyen       | Taux d'intérêt moyen pondéré du portefeuille                                                  |
| DTI Moyen                  | Ratio dette/revenu moyen des emprunteurs                                                      |
| Revenu Annuel Moyen        | Niveau de revenu moyen des emprunteurs                                                        |
| Montant en Défaut          | Exposition totale sur les prêts en défaut                                                     |
| Croissance Mensuelle       | Évolution du montant prêté par rapport au mois précédent                                      |
| Montant Prêté Cumul Annuel | Cumul du montant prêté depuis le début de l'année                                             |

## 🔍 Analyses réalisées

### Modélisation

Le modèle repose sur un **schéma en étoile** avec `LOANS_FACT` comme table de faits centrale. Elle est reliée à une table calendrier dédiée ainsi qu'aux principales dimensions d'analyse du risque : Grade, État, Statut de vérification et Statut de propriété.

### DAX : Taux d'Intérêt Moyen

La colonne source `INT_RATE` étant déjà multipliée par 100 dans Power Query, la mesure divise explicitement la valeur par 100 avant d'appliquer le format Pourcentage natif de Power BI.

Cette correction évite un doublement de l'affichage. Sans elle, un taux réel de 12,05 % apparaissait à tort comme 1204,88 %.

### DAX : Croissance Mensuelle

La mesure compare des **mois entiers** plutôt que des jours précis. Une comparaison jour par jour peut en effet retourner zéro lorsqu'un jour donné ne contient aucune transaction.

Le mois de référence est déterminé dynamiquement à partir du dernier mois contenant des données non nulles, puis comparé au mois précédent avec `EDATE`.

Résultat validé : **+13,04 %** entre décembre 2021 et novembre 2021.

### Analyse du risque

Une matrice Grade × Statut de prêt permet de comparer plusieurs indicateurs avec une mise en forme conditionnelle indépendante : taux de défaut, taux de remboursement et proportion de crédits en cours.

Cette analyse permet d'identifier rapidement les grades les plus risqués. Les grades F et G présentent notamment des taux de défaut compris entre 24 % et 31 %, contre environ 5 % à 6 % pour le grade A.

Une analyse croisée du DTI moyen et du taux d'intérêt moyen par statut et par grade permet également de mieux comprendre la structure du risque.

### Profil emprunteur

Le profil des emprunteurs est analysé selon le statut de propriété, l'ancienneté d'emploi et le niveau de revenu.

La distribution des revenus est représentée sous forme d'histogramme avec des tranches de 10 000 $, afin de mieux visualiser la concentration des emprunteurs selon leur niveau de revenu.

### Rigueur méthodologique

Plusieurs différences entre le plan initial et le dashboard finalement construit ont été documentées plutôt que masquées.

Un Treemap a été remplacé par une table jugée plus lisible. Deux visuels initialement prévus n'ont pas été retenus au profit d'un histogramme de distribution des revenus. Deux visuels consacrés aux flux financiers ont également été privilégiés après confirmation de la limite principale du dataset : une seule année complète de données.

## 🛠️ Technologies utilisées

* **Power BI Desktop** : Power Query, modèle de données et DAX
* **Power Query (M)** : préparation et transformation des données, notamment la mise à l'échelle du taux d'intérêt
* **DAX** : mesures avec variables, `CALCULATE`, `FILTER`, `EDATE` et mise en forme conditionnelle par règles

## 🖼️ Aperçu du dashboard

Le rapport comprend **4 pages**, chacune répondant à une question métier spécifique.

### Vue Exécutive

Cette page permet à un dirigeant d'obtenir rapidement une vision globale de l'état du portefeuille.

Elle comprend 5 KPI Cards, la répartition des prêts par statut, le taux de défaut par grade, une carte à formes du montant prêté par État et l'évolution mensuelle du volume.

![Vue Exécutive](./screenshots/01-vue-executive.jpg)

### Analyse du Risque

Cette page permet d'identifier où se concentrent les défauts et d'examiner les principaux facteurs associés au risque.

Elle présente une matrice Grade × Statut avec mise en forme conditionnelle, le taux de défaut par objet du prêt et par statut de vérification, ainsi qu'un nuage de points DTI vs taux d'intérêt.

![Analyse du risque](./screenshots/02-analyse-du-risque.jpg)

### Profil Emprunteur

Cette page permet de segmenter les emprunteurs afin d'affiner l'analyse du portefeuille et la politique d'octroi.

Elle présente le revenu annuel moyen et médian, la distribution des revenus, le taux de défaut selon le statut de propriété et l'ancienneté d'emploi, ainsi que le Top 10 des métiers représentés.

![Profil emprunteur](./screenshots/03-profil-emprunteur.jpg)

### Évolution Temporelle

Cette page permet d'analyser les principales tendances observées sur l'année 2021.

Elle présente le montant prêté et le montant remboursé par mois, la croissance mensuelle, l'évolution du taux de défaut et le taux d'intérêt moyen mensuel.

![Évolution Temporelle](./screenshots/04-evolution-temporelle.jpg)

> ℹ️ Les captures montrent une vue filtrée du dashboard, notamment sur le mois de juillet. Le bandeau « Données à jour au 31/07/2023 » visible sur les captures provient d'un gabarit initial et ne correspond pas à la couverture réelle des données. Le dataset couvre principalement l'année 2021, comme indiqué dans le contexte du projet.

## 💡 Insights clés

* Le taux de défaut global du portefeuille est de **13,82 %**, mais varie fortement selon le grade. Il passe d'environ 5,6 % pour le grade A à plus de 28 % pour les grades F et G. Le grade apparaît ainsi comme le facteur de risque le plus discriminant du modèle.
* Le volume mensuel de prêts a presque doublé entre janvier et décembre 2021, avec une progression de **+115,7 %**. Cette hausse ne s'est toutefois pas accompagnée d'une dégradation continue du taux de défaut, qui oscille entre 11,6 % et 15,1 % sur l'année. Deux pics ponctuels sont observés en mai et décembre, sans tendance générale clairement identifiable.
* La comparaison de mois entiers est indispensable pour obtenir une mesure fiable de la croissance mensuelle lorsque l'activité varie fortement d'un jour à l'autre.

## 📂 Contenu du dossier

```text
pilotage-risque-credit-bancaire/
├── README.md
├── data/                              # Données sources à compléter
├── screenshots/                       # Captures des 4 pages du dashboard
├── documentation/
│   └── Corrections_Projet_BI.docx     # Écarts identifiés et corrections apportées
└── pilotage-risque-credit-bancaire.pbix   # Fichier Power BI à ajouter
```
---

<div class="project-github-link">

<a href="https://github.com/fbomisso/fabrice.bomisso/tree/main/PowerBI/pilotage-risque-credit-bancaire" target="_blank" rel="noopener">
🔗 Voir le projet sur GitHub →
</a>

</div>


