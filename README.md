# 🌲 Algerian Forest Fire Detection – End-to-End Machine Learning Project

## 📌 Project Overview
This project is an **end-to-end machine learning pipeline** for predicting the **Fire Weather Index (FWI)** using the **Algerian Forest Fire Dataset**.  
It covers **data cleaning, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment preparation**.

The final model selected is **RidgeCV Regression**, achieving an **accuracy of ~98%**.

---

## 📊 Dataset
- **Source**: [Algerian Forest Fire Dataset – UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset)
- **Features**:
  - **Spatial**: Region, Month, Day
  - **Meteorological**: Temperature, Relative Humidity, Wind Speed, Rain
  - **FWI Components**: FFMC, DMC, DC, ISI
- **Target Variable**: FWI (Fire Weather Index)

---

## 🛠 Workflow
1. **Data Cleaning & Preprocessing**
   - Handled missing values
   - Standardized column names
   - Converted data types
   - Encoded categorical variables

2. **Exploratory Data Analysis (EDA)**
   - Distribution plots
   - Correlation heatmaps
   - Outlier detection

3. **Feature Engineering**
   - Scaling numerical features
   - Removing redundant features

4. **Model Training & Evaluation**
   - **Linear Regression**
   - **LassoCV**
   - **ElasticNetCV**
   - **RidgeCV** ✅ *(Selected – Best Performance)*

5. **Model Selection**
   - RidgeCV chosen due to **highest R² score (~0.98)** and stability.

6. **Deployment Preparation**
   - Created Flask app (`application.py`)
   - Saved trained model in `Model/ridge_model.pkl`
   - Added `requirements.txt` for reproducibility

---

## 📈 Model Performance
| Model           | R² Score |
|----------------|---------|
| Linear Regression | ~97% |
| LassoCV          | ~95% |
| ElasticNetCV     | ~94% |
| **RidgeCV**      | **~98%** ✅ |

---

## 🚀 How to Run Locally
### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Algerian_Forest_Fire_Detection.git
cd Algerian_Forest_Fire_Detection
