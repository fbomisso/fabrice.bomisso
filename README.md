# Customer Churn Prediction — From Data to Business Decision

## 📋 Présentation

Ce projet met en œuvre une démarche complète de **Data Science appliquée à la prédiction du churn client**, depuis l'exploration des données jusqu'à la mise à disposition d'une application de prédiction avec Streamlit.

L'objectif est d'identifier les clients susceptibles de quitter une entreprise de télécommunications, de comprendre les principaux facteurs associés au churn et de transformer ces résultats en un outil d'aide à la décision.

**Problématique :** comment identifier suffisamment tôt les clients présentant un risque élevé de churn afin de permettre aux équipes métier de prioriser leurs actions de fidélisation ?

**Solution :** un pipeline de Machine Learning basé sur un **Random Forest**, complété par une analyse SHAP, une segmentation des clients selon leur niveau de risque et une application Streamlit permettant de réaliser des prédictions individuelles.

---

## 🎯 Objectifs du projet

* Analyser les facteurs associés au churn client
* Nettoyer et préparer les données
* Construire de nouvelles variables pertinentes pour la prédiction
* Comparer plusieurs modèles de classification
* Sélectionner le modèle le plus adapté à l'objectif métier
* Interpréter les prédictions avec SHAP
* Segmenter les clients selon leur niveau de risque
* Formuler des recommandations métier à partir des résultats observés
* Déployer le modèle dans une application Streamlit

---

## 📊 Dataset

**Source :** IBM Telco Customer Churn Dataset

**Dataset utilisé :** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

**Taille :**

* 7 043 clients
* 21 variables initiales
* Variable cible : `Churn`

Le dataset contient notamment des informations relatives :

* au profil démographique ;
* à l'ancienneté ;
* aux services souscrits ;
* au type de contrat ;
* aux méthodes de paiement ;
* aux charges mensuelles et totales.

---

## 🔄 Méthodologie

Le projet suit les principales étapes d'un workflow de Data Science :

**Données → Nettoyage → EDA → Feature Engineering → Modélisation → Évaluation → SHAP → Segmentation → Recommandations métier → Application Streamlit**

---

## 🧹 Phase 1 — Nettoyage des données

Plusieurs contrôles ont été réalisés afin de préparer les données pour la modélisation.

### Principales opérations

* Conversion de `TotalCharges` en variable numérique
* Transformation de la variable cible `Churn` en variable binaire
* Traitement des valeurs manquantes
* Vérification des types de données
* Préparation des variables catégorielles et numériques

Les valeurs manquantes observées dans `TotalCharges` correspondent aux clients ayant une ancienneté nulle. Elles ont été traitées en cohérence avec ce contexte.

---

## ⚙️ Phase 2 — Feature Engineering

De nouvelles variables ont été créées afin de fournir au modèle des informations plus directement exploitables.

Parmi les principales variables :

* `tenure_years`
* `is_new_customer`
* `is_young_customer`
* `high_monthly_charges`
* `low_monthly_charges`
* `num_services`
* `has_multiple_services`
* `has_tech_support`
* `has_security`
* `is_automatic_payment`
* `is_long_contract`
* `risky_profile`

Ces variables permettent notamment de représenter l'ancienneté, le niveau d'équipement du client, son type d'engagement et certains profils considérés comme potentiellement plus exposés au churn.

---

## 🔎 Phase 3 — Analyse exploratoire

L'analyse exploratoire a permis d'identifier plusieurs associations importantes avec le churn.

### Principaux constats

| Facteur        | Observation                                                                               |
| -------------- | ----------------------------------------------------------------------------------------- |
| **Ancienneté** | Les clients les moins anciens présentent davantage de churn                               |
| **Contrat**    | Les contrats `Month-to-month` sont davantage associés au churn                            |
| **Internet**   | Le taux de churn est plus élevé chez les clients `Fiber optic` dans les données analysées |
| **Paiement**   | `Electronic check` présente un taux de churn élevé                                        |
| **Services**   | Les clients disposant de certains services additionnels présentent un churn plus faible   |

