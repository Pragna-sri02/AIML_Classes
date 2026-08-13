# 🏠 AI Property Valuation — House Price Prediction

A machine learning web application that predicts residential property prices across major Indian cities based on property location, area, bedrooms, resale status, and amenities.

🔗 **Live Demo:** [AI Property Valuation App](https://aimlclasses-swjkbpj3nqmjyffbxzgzwc.streamlit.app/)


## ✨ Features

- 🏠 House price prediction
- 🏙️ City-wise property analysis
- 📊 Property intelligence dashboard
- 💰 Budget-based property exploration
- 🤖 Machine learning model comparison
- 📈 R², MAE and RMSE evaluation
- 🛡️ Amenity-based property prediction
- 🎨 Interactive Streamlit interface

---

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **Machine Learning:** Scikit-learn
- **Data Handling:** Pandas
- **Model Persistence:** Joblib
- **Data Visualization:** Streamlit DataFrames and custom UI components
- **Frontend Styling:** Custom CSS

---

## 📊 Dataset

The project uses the **Housing Dataset in Metropolitan Cities(Combined)** dataset obtained from Kaggle.

---

## 🤖 Machine Learning

The following regression algorithms were compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- KNN Regressor
- Support Vector Regressor (SVR)

The models were evaluated using:

- **R² Score**
- **MAE**
- **RMSE**


### 🏆 Best Model

**Optimized Random Forest Regressor**

The trained model is saved as:

`Best_House_Price_Model.pkl`

The feature columns used by the model are saved as:

`model_columns.pkl`
---

## 📁 Project Structure

```text
├── app.py
├── house_price_prediction.ipynb
├── Indian_House_Price.csv
├── House_Prediction_Cleaned.csv
├── Best_House_Price_Model.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md
```
---
## ⚙️ Installation & Setup
### 1. Clone the repository
```bash
git clone https://github.com/Pragna-sri02/AIML_Classes.git
cd AIML_Classes
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```
---

## 🚀 How to Use
1. Select the city and location.
2. Enter property area and number of bedrooms.
3. Select resale status and available amenities.
4. Click Estimate Property Value.
5. View the predicted property price.
6. Explore the Dashboard and Model Performance sections.

## 👤 Author

**Dodda Pragna Sri**

🔗 **GitHub:** [Pragna-sri02](https://github.com/Pragna-sri02)
