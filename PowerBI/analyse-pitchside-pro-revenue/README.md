# PitchSide Pro — Diagnostic de la Performance des Revenus

## 📌 Overview

Projet Power BI réalisé dans le cadre de la Manche 1 du **Power BI Data Visualization World Championship 2026**, sur le jeu de données fictif PitchSide Pro (e-commerce mondial d'articles de football, 2021-2025). La démarche a suivi un principe directeur fixé dès le départ : *« Laisser les chiffres trancher d'abord »* — plutôt que de construire le rapport autour d'une intuition séduisante (l'impact des tournois sportifs), chaque hypothèse a été formulée, testée puis confirmée ou explicitement rejetée avant d'aboutir à une thèse et des recommandations.

## 🎯 Business Problem

Décomposer une croissance de revenu de +43 % sur 5 ans en ses causes réelles (trafic, conversion, panier moyen), pour éviter d'attribuer à tort cette croissance à l'intuition la plus séduisante — les grands tournois sportifs — et orienter les décisions d'investissement (acquisition, conversion, marchés, calendrier marketing) sur des causes vérifiées plutôt que supposées.

## ❓ Analytical Questions

- Quelle part de la croissance du revenu vient du trafic, de la conversion, ou du panier moyen ?
- Les pics liés aux événements sportifs créent-ils un effet durable, ou sont-ils des opportunités ponctuelles ?
- Quelle région mérite l'investissement marketing suivant ?
- Le mix produit ou la pression promotionnelle expliquent-ils les écarts de performance entre marchés ?
- Le canal Mobile App convertit-il différemment du canal Web ?

## 📊 Dataset

- **Source** : jeu de données fourni dans le cadre du Power BI Data Visualization World Championship 2026 (fictif, aucune donnée externe ajoutée, conformément au règlement du concours).
- **Période** : 2021-2025, 8 pays (3 macro-régions : EMEA, Amériques, APAC), 2 canaux (Web, Mobile App).
- **Tables** : `FactSales` (133 362 lignes, grain = ligne de commande), `FactTraffic` (29 216 lignes, grain = jour × région × canal, déjà agrégé), `DimDate` (1 826 jours, avec saisonnalité football encodée : `SeasonLabel`, `IsTournamentWindow`, `IsTransferWindow`, `IsHolidayPeak`, `IsLeagueLaunch`), `DimProduct` (100 produits), `DimCustomer` (30 000 clients), `DimRegion` (8 pays), `DimChannel` (2 canaux).

## 🔎 Data Quality

| Vérification | Résultat | Implication |
|---|---|---|
| Intégrité référentielle (clés étrangères) | OK, 0 orphelin | Modèle en étoile fiable, aucun filtrage défensif requis |
| Doublons (grain Date × Région × Canal) | OK, aucun | Pas de risque de double comptage |
| Granularité `FactTraffic` | OK | 8 régions × 2 canaux × 1 826 jours = 29 216 lignes exactement — table dense, sans trou |
| `PromoType` NULL (53 % des lignes) | Confirmé : `DiscountAmount` = 0 à chaque fois | Catégorie légitime « prix plein », pas une donnée manquante — recodée en Power Query |
| Cohérence Gross / Discount / Net / Profit | Écarts négligeables (≤ 0,02 €) | Arrondi flottant, ne jamais recalculer ces colonnes par soustraction |
| Valeurs aberrantes (quantités, prix, marges, taux) | Aucune détectée | — |

**Seul geste de nettoyage retenu** : recoder le NULL de `PromoType` en « Prix Plein » via Power Query (`Table.TransformColumns`), en aval du fichier source — transformation de présentation dans la couche modèle, sans modification de la donnée brute (conforme au règlement du concours qui interdit toute édition des fichiers sources).

## 🧹 Data Preparation

Traitement volontairement minimal en Power Query (le seul nettoyage nécessaire étant `PromoType`), pour deux raisons documentées : exécution unique au chargement plutôt qu'à chaque interaction (performance), et séparation claire entre la couche DAX (calculs métier) et le nettoyage de présentation (cosmétique).

## 🧱 Data Model

