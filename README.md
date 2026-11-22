<p align="center">
  <img src="assets/assets/MediSense%20AI%20README%20Guide.png" width="100%" alt="MediSense AI Project Banner">
</p>
\# 🩺 MediSense AI

\### Explainable Healthcare Risk Prediction System



An end-to-end Machine Learning application that analyses health indicators and predicts the diabetes-positive class using survey-based health data.



MediSense AI combines \*\*data preprocessing, machine learning, model evaluation, explainable AI (SHAP), and an interactive Streamlit application\*\* in one project.



> \*\*Disclaimer:\*\* This is an educational and research prototype. It is not a medical diagnostic tool, does not provide medical advice, and should not be used for clinical decision-making.



\---



\## 🚀 Project Overview



Healthcare datasets contain valuable information about lifestyle, general health, and medical conditions. Machine learning can help identify patterns within this information.



MediSense AI explores how classification algorithms can use health indicators to estimate whether a survey respondent belongs to the diabetes-positive class.



The project includes:

\- Exploratory Data Analysis (EDA)

\- Data cleaning and preprocessing

\- Logistic Regression and Random Forest classification

\- Model evaluation using multiple classification metrics

\- Feature importance analysis

\- SHAP-based model explainability

\- Model serialization using Joblib

\- Interactive prediction interface using Streamlit



\## 🎯 Objectives



1\. Analyse health indicators associated with diabetes status.

2\. Build and compare multiple classification models.

3\. Evaluate model performance beyond accuracy.

4\. Understand which features influence model predictions.

5\. Save the trained model for reuse.

6\. Build an interactive interface for predictions.



\## 📊 Dataset



\*\*Dataset:\*\* Diabetes Health Indicators Dataset  

\*\*Original data source:\*\* CDC Behavioral Risk Factor Surveillance System (BRFSS), 2015.



The project uses:



`diabetes\_binary\_health\_indicators\_BRFSS2015.csv`



\- Original records: 253,680

\- Features: 21

\- Target variable: `Diabetes\_binary`

\- Task: Binary classification



The dataset contains survey-based information about health conditions, lifestyle, and demographic indicators.



\### Data preprocessing



\- Checked dataset structure and data types.

\- Checked for missing values.

\- Identified and removed exact duplicate rows.

\- Separated independent variables and target variable.

\- Used stratified train-test splitting.

\- Applied StandardScaler to Logistic Regression features.



After removing exact duplicate rows:



\- Records retained: 229,474

\- Training records: 183,579

\- Testing records: 45,895



\*\*Important data consideration:\*\* Identical survey responses do not necessarily prove that two records belong to the same individual. Deduplication is therefore a preprocessing choice that should be evaluated further.



\## 🧠 Machine Learning Models



Two classification algorithms were implemented and compared.



\### 1. Logistic Regression



\- Used StandardScaler for feature scaling.

\- Applied class weighting to address class imbalance.

\- Used the model's predicted probabilities for ROC-AUC evaluation.



\### 2. Random Forest Classifier



\- Used 200 decision trees.

\- Maximum tree depth: 18.

\- Minimum samples per leaf: 2.

\- Applied balanced subsampling class weights.

\- Used parallel processing.



\## 📈 Model Performance



Both models were evaluated on the same held-out test dataset.



| Evaluation Metric | Logistic Regression | Random Forest |

|---|---:|---:|

| Accuracy | 71.43% | \*\*78.74%\*\* |

| Precision | 31.83% | \*\*37.48%\*\* |

| Recall | \*\*76.01%\*\* | 58.34% |

| F1-Score | 44.87% | \*\*45.64%\*\* |

| ROC-AUC | \*\*81.06%\*\* | 80.63% |



\### Performance interpretation



\- Random Forest achieved higher accuracy, precision, and F1-score.

\- Logistic Regression achieved higher recall and ROC-AUC.

\- Logistic Regression identified a larger proportion of positive-class cases but also generated more false positives.

\- Random Forest provided a better balance of precision and recall according to its F1-score.



\*\*Model selection:\*\* Random Forest is used in the interactive application. However, it is not universally superior. The appropriate model depends on the intended use case and the trade-off between false positives and false negatives.



