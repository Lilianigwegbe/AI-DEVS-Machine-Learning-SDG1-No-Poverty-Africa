## 🌍 Africa Poverty Forecasting App

This **Streamlit** web app forecasts **poverty trends in African countries** using the **SDG 1 dataset** and an **XGBoost machine learning model**.

---

### 🔮 Features

- 📌 Select an African country from a dropdown
- ⏳ Forecast future poverty rates for **up to 15 years**
- 📊 View both **historical and predicted** poverty trends in a clean chart
- 💡 Powered by **XGBoost regression** with lagged features for improved forecasting

---

### 🚀 Live Demo

✅ Use the app here:  
👉 **[https://evans200png-poverty-app-ns51he.streamlit.app/](https://evans200png-poverty-app-ns51he.streamlit.app/)**

---

### 🧑‍💻 How to Run the App Locally

#### 📁 1. Clone this repository

```bash
git clone [https://github.com/Lilianigwegbe/AI-DEVS-SDG1-Africa-Poverty-Forecast-ml.git]
cd model-app
```

---
#### 📦 2. Install the required dependencies

```bash
pip install -r requirements.txt
```

---

#### ▶️ 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

### 📂 Project Structure

```bash
africa-poverty-forecast/
├── app.py                      # Main Streamlit application
├── africa_poverty_cleaned.csv # Cleaned dataset
├── model.pkl                   # Trained XGBoost model
├── requirements.txt            # List of Python dependencies
└── README.md                   # Project documentation
```

---

### 📚 Technologies Used

_____
Python 3.10
____
Streamlit – web app framework
____
Pandas – data manipulation
____
XGBoost – machine learning model
____
Matplotlib – data visualization
____
Scikit-learn – preprocessing and model utilities