Schéma en étoile avec **deux tables de faits à grains différents**, jamais reliées directement entre elles — elles communiquent uniquement via les dimensions partagées (`DimDate`, `DimRegion`, `DimChannel`). `DimProduct` et `DimCustomer` ne se relient qu'à `FactSales`, car `FactTraffic` est déjà agrégé et ne conserve aucune clé produit ou client — limite structurelle du dataset assumée et documentée, pas une erreur de modélisation.

**Point de vigilance identifié et géré** : `DimCustomer` contient une colonne `MacroRegion` dénormalisée, dupliquant une information déjà présente dans `DimRegion`. Cette dénormalisation existe dans les données sources (non modifiée, conformément au règlement) — décision retenue : privilégier un seul chemin de filtre (`DimRegion[MacroRegion]`) par visuel pour éviter toute ambiguïté.

`DimDate` marquée explicitement comme « Table de dates » (requis par les fonctions de Time Intelligence DAX comme `SAMEPERIODLASTYEAR` — sans ce réglage, ces fonctions produisent des résultats silencieusement faux, sans erreur visible).

## 📐 Analytical Approach — la démarche « les chiffres tranchent d'abord »

### Axe temporel : une croissance continue de +43 % (2021-2025)

L'effet tournoi brut affichait +19 % de revenu/jour en fenêtre événementielle — mais cette lecture est trompeuse : la tendance de fond progresse déjà de ~9,5 %/an, et les deux tournois majeurs tombent sur des années différentes. **Correction méthodologique appliquée** : chaque fenêtre événementielle a été comparée à la même fenêtre calendaire les autres années (et non à la moyenne globale), pour isoler le véritable effet tournoi de la croissance organique.

### Axe Facteurs : décomposition Sessions × Conversion × AOV

| Indicateur | 2021 | 2025 |
|---|---|---|
| Sessions (trafic) | 100 | 138,2 |
| Taux de conversion | 100 | 100,0 |
| Panier moyen (AOV) | 100 | 102,1 |

**Verdict** : le trafic (+38,2 %) explique presque intégralement la croissance du revenu (+43,0 %). Le taux de conversion est resté parfaitement stable (entre 2,99 % et 3,01 %, littéralement plat à la décimale près).

**Vérification croisée sur deux axes indépendants** (pour écarter un effet de moyenne masquant des disparités) :
- Par région (8 pays) : conversion variant de +0,9 % à -0,5 % sur cinq ans — du bruit, pas un signal, sans exception.
- Par canal (Web vs Mobile App) : conversion figée sur les deux canaux (delta nul à quasi nul), trafic identique à la décimale près (+38,2 % partout).

### Axe Mix : deux hypothèses testées et rejetées

| Hypothèse testée | Résultat |
|---|---|
| Le mix produit (catégories, TeamType, édition limitée) explique-t-il la sur-performance de l'Allemagne/US/Brésil ? | **Rejetée** — catalogue quasi identique partout (écarts < 2 %) |
| La pression promotionnelle explique-t-elle la sous-performance du Royaume-Uni ? | **Rejetée** — taux de remise dans la moyenne (2,42-2,44 %), non corrélé au recul de l'AOV |

Ces deux rejets, documentés avec la même rigueur que les résultats positifs, renforcent la crédibilité de la conclusion finale : deux pistes restent explicitement ouvertes pour une itération future (mix fin StarPlayer/BrandLine, effet macro-économique `PriceIndex`/`ConversionIndex`) plutôt que d'être présentées comme résolues.

## 📊 Dashboard (5 pages)

### Page 1 — Tribune exécutive
**Objectif :** comment va l'entreprise, là, maintenant ?
**KPI :** Net Revenue (11,22M€), Total Profit (5,93M€), Marge bénéficiaire (52,8 %), Taux de conversion (3,2 %), Commandes (102K).
**Analyses :** courbe du revenu net mensuel 2021-2025 avec bandes visuelles sur les fenêtres tournois/Kit Launch Season, répartition du revenu par canal et par catégorie.

![Tribune exécutive](screenshots/01-tribune-executive.jpg)