\## 🔍 Explainable AI (SHAP)



To explore how the Random Forest model makes predictions, SHAP (SHapley Additive exPlanations) was implemented.



The analysis included:

\- SHAP TreeExplainer

\- SHAP summary plot

\- SHAP feature importance bar plot



The exploratory SHAP analysis highlighted features such as:

\- High blood pressure

\- General health

\- BMI

\- High cholesterol

\- Age category



SHAP values explain the model's behaviour; they do not establish medical causation.



\*\*Implementation note:\*\* SHAP was calculated using an approximate method on a sample of 20 test observations. The results should therefore be treated as exploratory rather than definitive global explanations.



\## 💻 Interactive Application



The project includes a Streamlit interface where users can enter health indicators and receive a model prediction.



\### Application features



\- Health-condition inputs

\- Lifestyle indicators

\- BMI and general health inputs

\- Age, education, and income category inputs

\- Predicted class

\- Estimated model probability



The application uses the saved Random Forest model.



The displayed probability is a model-estimated probability for the positive class. It is not a calibrated or clinically validated risk score.



\## 🛠️ Technology Stack



| Category | Technologies |

|---|---|

| Programming | Python |

| Data Analysis | Pandas, NumPy |

| Visualization | Matplotlib, Seaborn |

| Machine Learning | Scikit-learn |

| Explainable AI | SHAP |

| Model Serialization | Joblib |

| Application | Streamlit |

| Development | Jupyter Notebook, Anaconda |



\## 📁 Project Structure



```text

MediSense\_AI/

│

├── app.py

├── README.md

├── requirements.txt

│

├── 01\_Diabetes\_Risk\_Predictionn.ipynb

│

├── models/

│   ├── random\_forest\_diabetes.pkl

│   ├── logistic\_regression\_diabetes.pkl

│   └── standard\_scaler.pkl

│

└── data/

&#x20;   └── diabetes\_binary\_health\_indicators\_BRFSS2015.csv

```



The dataset is listed here for reference. It may be downloaded separately rather than committed to the repository.



\## ⚙️ Installation and Setup



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd MediSense\_AI

```



\### 2. Create and activate a Conda environment



```bash

conda create -n medisense python=3.11 -y

conda activate medisense

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Download the dataset



Download the selected CSV file from the dataset source and place it in the location expected by the notebook.



Dataset source: \[Diabetes Health Indicators Dataset – Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)



Official survey documentation: \[CDC BRFSS 2015](https://www.cdc.gov/brfss/annual\_data/annual\_2015.html)



\### 5. Run the notebook



```bash

jupyter notebook

```



Open the diabetes prediction notebook and run the cells in order to reproduce the analysis and model training.



\### 6. Launch the Streamlit application



```bash

streamlit run app.py

```



Open the local URL displayed in the terminal.



\*\*Note:\*\* The Streamlit application expects the trained Random Forest model to exist at `models/random\_forest\_diabetes.pkl`.



\## ⚠️ Limitations



\- The dataset is based on self-reported 2015 survey information, not clinical records or laboratory measurements.

\- The dataset may not represent current populations or all demographic groups.

\- Class imbalance affects the precision and recall trade-off.

\- The model has not undergone external clinical validation.

\- Predicted probabilities have not been calibrated.

\- The current SHAP analysis uses a small sample and approximate computation.

\- Feature importance does not imply causation.



\## 🔮 Future Improvements



\- Perform hyperparameter tuning and threshold optimization.

\- Evaluate Precision-Recall AUC and probability calibration.

\- Compare performance across demographic subgroups.

\- Validate the model on an independent dataset.

\- Expand explainability with individual prediction explanations.

\- Integrate a healthcare-document RAG system for evidence-based information retrieval.



\## 👩‍💻 Author



\*\*Divyanshi Sharma\*\*  

MBA – Artificial Intelligence \& Data Science



Interested in Machine Learning, Data Analytics, Explainable AI, and responsible AI applications.



\---



\### ⭐ Project Note



MediSense AI demonstrates an end-to-end machine learning workflow, from raw survey data and model development to explainability, model deployment, and interactive predictions.

