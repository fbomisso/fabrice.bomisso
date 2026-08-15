import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# app.py → Portfolio/models/app/
# modèles → Portfolio/models/
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR


# ============================================================
# CHARGEMENT DES ARTEFACTS
# ============================================================

@st.cache_resource
def load_artifacts():
    model = joblib.load(MODELS_DIR / "churn_model.pkl")
    preprocessor = joblib.load(MODELS_DIR / "preprocessor.pkl")
    feature_names = joblib.load(MODELS_DIR / "feature_names.pkl")
    thresholds = joblib.load(MODELS_DIR / "thresholds.pkl")

    return model, preprocessor, feature_names, thresholds


try:
    model, preprocessor, feature_names, thresholds = load_artifacts()
except Exception as e:
    st.error(f"Erreur lors du chargement des modèles : {e}")
    st.stop()


# ============================================================
# FEATURE ENGINEERING
# ============================================================

def create_features(data):
    df = data.copy()

    # 1. Ancienneté
    df["tenure_years"] = df["tenure"] / 12

    df["is_new_customer"] = (
        df["tenure"] <= 6
    ).astype(int)

    df["is_young_customer"] = (
        df["tenure"] <= 12
    ).astype(int)

    # 2. Charges mensuelles
    df["high_monthly_charges"] = (
        df["MonthlyCharges"] > 89.85
    ).astype(int)

    df["low_monthly_charges"] = (
        df["MonthlyCharges"] < 35.50
    ).astype(int)

    # 3. Nombre de services
    services_cols = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    df["num_services"] = (
        df[services_cols] == "Yes"
    ).sum(axis=1)

    df["has_multiple_services"] = (
        df["num_services"] >= 2
    ).astype(int)

    # 4. Support et sécurité
    df["has_tech_support"] = (
        df["TechSupport"] == "Yes"
    ).astype(int)

    df["has_security"] = (
        df["OnlineSecurity"] == "Yes"
    ).astype(int)

    # 5. Paiement automatique
    automatic_payment = [
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]

    df["is_automatic_payment"] = (
        df["PaymentMethod"].isin(automatic_payment)
    ).astype(int)

    # 6. Contrat long terme
    df["is_long_contract"] = (
        df["Contract"].isin([
            "One year",
            "Two year"
        ])
    ).astype(int)

    # 7. Profil à risque
    df["risky_profile"] = (
        (df["is_new_customer"] == 1) &
        (df["Contract"] == "Month-to-month")
    ).astype(int)

    return df


# ============================================================
# RECOMMANDATIONS
# ============================================================

def get_recommendations(row, risk):
    recommendations = []

    if risk == "ÉLEVÉ":
        if row["Contract"] == "Month-to-month":
            recommendations.append(
                "Proposer une offre de contrat d'un an."
            )

        if row["PaymentMethod"] == "Electronic check":
            recommendations.append(
                "Encourager le passage au paiement automatique."
            )

        if row["OnlineSecurity"] != "Yes":
            recommendations.append(
                "Proposer l'option OnlineSecurity."
            )

        if row["TechSupport"] != "Yes":
            recommendations.append(
                "Proposer l'option TechSupport."
            )

        if row["tenure"] <= 6:
            recommendations.append(
                "Déclencher un programme d'accompagnement des nouveaux clients."
            )

        if not recommendations:
            recommendations.append(
                "Déclencher une campagne personnalisée de rétention."
            )

    elif risk == "MOYEN":
        recommendations.append(
            "Renforcer l'engagement du client avec une offre personnalisée."
        )

        if row["Contract"] == "Month-to-month":
            recommendations.append(
                "Proposer une évolution vers un contrat long terme."
            )

        if row["OnlineSecurity"] != "Yes":
            recommendations.append(
                "Proposer des services additionnels."
            )

    else:
        recommendations.append(
            "Maintenir la satisfaction et la fidélisation du client."
        )

        recommendations.append(
            "Valoriser la fidélité avec des offres personnalisées."
        )

    return recommendations


# ============================================================
# INTERFACE
# ============================================================

st.title("📊 Customer Churn Prediction")

st.markdown(
    """
Cette application estime le **risque de churn d'un client télécom**
à partir de son profil, de ses services, de son contrat et de son mode
de paiement.
"""
)

st.divider()


# ============================================================
# PROFIL CLIENT
# ============================================================