### Page 2 — Sous le capot
**Objectif :** le revenu croît — mais pourquoi ?
**KPI :** Indice de croissance des sessions (138,2), indice de croissance du taux de conversion (100 = stable), indice de croissance du panier moyen (102,1).
**Analyses :** graphique combiné barres (Sessions) + ligne (Conversion Rate %) — le visuel le plus important du rapport, avec bornes d'axe Y fixées manuellement (0-5 %) pour ne pas exagérer visuellement une variation négligeable ; table de décomposition indexée base 100.
**Insights :** titre porteur d'insight plutôt que descriptif — « Le trafic double, la conversion ne bouge pas ».

![Sous le capot](screenshots/02-sous-le-capot.jpg)

### Page 3 — Cartographie du signal
**Objectif :** quels marchés méritent un focus, et pourquoi ?
**Analyses :** classement des 8 pays par écart croissance revenu vs croissance trafic (mesure `Revenue vs Traffic Gap 2021-2025`, code couleur vert/rouge), table de détail triable, mix produit par pays démontrant l'hypothèse rejetée.
**Insights :** Allemagne (+12,4 pts), Brésil (+11,1 pts), États-Unis (+10,2 pts) en sur-performance ; Royaume-Uni seul en écart négatif (-4,8 pts).

![Cartographie du signal](screenshots/03-cartographie-du-signal.jpg)

### Page 4 — Le faux coupable
**Objectif :** les tournois sont-ils vraiment le driver qu'on pensait ?
**Analyses :** revenu par jour par `SeasonLabel` (barres horizontales), comparaison Sessions/jour vs AOV par saison.
**Insights :** Kit Launch Season (7 427 €/jour, AOV 119,57€) est la seule période combinant trafic ET valeur, contrairement aux tournois portés presque uniquement par le volume — et elle revient chaque année, contrairement aux tournois qui n'arrivent qu'épisodiquement.

![Le faux coupable](screenshots/04-le-faux-coupable.jpg)

### Page 5 — Le plan de match
**Objectif :** et maintenant, qu'est-ce qu'on fait ?
**Contenu :** trois blocs de recommandations scannables (Optimiser la conversion / Recalibrer sur Kit Launch Season / Marchés à investiguer), avec renvoi explicite vers les pages-preuve correspondantes — pas de nouvelle analyse de données brutes sur cette page, uniquement une synthèse.

![Le plan de match](screenshots/05-le-plan-de-match.jpg)

## 🔑 Key Insights

- **Observation :** le trafic a progressé de +38,2 % sur 5 ans, sur 8 pays et 2 canaux sans exception, tandis que le taux de conversion est resté figé à ~3 %. **Interprétation :** la croissance de l'entreprise repose sur un unique moteur (l'acquisition), vérifié sur deux axes de coupe indépendants. **Implication métier :** l'entonnoir de conversion est une réserve de croissance inexploitée, plus importante que tout effet calendaire sportif.
- **Observation :** l'effet tournoi brut (+19 % de revenu/jour) se réduit une fois corrigé de la tendance organique et comparé à fenêtre calendaire identique. **Interprétation :** les tournois amplifient le trafic, ils ne créent pas un mécanisme différent. **Implication métier :** ne pas surestimer l'impact structurel des grands événements sportifs dans la planification.
- **Observation :** Allemagne, États-Unis et Brésil affichent un panier moyen en croissance (+3 à +4 %) sans différence de mix produit ni de pression promotionnelle par rapport aux autres marchés. **Interprétation :** corrélation identifiée, cause non isolée — volontairement reformulée d'une conclusion affirmative vers une piste à investiguer. **Implication métier :** ne pas lancer d'action de montée en gamme avant d'avoir compris la cause réelle.

## 💡 Business Recommendations

- **Prioriser l'optimisation de la conversion** avant d'augmenter le budget d'acquisition : un gain de seulement +0,3 à +0,5 point de conversion, à trafic constant, représenterait un gain de revenu à deux chiffres.
- **Désigner l'Allemagne, les États-Unis et le Brésil comme marchés prioritaires à investiguer** (pas encore à cibler commercialement) pour comprendre la cause de leur progression d'AOV avant toute action de premiumisation.
- **Recalibrer le calendrier marketing et la gestion des stocks autour de Kit Launch Season** (récurrent chaque année) plutôt qu'autour des tournois sportifs (épisodiques) comme driver principal de la stratégie commerciale annuelle.

