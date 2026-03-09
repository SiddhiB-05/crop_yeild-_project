# 🌾 Crop Yield Prediction System

A **Machine Learning–based web application** that predicts **crop yield** using environmental and agricultural factors such as **region, crop type, rainfall, temperature, pesticide usage, and year**.

The system trains and evaluates multiple regression models and deploys the **Random Forest Regressor** using **Flask** for real-time predictions through a web interface.

---

# 🚀 Live Demo

🔗 **Try the Application:**
https://annabeth08-crop-yield-prediction.hf.space

---

# 📌 Project Overview

Agriculture is highly dependent on environmental and climatic conditions. Predicting crop yield accurately helps **farmers, researchers, and policymakers** make better decisions related to production planning, resource allocation, and food security.

This project:

* Trains multiple regression models on historical crop data
* Evaluates models using standard regression metrics
* Selects the best-performing model for deployment
* Deploys the model using **Flask**
* Provides predictions through a **web interface and REST API**

---

# ⚙️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **Pickle**
* **HTML / CSS**

---

# 📊 Input Features

The model predicts crop yield based on the following features:

| Feature                       | Description                  |
| ----------------------------- | ---------------------------- |
| Area                          | Country or region            |
| Item                          | Crop type                    |
| Year                          | Year of production           |
| average_rain_fall_mm_per_year | Average annual rainfall (mm) |
| pesticides_tonnes             | Pesticide usage (tonnes)     |
| avg_temp                      | Average temperature (°C)     |

---

# 🧠 Machine Learning Models Used

Three regression models were trained and evaluated.

---

## 🌲 Random Forest Regressor (Final Model)

### Training Performance

* **RMSE:** 4,356.9135
* **MAE:** 2,303.5415
* **R² Score:** 0.9973

### Test Performance

* **RMSE:** 12,980.9416
* **MAE:** 6,579.0735
* **R² Score:** 0.9768

✅ **Random Forest Regressor was selected for deployment** because it offers:

* High prediction accuracy
* Strong generalization ability
* Reduced overfitting compared to Decision Tree
* Stable performance across multiple features

---

## 🚀 XGBoost Regressor

### Training Performance

* **RMSE:** 415.9188
* **MAE:** 203.4589
* **R² Score:** 1.0000

### Test Performance

* **RMSE:** 10,301.8674
* **MAE:** 3,697.7668
* **R² Score:** 0.9854

Although **XGBoost achieved the highest test accuracy**, Random Forest was selected because of its **simpler deployment, stability, and interpretability**.

---

# 🏗️ Project Structure

```
crop-yield-prediction
│
├── models/
│   ├── rf_regressor.pkl
│   └── preprocessor.pkl
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── application.py
├── requirements.txt
└── README.md
```

---

# 🔌 Flask API Endpoints

## 🏠 Home Page

```
GET /
```

Renders the main web interface for the application.

---

## 🔮 Predict Crop Yield

```
POST /predict_data
```

### Request Body (JSON)

```json
{
  "area": "India",
  "item": "Wheat",
  "year": 2013,
  "rainfall": 1100,
  "pesticides": 55,
  "avg_temp": 24.5
}
```

### Response (JSON)

```json
{
  "prediction": 31245,
  "crop": "Wheat",
  "region": "India"
}
```

---

# ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/crop-yield-prediction.git
```

### 2️⃣ Navigate to Project Folder

```
cd crop-yield-prediction
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application

```
python application.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

# 📈 Conclusion

This system successfully predicts **crop yield using machine learning techniques**.

The **Random Forest Regressor** provides a strong balance between **accuracy, robustness, and stability**. By integrating the model with **Flask**, the system allows real-time predictions through a simple web interface.

This project demonstrates how **machine learning can assist agricultural decision-making and improve productivity forecasting**.

---

# 🌱 Future Improvements

* Add **data visualization dashboards**
* Deploy using **Docker or cloud platforms**
* Integrate **real-time weather APIs**
* Improve **model explainability using SHAP**
* Support **more crops and regions**

---

If you found this project useful, feel free to ⭐ the repository.
