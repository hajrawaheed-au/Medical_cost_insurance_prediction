# 🩺 Medical Insurance Charges Prediction

An end-to-end Machine Learning project that predicts **medical insurance charges** based on an individual's demographic and health-related information. This project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, model persistence, and prediction through a terminal-based interface.

---

# 📌 Project Overview

The objective of this project is to build a regression model capable of estimating medical insurance charges using personal and health-related attributes. Multiple regression models were explored, and **Random Forest Regressor** was selected as the final model due to its superior performance.

---

## 📊 Dataset

This project uses the **Medical Cost Personal Dataset**, which contains demographic and health-related information of individuals along with their corresponding medical insurance charges. The dataset is used to build a regression model that predicts insurance costs based on personal attributes.

**Target Variable**

- `charges`

**Features**

- Age
- Sex
- BMI
- Children
- Smoker
- Region

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Data inspection
- Missing value analysis
- Duplicate value analysis
- Descriptive statistics
- Distribution analysis
- Categorical feature analysis
- Correlation analysis
- Outlier detection

---

## ⚙️ Data Preprocessing

Only Label Encoding was applied to sex and smoker because they contain only two categories. One-Hot Encoding was applied to region because its categories have no natural order. No additional data cleaning or feature combination was performed because the dataset was already clean and the existing features were sufficient.


---

## 🤖 Model Selection

The following regression models were explored:

- Linear Regression
- Decision Tree Regressor
- **Random Forest Regressor (Final Model)**

Random Forest Regressor was selected because it achieved the best overall performance on the dataset.

---

## 📈 Model Performance

The final Random Forest Regressor was evaluated using both **5-Fold Cross Validation** and **Testing Data**.

| Metric | Validation Data | Testing Data |
|---|---:|---:|
| **R² Score** | **0.852** | **0.869** |
| **MAE** | — | **2608.91** |
| **RMSE** | — | **4506.74** |
| **MSE** | — | **20,310,720** |

### Validation Accuracy

The model achieved an average **R² score of 0.852** across 5-fold cross-validation, with a standard deviation of **0.02687**.

This indicates that the model maintained relatively consistent performance across different validation folds.

### Testing Data Accuracy

On the unseen testing data, the model achieved an **R² score of 0.869**, indicating that it explains approximately **86.9% of the variation** in medical insurance charges.

The testing results were:

- **R² Score:** 0.869
- **MAE:** 2608.91
- **RMSE:** 4506.74
- **MSE:** approximately 20,310,720

Overall, the similar validation and testing R² scores suggest that the model generalizes reasonably well to unseen data.
## 💾 Model Persistence

The trained model is saved using **Joblib** as:

```text
models/random_forest_model.pkl
````

This allows predictions without retraining the model.

---

## 🔮 Prediction

A separate prediction script (`predict.py`) was developed to:

* Load the trained model
* Accept user input from the terminal
* Predict medical insurance charges

Run the prediction script:

```bash
python src/predict.py
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Jupyter Notebook

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/hajrawaheed-au/Medical_cost_insurance_prediction.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the prediction script:

```bash
python src/predict.py
```

---

## 📌 Future Improvements

* Apply GridSearchCV and RandomizedSearchCV for automated hyperparameter tuning.
* Build an interactive Streamlit web application.
* Compare additional regression models.
* Perform feature engineering to further improve model performance.

---

## 👤 Author

**Hajra Waheed**
