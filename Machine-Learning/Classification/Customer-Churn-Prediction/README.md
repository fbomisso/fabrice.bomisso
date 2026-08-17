````markdown
# Customer Churn Prediction | From Data to Business Decision

## Présentation

Ce projet porte sur la prédiction du churn client dans le secteur des télécommunications.

L'objectif est d'identifier les clients présentant un risque de départ, d'analyser les facteurs associés au churn et de transformer les résultats du modèle en informations utiles pour les actions de fidélisation.

Le projet couvre l'ensemble du processus, de la préparation des données jusqu'au déploiement d'une application de prédiction avec Streamlit.

**Problématique :** comment identifier suffisamment tôt les clients présentant un risque élevé de churn afin de permettre aux équipes métier de prioriser leurs actions de fidélisation ?

**Solution :** un modèle de classification basé sur un **Random Forest**, complété par une analyse SHAP, une segmentation des clients selon leur niveau de risque et une application Streamlit permettant d'effectuer des prédictions individuelles.

---

## Objectifs du projet

- Analyser les facteurs associés au churn client
- Nettoyer et préparer les données
- Créer de nouvelles variables pour améliorer l'analyse
- Comparer plusieurs modèles de classification
- Sélectionner le modèle adapté à l'objectif métier
- Interpréter les prédictions avec SHAP
- Segmenter les clients selon leur niveau de risque
- Formuler des recommandations à partir des résultats
- Déployer le modèle dans une application Streamlit

---

## Dataset

**Source :** IBM Telco Customer Churn Dataset

**Dataset utilisé :** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

**Taille :**

- 7 043 clients
- 21 variables initiales
- Variable cible : `Churn`

Le dataset contient notamment des informations sur :

- le profil démographique ;
- l'ancienneté ;
- les services souscrits ;
- le type de contrat ;
- les méthodes de paiement ;
- les charges mensuelles et totales.

---

## Méthodologie

Le projet suit le processus suivant :

**Données → Nettoyage → EDA → Feature Engineering → Modélisation → Évaluation → SHAP → Segmentation → Recommandations métier → Application Streamlit**

---

## 01. Nettoyage des données

Plusieurs contrôles ont été réalisés avant la modélisation.

### Principales opérations

- Conversion de `TotalCharges` en variable numérique
- Transformation de `Churn` en variable binaire
- Traitement des valeurs manquantes
- Vérification des types de données
- Préparation des variables catégorielles et numériques

Les valeurs manquantes observées dans `TotalCharges` correspondent aux clients ayant une ancienneté nulle. Elles ont été traitées en tenant compte de ce contexte.

---

## 02. Feature Engineering

Plusieurs variables ont été créées pour compléter les informations disponibles dans le dataset.

Principales variables utilisées :

- `tenure_years`
- `is_new_customer`
- `is_young_customer`
- `high_monthly_charges`
- `low_monthly_charges`
- `num_services`
- `has_multiple_services`
- `has_tech_support`
- `has_security`
- `is_automatic_payment`
- `is_long_contract`
- `risky_profile`

Ces variables décrivent notamment l'ancienneté du client, son niveau d'équipement, son engagement contractuel et certains profils associés à un risque plus important.

---

## 03. Analyse exploratoire

L'analyse exploratoire a permis d'identifier plusieurs associations avec le churn.

| Facteur | Observation |
| --- | --- |
| **Ancienneté** | Les clients les moins anciens présentent davantage de churn |
| **Contrat** | Les contrats `Month-to-month` sont davantage associés au churn |
| **Internet** | Le taux de churn est plus élevé chez les clients `Fiber optic` dans les données analysées |
| **Paiement** | `Electronic check` présente un taux de churn élevé |
| **Services** | Certains services additionnels sont associés à un churn plus faible |

Ces résultats décrivent les tendances observées dans les données. Une association entre deux variables ne permet pas à elle seule d'établir une relation causale.

---

## 04. Modélisation

Deux modèles de classification ont été étudiés :

- **Logistic Regression**
- **Random Forest**

Le **Recall** a été particulièrement pris en compte, car l'objectif est de détecter le plus grand nombre possible de clients susceptibles de churner.

### Random Forest : modèle retenu

| Métrique | Résultat |
| --- | ---: |
| Accuracy | 79,0 % |
| Recall | **77,81 %** |
| F1-score | **63,75 %** |
| ROC-AUC | **0,85** |

Le Random Forest a été retenu en raison de sa capacité à détecter une proportion importante des clients ayant réellement churné.

Le modèle obtient un **Recall de 77,81 %** sur le jeu de test.

---

## 05. Explainability avec SHAP

SHAP a été utilisé pour analyser la contribution des variables aux prédictions du modèle.

Les principales variables identifiées sont notamment :

1. `is_long_contract`
2. `InternetService_Fiber optic`
3. `tenure_years`
4. `tenure`
5. `Contract_Two year`

Les résultats mettent notamment en évidence l'importance de facteurs liés à l'engagement contractuel, à l'ancienneté et au service Internet dans les prédictions du modèle.

SHAP apporte donc une lecture plus détaillée des prédictions du Random Forest.