Ces observations servent de base à l'analyse prédictive, mais une association observée dans les données ne signifie pas nécessairement qu'elle constitue une relation causale.

---

## 🤖 Phase 4 — Modélisation

Deux modèles de classification ont été étudiés :

* **Logistic Regression**
* **Random Forest**

L'objectif principal étant de détecter le plus grand nombre possible de clients susceptibles de churner, le **Recall** constitue une métrique particulièrement importante.

### Random Forest — modèle retenu

| Métrique |    Résultat |
| -------- | ----------: |
| Accuracy |      79,0 % |
| Recall   | **77,81 %** |
| F1-score | **63,75 %** |
| ROC-AUC  |        0,85 |

Le Random Forest a été retenu car il permet de détecter une proportion importante des clients ayant réellement churné, avec un **Recall de 77,81 %**.

---

## 🔍 Phase 5 — Explainability avec SHAP

L'analyse SHAP a été utilisée afin de mieux comprendre les variables qui contribuent aux prédictions du modèle.

Les variables importantes identifiées comprennent notamment :

1. `is_long_contract`
2. `InternetService_Fiber optic`
3. `tenure_years`
4. `tenure`
5. `Contract_Two year`

L'analyse montre notamment l'importance de facteurs liés à **l'engagement contractuel, l'ancienneté et le service Internet** dans les prédictions du modèle.

SHAP permet ainsi de compléter les performances du modèle par une lecture plus interprétable de ses décisions.

---

## 🎯 Phase 6 — Segmentation des clients à risque

Le modèle a été utilisé pour attribuer un score de risque aux **1 409 clients du jeu de test**.

Les clients ont ensuite été répartis en trois catégories :

| Catégorie     | Clients | Churn réel | Score moyen | Ancienneté moyenne |
| ------------- | ------: | ---------: | ----------: | -----------------: |
| 🔴 **ÉLEVÉ**  |     295 | **66,4 %** |      81,4 % |           8,1 mois |
| 🟠 **MOYEN**  |     332 | **35,8 %** |      55,9 % |          23,6 mois |
| 🟢 **FAIBLE** |     782 |  **7,5 %** |      15,5 % |          44,5 mois |

Cette segmentation montre une bonne capacité du modèle à différencier les niveaux de risque.

Le groupe **ÉLEVÉ** présente un taux de churn réel de 66,4 %, contre seulement 7,5 % pour le groupe **FAIBLE**.

---

## 💼 Phase 7 — Recommandations métier

Les résultats de la segmentation permettent de prioriser les actions de fidélisation.

### 🔴 Risque élevé

Priorité aux clients présentant plusieurs signaux de risque, notamment :

* faible ancienneté ;
* contrat `Month-to-month` ;
* paiement par `Electronic check` ;
* certains profils utilisant `Fiber optic` ;
* faible niveau de services additionnels.

**Actions possibles :**

* contact proactif ;
* vérification de la satisfaction ;
* proposition de services additionnels pertinents ;
* encouragement vers le paiement automatique ;
* proposition d'un contrat plus long lorsque cela est pertinent.

### 🟠 Risque moyen

L'objectif est d'éviter que ces clients basculent vers le segment à risque élevé.

**Actions possibles :**

* suivi régulier ;
* amélioration de l'équipement en services ;
* proposition progressive d'un contrat plus engageant ;
* analyse de la satisfaction.

### 🟢 Risque faible

L'objectif principal est de maintenir la relation client.

**Actions possibles :**

* programme de fidélisation ;
* maintien de la qualité de service ;
* suivi de satisfaction ;
* reconnaissance de la fidélité.

> **Important :** ces recommandations constituent des pistes opérationnelles fondées sur les associations observées dans les données. Elles ne permettent pas, à elles seules, d'affirmer qu'une action donnée réduira effectivement le churn. Leur efficacité devra être validée par des expérimentations métier, notamment via des tests A/B.

---

## 🚀 Phase 8 — Application Streamlit

