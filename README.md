# 🌾 Crop Yield Prediction System

A Machine Learning–based web application that predicts **crop yield** using environmental and agricultural factors such as region, crop type, rainfall, temperature, pesticide usage, and year.  
The system compares multiple regression models and deploys the **Random Forest Regressor** using **Flask** for real-time predictions.

---

## 📌 Project Overview

Agriculture is highly dependent on climate and environmental conditions. Accurate crop yield prediction can help farmers, researchers, and policymakers make informed decisions.

This project:
- Trains multiple regression models on historical crop data
- Compares their performance using standard regression metrics
- Deploys the best-performing model using Flask
- Provides predictions through a web interface and REST API

---

## ⚙️ Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NumPy  
- Pickle  
- HTML / CSS  

---

## 📊 Input Features

The model predicts crop yield based on the following features:

| Feature | Description |
|-------|------------|
| Area | Country or region |
| Item | Crop type |
| Year | Year of production |
| average_rain_fall_mm_per_year | Average annual rainfall (mm) |
| pesticides_tonnes | Pesticide usage (tonnes) |
| avg_temp | Average temperature (°C) |

---

## 🧠 Machine Learning Models Used

Three regression models were trained and evaluated:

---

### 🌳 Decision Tree Regressor

**Training Set Performance**
- Root Mean Squared Error (RMSE): **32,344.3632**
- Mean Absolute Error (MAE): **13,635.1413**
- R² Score: **0.8536**

**Test Set Performance**
- Root Mean Squared Error (RMSE): **39,329.3611**
- Mean Absolute Error (MAE): **18,050.2551**
- R² Score: **0.7866**

This model provides a strong baseline but tends to overfit and shows reduced generalization on unseen data.

---

### 🌲 Random Forest Regressor (Final Model)

**Training Set Performance**
- Root Mean Squared Error (RMSE): **4,356.9135**
- Mean Absolute Error (MAE): **2,303.5415**
- R² Score: **0.9973**

**Test Set Performance**
- Root Mean Squared Error (RMSE): **12,980.9416**
- Mean Absolute Error (MAE): **6,579.0735**
- R² Score: **0.9768**

✅ **Random Forest Regressor was selected for deployment** due to:
- High prediction accuracy
- Strong generalization on test data
- Reduced overfitting compared to Decision Tree
- Robust performance across multiple features

---

### 🚀 XGBoost Regressor

**Training Set Performance**
- Root Mean Squared Error (RMSE): **415.9188**
- Mean Absolute Error (MAE): **203.4589**
- R² Score: **1.0000**

**Test Set Performance**
- Root Mean Squared Error (RMSE): **10,301.8674**
- Mean Absolute Error (MAE): **3,697.7668**
- R² Score: **0.9854**

Although XGBoost achieved the highest test accuracy, Random Forest was chosen for deployment due to its interpretability, stability, and simpler production setup.

---

## 🏗️ Project Structure

├── models/
│ ├── rf_regressor.pkl
│ └── preprocessor.pkl
├── templates/
│ ├── index.html
│ └── home.html
├── application.py
├── requirements.txt
└── README.md


---

## 🔌 Flask API Endpoints

### 🏠 Home Page
GET /

Renders the main user interface.

---

### 🔮 Predict Crop Yield
POST /predict_data


**Request Body (JSON):**
```json
{
  "area": "India",
  "item": "Wheat",
  "year": 2013,
  "rainfall": 1100,
  "pesticides": 55,
  "avg_temp": 24.5
}
Response (JSON):

{
  "prediction": 31245,
  "crop": "Wheat",
  "region": "India"
}
▶️ How to Run the Project
Clone the repository

git clone https://github.com/yourusername/crop-yield-prediction.git
Install dependencies

pip install -r requirements.txt
Run the Flask application

python app.py
Open your browser and visit:

http://127.0.0.1:5000/
📈 Conclusion
The system successfully predicts crop yield using machine learning

Random Forest Regressor offers an optimal balance between accuracy and robustness

Flask enables easy deployment and real-time prediction

The project can be extended for large-scale agricultural decision support systems

🌱 Future Improvements
Add data visualization dashboards

Deploy using Docker or cloud platforms

Include real-time weather data APIs

Improve model explainability using SHAP or feature importance