## 🛠️ Technologies

Power BI Desktop · Power Query (M) · DAX (`DIVIDE`, `DISTINCTCOUNT`, `CALCULATE` à bornes fixes, `SAMEPERIODLASTYEAR`, `TOTALYTD`, mesures de ratio référençant d'autres mesures) · Modélisation en étoile à deux tables de faits de grains différents

## 📁 Project Structure

```text
analyse-pitchside-pro-revenue/
├── README.md
├── screenshots/
│   ├── 01-tribune-executive.jpg
│   ├── 02-sous-le-capot.jpg
│   ├── 03-cartographie-du-signal.jpg
│   ├── 04-le-faux-coupable.jpg
│   └── 05-le-plan-de-match.jpg
├── documentation/
│   └── PitchSidePro_Documentation_Projet.docx   # démarche complète, sections 1 à 12
├── data/       # [À COMPLÉTER EN LOCAL]
└── pbix/       # [À COMPLÉTER EN LOCAL]
```

## ▶️ How to Explore

`[À COMPLÉTER EN LOCAL]` — préciser si le `.pbix` sera publié dans `pbix/` (vérifier sa taille avant de committer, cf. les limites GitHub déjà rencontrées sur le projet Retail).

## ⚠️ Limitations

- Dataset fictif, fourni dans le cadre d'un concours (Power BI Data Visualization World Championship 2026) — aucune donnée externe n'a pu être ajoutée, conformément au règlement.
- `FactTraffic` étant déjà agrégé au grain jour × région × canal, aucun visuel ne peut croiser Sessions/Conversion avec un attribut client ou produit individuel (segment, catégorie) — limite structurelle du dataset, pas un axe d'analyse manquant.
- La cause exacte de la progression du panier moyen en Allemagne, aux États-Unis et au Brésil n'a pas été isolée dans le cadre de ce projet — présentée comme piste à investiguer, pas comme conclusion.
- L'érosion légère de l'AOV au Royaume-Uni n'est expliquée ni par le mix produit ni par la pression promotionnelle — cause non identifiée.

## 🚀 Future Improvements

- Isoler la cause de la progression du panier moyen en Allemagne/US/Brésil (mix fin `StarPlayer`/`BrandLine`, ou effet `PriceIndex`/`ConversionIndex` de `DimRegion`).
- Analyser si les clients acquis pendant les fenêtres de tournoi (cohortes `IsTournamentWindow`, via la colonne calculée `Acquisition Year`) ont un comportement d'achat différent dans la durée.
- Croiser `Price Tier` avec `Country` pour tester si les marchés en sur-performance d'AOV achètent proportionnellement plus de produits Premium/Ultra-Premium.
- Investiguer séparément l'érosion d'AOV du Royaume-Uni.

---

## 🎓 Skills Demonstrated

| Compétence | Preuve |
|---|---|
| Data Quality | 7 vérifications systématiques avant exploration (intégrité référentielle, doublons, granularité, cohérence arithmétique) menées pour éviter un faux positif d'analyse |
| DAX | Mesures de décomposition causale (Sessions × Conversion × AOV), choix méthodologique documenté entre comparaison glissante (YoY) et comparaison structurelle à bornes fixes, `DISTINCTCOUNT(OrderID)` plutôt que `COUNTROWS` pour un panier moyen exact |
| Data Modeling | Schéma en étoile à deux tables de faits de grains différents communiquant uniquement via dimensions partagées ; limite structurelle du dataset documentée plutôt que masquée |
| Power Query (M) | Nettoyage minimal et justifié (recodage `PromoType`), conforme à une contrainte réglementaire de non-modification des données sources |
| Business Analysis | Démarche d'hypothèses testées puis explicitement rejetées (mix produit, pression promotionnelle) avant d'aboutir à une thèse robuste, vérifiée sur deux axes de coupe indépendants |
| Data Storytelling | Script de présentation exécutive structuré (contexte → constat → contre-exemple → recommandations → punchline), page de rapport dédiée aux recommandations sans réintroduction d'analyse brute |
| Problem Solving | Reformulation volontaire d'une conclusion affirmative en piste à investiguer lorsque la cause n'était pas démontrée, uniquement la corrélation |
