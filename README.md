# 🏠 AI Property Valuation — House Price Prediction

A machine learning web app that estimates Indian house prices based on location, size, building details, and amenities — powered by a **Random Forest Regressor** and served through an interactive **Streamlit** interface.

🔗 **Live Demo:** [AI Property Valuation App](https://aimlclasses-knazmhtvd3ehehgojxdzkw.streamlit.app/)

---

## ✨ Features

- **Price Prediction** — Enter property details such as city, locality, BHK, area, floors, amenities, and more to get an instant AI-estimated price.
- **Dashboard** — View dataset overview, number of properties, number of cities, Best Value Cities, Budget Explorer, and other property insights.
- **Model Performance** — Compare multiple ML algorithms using MAE, RMSE, and R² metrics.
- **Responsive UI** — Clean and colorful interface built with custom CSS on top of Streamlit.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **ML Library:** Scikit-learn
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Model Persistence:** Joblib

---

## 📊 Dataset

- **Source:** `Indian_House_Price.csv` — Indian residential property listings.
- **Cleaned file used by the app:** `House_Prediction_Cleaned.csv`
- **Key columns:** City, Locality, BHK, Area (sqft), Bathrooms, Parking Spaces, Balcony, Floor Number, Total Floors, Property Age, Property Type, Furnishing, Metro Distance, Distance to City Center, Nearby Schools/Hospitals, Amenities Score, Price (INR)
- **Preprocessing:** Missing value imputation, duplicate removal, outlier removal using the IQR method on Area, and one-hot encoding for categorical features.
- **Engineered features:** `Bath_BHK_Ratio`, `Total_Facilities`, `Location_Score`

---

## 🤖 Model Details

Multiple regression algorithms were trained and compared:

| Algorithm | MAE (₹) | RMSE (₹) | R² Score |
|---|---:|---:|---:|
| Linear Regression | 10,53,715 | 15,20,602 | 0.945 |
| Decision Tree | 11,39,923 | 14,44,390 | 0.951 |
| **Random Forest** | **8,11,828** | **10,12,107** | **0.976** |
| KNN | 40,09,238 | 56,50,064 | 0.243 |
| SVR | 47,08,039 | 65,86,032 | -0.029 |

### 🏆 Best Model

**Random Forest Regressor**

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
1. Fill in the property details such as city, locality, size, building details, features, accessibility, and amenities.
2. Click **Estimate Property Value**.
3. Review the estimated price and property profile.
4. Check the **Dashboard** tab for property and city-wise insights.
5. Check the **Model Performance** tab to compare the regression models.

## 👤 Author

**Dodda Pragna Sri**

🔗 **GitHub:** [Pragna-sri02](https://github.com/Pragna-sri02)
