<p align="center">
  <img src="assets/assets/MediSense%20AI%20README%20Guide.png" width="100%" alt="MediSense AI Project Banner">
</p>

<h1 align="center">MediSense AI</h1>

<h3 align="center">Explainable Healthcare Risk Prediction System</h3>

<p align="center">
  An interactive machine learning research prototype that predicts diabetes-positive class probability using health and lifestyle indicators.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-orange">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red">
  <img src="https://img.shields.io/badge/SHAP-Explainable%20AI-purple">
  <img src="https://img.shields.io/badge/Project-Research%20Prototype-green">
</p>

---

## 1. Project Overview

**MediSense AI** is an explainable machine learning project developed to explore patterns associated with diabetes status using health and lifestyle indicators.

The system combines predictive modelling, model evaluation, and explainability techniques to make machine learning outputs easier to understand.

### Key Objectives

- Predict diabetes-positive class status using health and lifestyle indicators.
- Compare Logistic Regression and Random Forest classification models.
- Evaluate model performance using multiple classification metrics.
- Interpret model behaviour using SHAP explainability.
- Provide an interactive prediction interface using Streamlit.
- Demonstrate a reproducible machine learning workflow.

---

## 2. Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Explainable AI | SHAP |
| Model Persistence | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook, Anaconda |
| Version Control | Git, GitHub, Git LFS |

---

## 3. Dataset Information

**Dataset:** Diabetes Health Indicators Dataset

**Original Source:** CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015.

| Attribute | Details |
|---|---|
| Original Records | 253,680 |
| Features | 21 |
| Target Variable | Diabetes_binary |
| Original Classes | 0 and 1 |
| Original Dataset Columns | 22 |
| Records After Duplicate Removal | 229,474 |
| Missing Values | None |

### Target Variable

- `0` – Diabetes-negative class
- `1` – Diabetes-positive class

### Selected Features

The dataset includes indicators such as:

- BMI
- High Blood Pressure
- High Cholesterol
- Physical Activity
- Smoking Status
- General Health
- Physical Health
- Mental Health
- Age Group
- Education
- Income

**Important:** The dataset contains self-reported survey information. Age, education, and income are represented using category codes.

---

## 4. Project Workflow

The project follows a structured machine learning pipeline:

1. **Data Loading** – Import the BRFSS dataset using Pandas.
2. **Data Cleaning** – Inspect data quality and remove exact duplicate rows.
3. **Exploratory Data Analysis** – Examine distributions and target-class imbalance.
4. **Preprocessing** – Split the dataset using stratified sampling and scale features for Logistic Regression.
5. **Model Training** – Train Logistic Regression and Random Forest classifiers.
6. **Model Evaluation** – Compare classification performance.
7. **Explainability** – Use feature importance and SHAP to interpret model behaviour.
8. **Model Persistence** – Save trained models using Joblib.
9. **Prediction Function** – Build a reusable prediction function.
10. **Deployment Interface** – Develop an interactive Streamlit application.

---

## 5. Model Performance

Two classification algorithms were trained and evaluated on the same test dataset.

| Evaluation Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 71.43% | 78.74% |
| Precision | 31.83% | 37.48% |
| Recall | 76.01% | 58.34% |
| F1-Score | 44.87% | 45.64% |
| ROC-AUC | 81.06% | 80.63% |

### Model Comparison

**Logistic Regression**
- Achieved higher recall and ROC-AUC.
- Identified a larger proportion of diabetes-positive cases.
- Produced more false-positive predictions.

**Random Forest**
- Achieved higher accuracy, precision, and F1-score.
- Captured non-linear relationships in the dataset.
- Was selected for the interactive prediction application.

**Model Selection:** Random Forest was selected for the application because it achieved the higher F1-score and accuracy. However, Logistic Regression achieved higher recall, making the trade-off important for any screening-oriented application.

---

## 6. Explainable AI – SHAP

SHAP (SHapley Additive exPlanations) was used to explore how input features influence the Random Forest model's predictions.

### Key Model Insights

The model's feature importance analysis highlighted:

- BMI
- General Health
- High Blood Pressure
- Age Group
- Income
- Physical Health
- High Cholesterol

SHAP summary plots were also generated to examine the contribution of individual features to model predictions.

**Note:** Feature importance and SHAP values describe model behaviour. They do not establish medical causation.

---

## 7. Interactive Application

MediSense AI includes a Streamlit interface where users can enter health and lifestyle information and receive a model prediction.

### Application Features

- Interactive health-indicator inputs.
- Random Forest-based prediction.
- Estimated probability for the diabetes-positive class.
- Simple prediction-result presentation.
- Educational-use disclaimer.

The application uses a default classification threshold of 0.5.

---

## 8. Project Structure

```text
MediSense-AI/
│
├── assets/
│   └── assets/
│       └── MediSense AI README Guide.png
│
├── models/
│   ├── logistic_regression_diabetes.pkl
│   ├── random_forest_diabetes.pkl
│   └── standard_scaler.pkl
│
├── 01_Diabetes_Risk_Predictionn.ipynb
├── app.py
├── diabetes_binary_health_indicators_BRFSS2015.csv
├── requirements.txt
├── README.md
└── .gitattributes
```

---

## 9. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/divaaasharma/MediSense-AI.git
cd MediSense-AI
```

### Step 2: Install Git LFS

The trained model files are stored using Git Large File Storage.

```bash
git lfs install
git lfs pull
```

### Step 3: Create a Virtual Environment

```bash
conda create -n medisense python=3.11 -y
conda activate medisense
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

---

## 10. Limitations and Future Improvements

### Current Limitations

- The dataset is based on self-reported survey information.
- The data originates from the 2015 BRFSS survey.
- The model is not clinically validated.
- Predicted probabilities have not been clinically validated or calibrated.
- SHAP analysis was performed on a small sample using approximate computation.
- Removing duplicate rows may affect the representation of survey responses.

### Future Enhancements

- Perform hyperparameter optimization.
- Explore threshold tuning and probability calibration.
- Evaluate additional classification algorithms.
- Improve model explainability and individual prediction analysis.
- Expand the application with more interactive visualizations.
- Validate performance on independent and more recent datasets.

---

## 11. Important Disclaimer

MediSense AI is an educational machine learning research prototype.

It is **not a medical diagnostic tool**, does not replace professional medical advice, and should not be used to make clinical decisions.

The estimated probability represents the model's output based on patterns learned from the dataset. It is not an individual's clinically validated diabetes risk.

---

## 12. Author

**Divyanshi Sharma**

MBA – Artificial Intelligence & Data Science

### Connect

- GitHub: [@divaaasharma](https://github.com/divaaasharma)
- Project Repository: [MediSense AI](https://github.com/divaaasharma/MediSense-AI)

---

<p align="center">
  <b>MediSense AI</b><br>
  Making machine learning predictions more interpretable and accessible.
</p>
