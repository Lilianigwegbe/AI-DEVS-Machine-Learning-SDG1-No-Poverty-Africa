# 🌍 Africa Poverty Forecasting App  

## 📌 SDG 1: No Poverty  

---

## 📖 About This Project  
  

This is AI software engineering project was created as part of our Sustainable Development Goals (SDG) machine learning assignment. We chose **SDG 1: No Poverty**, focusing on forecasting poverty trends in African countries.  

By using a machine learning model, we aim to predict how poverty rates might change over time — helping governments, communities, and organizations plan better for the future. 🌱  

---

## 🎯 Problem We Are Solving  

Poverty remains one of Africa’s biggest challenges. Knowing how poverty levels might change in the coming years can help decision-makers take action sooner.

Our app makes this easier by:
- Forecasting poverty rates for African countries  
- Showing both past and future trends in simple, clear charts  
- Helping users explore data in a clean, interactive way  

---

## 🧠 Machine Learning Approach  

### 📌 What Technique Did We Use?  

We used a **Supervised Learning** method called **XGBoost Regression**.  

**What is XGBoost?**  
It’s a popular, beginner-friendly machine learning algorithm known for being fast and accurate. It works by combining simple prediction models (called decision trees) into a more powerful one.

**How it works in our project:**
- We trained the model using poverty data from past years
- Created lagged features (like previous years’ poverty rates) to help the model learn trends over time  
- Used the model to predict future poverty rates for up to 15 years ahead  

---

## 📊 Dataset  

We used a cleaned dataset called **`africa_poverty_cleaned.csv`**, which includes:
- Country names  
- Years  
- Poverty rates (as a percentage)  

The data was sourced from publicly available SDG databases and cleaned for analysis.

---

## 🛠️ Tools and Libraries  

This project was built using:
- **Python 3.10**
- **Streamlit** (for creating the interactive web app)
- **Pandas** (for data manipulation)
- **XGBoost** (for regression modeling)
- **Matplotlib** (for charts and plots)
- **Scikit-learn** (for preprocessing and utilities)

---

## 📝 How Our Project Works (Workflow)

1. 📥 Load and clean the poverty dataset  
2. 🔍 Prepare lagged features so the model can learn trends  
3. ⚙️ Train an **XGBoost Regression model** on the data  
4. 💾 Save the trained model as a `.pkl` file  
5. 🖥️ Build a **Streamlit web app** for user interaction  
6. 📊 Plot both historical and predicted poverty rates in an easy-to-read chart  

---

## ⚖️ Ethical Reflection  

**Possible Data Bias:**  
Some countries might have missing or unreliable data, which could affect how well the model forecasts poverty rates for them.

**Fairness and Impact:**  
Our goal is to make poverty forecasting accessible and transparent. By sharing both predictions and data openly, we encourage informed decision-making and promote fair development planning for African communities.

---

## 📽️ Demo  

✅ You can try out the live app here:  
👉 **[https://evans200png-poverty-app-ns51he.streamlit.app/](https://evans200png-poverty-app-ns51he.streamlit.app/)**  

---

## 👨‍💻 How to Run This Project Locally  

### ✅ What You Need:
- **Python 3.10+ installed on your computer**
- Internet connection to install required libraries  

---

### 📦 1. Download the project files  

Either clone the repo:
```bash
git clone https://github.com/Lilianigwegbe/AI-DEVS-SDG1-Africa-Poverty-Forecast-ml.git
cd model-app
