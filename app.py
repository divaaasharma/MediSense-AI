import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="MediSense AI",
    page_icon="🩺",
    layout="wide"
)

# ---------------------------------
# LOAD TRAINED MODEL
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "random_forest_diabetes.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# ---------------------------------
# FEATURE ORDER
# ---------------------------------

FEATURE_COLUMNS = [
    "HighBP",
    "HighChol",
    "CholCheck",
    "BMI",
    "Smoker",
    "Stroke",
    "HeartDiseaseorAttack",
    "PhysActivity",
    "Fruits",
    "Veggies",
    "HvyAlcoholConsump",
    "AnyHealthcare",
    "NoDocbcCost",
    "GenHlth",
    "MentHlth",
    "PhysHlth",
    "DiffWalk",
    "Sex",
    "Age",
    "Education",
    "Income"
]

# ---------------------------------
# APPLICATION HEADER
# ---------------------------------

st.title("🩺 MediSense AI")

st.subheader("Explainable Healthcare Risk Prediction System")

st.write(
    "An AI-powered research prototype that analyses "
    "health indicators using a trained Machine Learning model."
)

st.info(
    "This application is for educational and research purposes only. "
    "It does not provide medical diagnosis or replace professional advice."
)

st.divider()

# ---------------------------------
# INPUT FORM
# ---------------------------------

st.header("Enter Health Indicators")

with st.form("health_form"):

    col1, col2 = st.columns(2)

    # Binary feature inputs

    with col1:

        st.subheader("Health Conditions")

        high_bp = st.checkbox("High Blood Pressure")

        high_chol = st.checkbox("High Cholesterol")

        chol_check = st.checkbox("Cholesterol Check in Last 5 Years", value=True)

        smoker = st.checkbox("Smoker")

        stroke = st.checkbox("History of Stroke")

        heart_disease = st.checkbox("Heart Disease or Heart Attack")

        diff_walk = st.checkbox("Difficulty Walking or Climbing Stairs")

        sex = st.selectbox(
            "Sex",
            ["Female", "Male"]
        )

    with col2:

        st.subheader("Lifestyle and Healthcare")

        phys_activity = st.checkbox("Physical Activity")

        fruits = st.checkbox("Consumes Fruits Daily")

        veggies = st.checkbox("Consumes Vegetables Daily")

        heavy_alcohol = st.checkbox("Heavy Alcohol Consumption")

        healthcare = st.checkbox("Has Healthcare Coverage", value=True)

        no_doc_cost = st.checkbox("Unable to Visit Doctor Due to Cost")

    st.divider()

    # Numerical and ordinal features

    st.subheader("Additional Health Information")

    col3, col4 = st.columns(2)

    with col3:

        bmi = st.number_input(
            "BMI",
            min_value=12.0,
            max_value=98.0,
            value=27.0,
            step=0.5
        )

        gen_health = st.selectbox(
            "General Health",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Excellent",
                2: "Very Good",
                3: "Good",
                4: "Fair",
                5: "Poor"
            }[x]
        )

        age = st.slider(
            "Age Category Code",
            1, 13, 8
        )

        education = st.slider(
            "Education Category Code",
            1, 6, 4
        )

        income = st.slider(
            "Income Category Code",
            1, 8, 5
        )

    with col4:

        ment_health = st.slider(
            "Days of Poor Mental Health (Last 30 Days)",
            0, 30, 0
        )

        phys_health = st.slider(
            "Days of Poor Physical Health (Last 30 Days)",
            0, 30, 0
        )

    submitted = st.form_submit_button(
        "Predict Diabetes Status",
        use_container_width=True
    )

# ---------------------------------
# PREDICTION
# ---------------------------------

if submitted:

    input_data = {
        "HighBP": int(high_bp),
        "HighChol": int(high_chol),
        "CholCheck": int(chol_check),
        "BMI": bmi,
        "Smoker": int(smoker),
        "Stroke": int(stroke),
        "HeartDiseaseorAttack": int(heart_disease),
        "PhysActivity": int(phys_activity),
        "Fruits": int(fruits),
        "Veggies": int(veggies),
        "HvyAlcoholConsump": int(heavy_alcohol),
        "AnyHealthcare": int(healthcare),
        "NoDocbcCost": int(no_doc_cost),
        "GenHlth": gen_health,
        "MentHlth": ment_health,
        "PhysHlth": phys_health,
        "DiffWalk": int(diff_walk),
        "Sex": 0 if sex == "Female" else 1,
        "Age": age,
        "Education": education,
        "Income": income
    }

    input_df = pd.DataFrame(
        [input_data],
        columns=FEATURE_COLUMNS
    )

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.divider()

    st.header("Prediction Results")

    col5, col6 = st.columns(2)

    with col5:

        if prediction == 1:

            st.warning(
                "Model Prediction: Diabetes-positive class"
            )

        else:

            st.success(
                "Model Prediction: Diabetes-negative class"
            )

    with col6:

        st.metric(
            "Estimated Model Probability",
            f"{probability * 100:.2f}%"
        )

    st.caption(
        "This probability is the model's estimated probability "
        "for the positive class. It is not a validated clinical risk score."
    )

    st.write(
        "The prediction is based on patterns learned from "
        "the CDC BRFSS 2015 survey dataset."
    )

# ---------------------------------
# FOOTER
# ---------------------------------

st.divider()

st.caption(
    "MediSense AI | Machine Learning Research Prototype | "
    "Educational Use Only"
)