---

## 06. Segmentation des clients à risque

Le modèle a été utilisé pour calculer un score de risque pour les **1 409 clients du jeu de test**.

Les clients ont ensuite été répartis en trois catégories :

| Catégorie | Clients | Churn réel | Score moyen | Ancienneté moyenne |
| --- | ---: | ---: | ---: | ---: |
| 🔴 **ÉLEVÉ** | 295 | **66,4 %** | 81,4 % | 8,1 mois |
| 🟠 **MOYEN** | 332 | **35,8 %** | 55,9 % | 23,6 mois |
| 🟢 **FAIBLE** | 782 | **7,5 %** | 15,5 % | 44,5 mois |

Le groupe **ÉLEVÉ** présente un taux de churn réel de **66,4 %**, contre **7,5 %** pour le groupe **FAIBLE**.

Cette différence montre que le score produit par le modèle permet de distinguer plusieurs niveaux de risque sur le jeu de test.

---

## 07. Recommandations métier

Les résultats de la segmentation peuvent servir à prioriser les actions de fidélisation.

### Risque élevé

Les clients de cette catégorie présentent plusieurs signaux associés au churn, notamment :

- faible ancienneté ;
- contrat `Month-to-month` ;
- paiement par `Electronic check` ;
- certains profils utilisant `Fiber optic` ;
- faible niveau de services additionnels.

**Actions possibles :**

- contact proactif ;
- vérification de la satisfaction ;
- proposition de services additionnels pertinents ;
- encouragement vers le paiement automatique ;
- proposition d'un contrat plus long lorsque cela est pertinent.

### Risque moyen

L'objectif est de suivre ces clients avant qu'ils n'atteignent un niveau de risque plus élevé.

**Actions possibles :**

- suivi régulier ;
- amélioration de l'équipement en services ;
- proposition progressive d'un contrat plus engageant ;
- analyse de la satisfaction.

### Risque faible

L'objectif est principalement de maintenir la relation avec ces clients.

**Actions possibles :**

- programme de fidélisation ;
- maintien de la qualité de service ;
- suivi de satisfaction ;
- reconnaissance de la fidélité.

> **Important :** ces recommandations sont basées sur les associations observées dans les données. Elles ne permettent pas d'affirmer qu'une action donnée réduira effectivement le churn. Leur efficacité devra être vérifiée avec des expérimentations métier, notamment des tests A/B.

---

## 08. Application Streamlit

Le modèle a été intégré dans une application Streamlit permettant de saisir le profil d'un client et d'obtenir une prédiction.

### Parcours utilisateur

**Saisie du profil → Prétraitement → Prédiction → Score de risque → Catégorie → Facteurs clés → Recommandations**

L'application permet notamment de renseigner :

- le profil démographique ;
- l'ancienneté ;
- le type de contrat ;
- le service Internet ;
- les charges mensuelles ;
- la méthode de paiement ;
- les services additionnels.

La prédiction utilise les artefacts sauvegardés lors de l'entraînement.

---

## Artefacts du modèle

Les fichiers nécessaires à l'application sont stockés dans le dossier `models/` :

```text
models/
├── churn_model.pkl
├── preprocessor.pkl
├── feature_names.pkl
└── thresholds.pkl
````

* `churn_model.pkl` : modèle Random Forest
* `preprocessor.pkl` : pipeline de prétraitement
* `feature_names.pkl` : noms des variables finales
* `thresholds.pkl` : seuils utilisés pour certaines variables dérivées

Le modèle final utilise **42 features après preprocessing**.

---

## Structure du projet

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

## Technologies utilisées

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

## Installation et utilisation

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

## Limites du projet

### `TotalCharges`

Dans l'application Streamlit, `TotalCharges` est estimé à partir de :

```text
tenure × MonthlyCharges
```

Cette valeur constitue une approximation pour la prédiction d'un nouveau profil.

En production, il serait préférable d'utiliser la valeur réelle provenant du système d'information client.

### Données historiques

Le modèle est entraîné sur des données historiques. Les relations observées ne doivent pas être interprétées automatiquement comme des relations causales.

### Recommandations métier

Les recommandations proposées sont des pistes de décision. Leur impact réel doit être évalué avec des données métier et des expérimentations.

### Données statiques

Le modèle n'est actuellement connecté ni à un système de données temps réel ni à un mécanisme automatique de réentraînement.

---

## Perspectives d'amélioration

Plusieurs évolutions peuvent être envisagées :

* intégration des données CRM en temps réel ;
* utilisation du véritable `TotalCharges` ;
* ajout de données comportementales ;
* monitoring des performances du modèle ;
* réentraînement automatique ;
* scoring des clients en batch ;
* intégration d'un dashboard de suivi du churn ;
* mise en place de tests A/B pour mesurer l'efficacité des actions de rétention ;
* déploiement cloud.

---

## Auteur

**Fabrice BOMISSO**

Projet personnel de Data Science orienté **Machine Learning, Analytics et aide à la décision métier**.

---

## Licence

Ce projet est distribué sous licence MIT.

```
```