Le modèle a été intégré dans une application Streamlit permettant à un utilisateur métier de saisir le profil d'un client et d'obtenir une prédiction.

### Parcours utilisateur

**Saisie du profil → Prétraitement → Prédiction → Score de risque → Catégorie → Facteurs clés → Recommandations**

L'application permet notamment de renseigner :

* le profil démographique ;
* l'ancienneté ;
* le type de contrat ;
* le service Internet ;
* les charges mensuelles ;
* la méthode de paiement ;
* les services additionnels.

La prédiction utilise directement les artefacts sauvegardés lors de l'entraînement.

---

## 📦 Artefacts du modèle

Les artefacts nécessaires à l'application sont stockés dans le dossier `models/` :

```text
models/
├── churn_model.pkl
├── preprocessor.pkl
├── feature_names.pkl
└── thresholds.pkl
```

* `churn_model.pkl` : modèle Random Forest
* `preprocessor.pkl` : pipeline de prétraitement
* `feature_names.pkl` : noms des variables finales
* `thresholds.pkl` : seuils utilisés pour certaines variables dérivées

Le modèle final utilise **42 features après preprocessing**.

---

## 📁 Structure actuelle du projet

```text
UserGenerator/
│
├── app/
│   └── app.py
│
├── models/
│   ├── churn_model.pkl
│   ├── preprocessor.pkl
│   ├── feature_names.pkl
│   └── thresholds.pkl
│
├── Telco-Customer-Churn.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Technologies utilisées

| Domaine                  | Technologies                                     |
| ------------------------ | ------------------------------------------------ |
| Langage                  | Python                                           |
| Manipulation des données | Pandas, NumPy                                    |
| Visualisation            | Matplotlib, Seaborn                              |
| Machine Learning         | Scikit-learn                                     |
| Modèle final             | Random Forest                                    |
| Explainability           | SHAP                                             |
| Prétraitement            | ColumnTransformer, StandardScaler, OneHotEncoder |
| Sauvegarde               | Joblib                                           |
| Application              | Streamlit                                        |
| Environnement            | Jupyter Notebook, VS Code                        |

---

## ▶️ Installation et utilisation

### 1. Cloner le projet

```bash
git clone <URL_DU_REPOSITORY>
cd UserGenerator
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
```

### 3. Activer l'environnement sous Windows

```bash
env\Scripts\activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Lancer l'application

```bash
python -m streamlit run app/app.py
```

L'application est ensuite accessible localement à :

```text
http://localhost:8501
```

---

## ⚠️ Limites du projet

### `TotalCharges`

Dans l'application Streamlit, `TotalCharges` est estimé à partir de :

```text
tenure × MonthlyCharges
```

Cette valeur constitue une approximation pour la prédiction d'un nouveau profil.

En production, il serait préférable d'utiliser la valeur réelle provenant du système d'information client.

### Données historiques

Le modèle apprend à partir de données historiques. Les relations observées ne doivent donc pas être interprétées automatiquement comme des relations causales.

### Recommandations métier

Les recommandations proposées sont des pistes de décision. Leur impact réel doit être évalué expérimentalement.

### Données statiques

Le modèle n'est pas actuellement connecté à un système de données temps réel ni à un mécanisme automatique de réentraînement.

---

## 🚀 Perspectives d'amélioration

Plusieurs évolutions pourraient être envisagées :

* intégration des données CRM en temps réel ;
* utilisation du véritable `TotalCharges` ;
* ajout de données comportementales ;
* monitoring des performances du modèle ;
* réentraînement automatique ;
* scoring de clients en batch ;
* intégration d'un dashboard de suivi du churn ;
* mise en place de tests A/B pour mesurer l'efficacité des actions de rétention ;
* déploiement cloud.

---

## 👤 Auteur

**Fabrice BOMISSO**

Projet personnel de Data Science orienté **Machine Learning, Analytics et aide à la décision métier**.

---

## 📜 Licence

Ce projet est distribué sous licence MIT.
