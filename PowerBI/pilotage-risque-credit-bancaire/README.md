# 💳 Pilotage du Risque de Crédit — Analyse de Prêts Bancaires

## 🎯 Objectif

Construire un dashboard Power BI de **pilotage du risque de crédit** permettant à une institution financière de suivre la santé de son portefeuille de prêts : volume prêté, taux de défaut, rentabilité, et profil de risque par grade, objet du prêt, statut de vérification et profil emprunteur.

## 🧩 Contexte

Le dataset couvre **38 576 contrats de prêt**, répartis dans les **50 États américains**. Les prêts ont été émis sur l'année **2021** (du 1er janvier au 12 décembre 2021), avec un suivi de paiement (dernier paiement, prochain paiement, dernier tirage de crédit) s'étendant jusqu'en janvier 2022 — c'est donc la seule année pleinement analysable pour les tendances temporelles.

La table calendrier du modèle couvre volontairement une période plus large (octobre 2021 – janvier 2024) que les données réelles : une bonne pratique de modélisation qui anticipe l'arrivée de nouvelles données sans reconstruction du modèle.

## 🔗 Sources de données

- `LOANS_FACT` — table de faits principale des contrats de prêt (montant, statut, grade, taux d'intérêt, objet, durée...)
- Dimensions : État américain, Grade (A→G), Statut de vérification, Statut de propriété, Ancienneté d'emploi, Métier
- `Date_Dimension_tab` — table calendrier dédiée (relation avec les dates de faits)

## 📈 KPIs

| KPI (nom français du modèle) | Ce qu'il mesure |
|---|---|
| Montant Total Prêté | Volume total du portefeuille |
| Nombre Total de Prêts | Volume en nombre de contrats |
| Montant Moyen par Prêt | Taille moyenne d'un contrat |
| Taux de Défaut | % de prêts en défaut (Charged Off) — **13,82 %** sur l'ensemble du portefeuille |
| Taux de Remboursement | Montant Total Remboursé / Montant Total Prêté |
| Taux d'Intérêt Moyen | Taux d'intérêt moyen pondéré du portefeuille |
| DTI Moyen | Ratio dette/revenu moyen des emprunteurs |
| Revenu Annuel Moyen | Profil de revenu des emprunteurs |
| Montant en Défaut | Exposition totale sur les prêts en défaut |
| Croissance Mensuelle | Évolution du montant prêté par rapport au mois précédent |
| Montant Prêté Cumul Annuel | Cumul du montant prêté depuis le début de l'année |

## 🔍 Analyses réalisées

**Modélisation** — Schéma en étoile avec `LOANS_FACT` comme table de faits centrale, reliée à une table calendrier dédiée et aux dimensions de risque (Grade, État, Statut de vérification, Statut de propriété).

**DAX — Taux d'Intérêt Moyen** — La colonne source `INT_RATE` étant déjà multipliée par 100 en Power Query, la mesure divise explicitement par 100 avant application du format Pourcentage natif de Power BI, pour éviter un doublement d'affichage (12,05 % affiché à tort comme 1204,88 % sans cette correction).

**DAX — Croissance Mensuelle** — Mesure construite pour comparer des **mois entiers** plutôt que des jours précis (une comparaison jour-à-jour tombe à zéro dès qu'un jour donné n'a pas de transaction). Le mois de référence est déterminé dynamiquement (dernier mois avec des données non nulles) puis comparé au mois précédent via `EDATE`. Résultat validé : **+13,04 %** (décembre 2021 vs novembre 2021).

**Analyse du risque** — Matrice croisant Grade × Statut de prêt avec mise en forme conditionnelle indépendante par mesure (taux de défaut, de remboursement, de crédits en cours), permettant d'identifier immédiatement les grades à risque (F et G affichent des taux de défaut de 24–31 % contre 5–6 % pour le grade A). Analyse croisée DTI moyen / taux d'intérêt moyen par statut et grade pour visualiser la structure du risque.

**Profil emprunteur** — Segmentation par statut de propriété, ancienneté d'emploi et distribution des revenus (histogramme natif par tranches de 10 000 $), pour affiner la politique d'octroi de prêts.

**Rigueur méthodologique** — Plusieurs écarts entre le plan initial et le dashboard réellement construit ont été documentés et assumés plutôt que masqués : un Treemap remplacé par une table plus lisible, deux visuels non retenus au profit d'un histogramme de distribution des revenus jugé plus riche, et deux visuels de flux financier privilégiés une fois la limite réelle des données (une seule année complète) confirmée.

## 🛠️ Technologies utilisées

- **Power BI Desktop** (Power Query, modèle de données, DAX)
- **Power Query (M)** pour la préparation des données (dont la mise à l'échelle du taux d'intérêt)
- **DAX** (mesures avec variables, `CALCULATE`, `FILTER`, `EDATE`, mise en forme conditionnelle par règles)

## 🖼️ Aperçu du dashboard

Le rapport comprend **4 pages**, chacune conçue pour une question métier et un profil utilisateur précis.

### Vue Exécutive — un dirigeant comprend l'état du portefeuille en 30 secondes
5 KPI Cards, répartition par statut de prêt, taux de défaut par grade, carte à formes du montant prêté par État, évolution mensuelle du volume.
![Vue Exécutive](./screenshots/01-vue-executive.jpg)

### Analyse du Risque — où se concentrent les défauts, et pourquoi
Matrice Grade × Statut avec mise en forme conditionnelle, taux de défaut par objet du prêt et par statut de vérification, nuage de points DTI vs taux d'intérêt.
![Analyse du risque](./screenshots/02-analyse-du-risque.jpg)

### Profil Emprunteur — segmenter les emprunteurs pour affiner la politique d'octroi
Revenu annuel moyen et médian, distribution des revenus, taux de défaut par statut de propriété et ancienneté d'emploi, top 10 des métiers représentés.
![Profil emprunteur](./screenshots/03-profil-emprunteur.jpg)

### Évolution Temporelle — détecter les tendances sur l'année 2021
Montant prêté vs montant remboursé par mois, croissance mensuelle, évolution du taux de défaut et du taux d'intérêt moyen mensuel.
![Évolution Temporelle](./screenshots/04-evolution-temporelle.jpg)

> ℹ️ Les captures ci-dessus montrent une vue filtrée du dashboard (mois de juillet, bandeau "Données à jour au 31/07/2023" hérité d'un gabarit initial) — la couverture réelle des données est l'année 2021, comme précisé dans le contexte ci-dessus.

## 💡 Insights clés

- Le taux de défaut global du portefeuille est de **13,82 %**, mais varie fortement selon le grade : de 5,6 % (grade A) à plus de 28 % (grade F/G) — le grade est le facteur de risque le plus discriminant du modèle.
- Le volume mensuel de prêts a quasiment doublé entre janvier et décembre 2021 (**+115,7 %**), sans dégradation continue du taux de défaut : celui-ci oscille entre 11,6 % et 15,1 % sur l'année, avec deux pics ponctuels (mai et décembre) mais sans tendance de fond claire. La croissance du volume ne s'est donc pas accompagnée d'une dégradation continue de la qualité du portefeuille.
- La comparaison de mois entiers (plutôt que de jours précis) est indispensable pour un calcul de croissance mensuelle fiable sur des données dont l'activité est irrégulière jour par jour.

## 📂 Contenu du dossier

```text
pilotage-risque-credit-bancaire/
├── README.md
├── data/                              # Données sources (à compléter)
├── screenshots/                       # Captures des 4 pages du dashboard
├── documentation/
│   └── Corrections_Projet_BI.docx     # Écarts identifiés et corrections apportées au rapport initial
└── pilotage-risque-credit-bancaire.pbix   # à ajouter
```