st.subheader("👤 Profil client")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Genre",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1],
        format_func=lambda x: "Oui" if x == 1 else "Non"
    )

with col2:
    partner = st.selectbox(
        "Partenaire",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Personnes à charge",
        ["Yes", "No"]
    )

with col3:
    tenure = st.number_input(
        "Ancienneté (mois)",
        min_value=0,
        max_value=72,
        value=12
    )

    phone_service = st.selectbox(
        "Service téléphonique",
        ["Yes", "No"]
    )


# ============================================================
# SERVICES
# ============================================================

st.subheader("📡 Services")

col1, col2, col3 = st.columns(3)

with col1:
    multiple_lines = st.selectbox(
        "Lignes multiples",
        ["No", "Yes", "No phone service"]
    )

    internet_service = st.selectbox(
        "Service Internet",
        ["DSL", "Fiber optic", "No"]
    )

with col2:
    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

with col3:
    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

col1, col2 = st.columns(2)

with col1:
    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

with col2:
    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )


# ============================================================
# CONTRAT ET PAIEMENT
# ============================================================

st.subheader("💳 Contrat & paiement")

col1, col2, col3 = st.columns(3)

with col1:
    contract = st.selectbox(
        "Contrat",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    payment_method = st.selectbox(
        "Méthode de paiement",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col3:
    paperless_billing = st.selectbox(
        "Facturation électronique",
        ["Yes", "No"]
    )


# ============================================================
# CHARGES
# ============================================================

st.subheader("💰 Charges")

col1, col2 = st.columns(2)

with col1:
    monthly_charges = st.number_input(
        "Charges mensuelles",
        min_value=0.0,
        max_value=200.0,
        value=70.0,
        step=0.01
    )

with col2:
    total_charges = st.number_input(
        "Charges totales",
        min_value=0.0,
        max_value=10000.0,
        value=float(tenure * monthly_charges),
        step=0.01
    )


# ============================================================
# PREDICTION
# ============================================================

st.divider()

if st.button(
    "🔮 Prédire le risque de churn",
    type="primary",
    use_container_width=True
):

    input_data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone_service == "Yes" else 0,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": 1 if paperless_billing == "Yes" else 0,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    try:
        features = create_features(input_data)

        numeric_features = [
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "PaperlessBilling",
            "MonthlyCharges",
            "TotalCharges",
            "tenure_years",
            "is_new_customer",
            "is_young_customer",
            "high_monthly_charges",
            "low_monthly_charges",
            "num_services",
            "has_multiple_services",
            "has_tech_support",
            "has_security",
            "is_automatic_payment",
            "is_long_contract",
            "risky_profile"
        ]

        categorical_features = [
            "gender",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaymentMethod"
        ]

        X = features[
            numeric_features + categorical_features
        ]

        X_processed = preprocessor.transform(X)

        churn_probability = model.predict_proba(
            X_processed
        )[0, 1]

        score = churn_probability * 100

        if churn_probability >= thresholds["risk_high"]:
            risk = "ÉLEVÉ"
            risk_icon = "🔴"
        elif churn_probability >= thresholds["risk_medium"]:
            risk = "MOYEN"
            risk_icon = "🟠"
        else:
            risk = "FAIBLE"
            risk_icon = "🟢"

        st.subheader("🎯 Résultat")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Score de risque",
                f"{score:.1f}%"
            )

        with col2:
            st.metric(
                "Niveau de risque",
                f"{risk_icon} {risk}"
            )

        st.progress(
            min(max(churn_probability, 0.0), 1.0)
        )

        st.subheader("💡 Recommandations métier")

        recommendations = get_recommendations(
            input_data.iloc[0],
            risk
        )

        for recommendation in recommendations:
            st.info(recommendation)

        st.subheader("🔎 Profil analysé")

        profile_cols = st.columns(4)

        profile_cols[0].metric(
            "Ancienneté",
            f"{tenure} mois"
        )

        profile_cols[1].metric(
            "Services",
            int(features["num_services"].iloc[0])
        )

        profile_cols[2].metric(
            "Contrat",
            contract
        )

        profile_cols[3].metric(
            "Charges mensuelles",
            f"{monthly_charges:.2f}"
        )

    except Exception as e:
        st.error(
            f"Une erreur est survenue pendant la prédiction : {e}"
        )
        st.exception(e)