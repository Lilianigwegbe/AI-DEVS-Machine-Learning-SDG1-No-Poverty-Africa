# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("africa_poverty_cleaned.csv")

# Encode country names
df['Country Code Encoded'] = LabelEncoder().fit_transform(df['Country Name'])
df = df.sort_values(by=['Country Name', 'Year'])
df['Poverty Rate Lag1'] = df.groupby('Country Name')['Poverty Rate'].shift(1)
df.dropna(inplace=True)

# Train model
X = df[['Year', 'Poverty Rate Lag1', 'Country Code Encoded']]
y = df['Poverty Rate']
model = XGBRegressor(n_estimators=50, max_depth=4, subsample=0.8, colsample_bytree=0.8)
model.fit(X, y)

# Forecasting function
def forecast_poverty(country_name, years_to_forecast):
    country_data = df[df['Country Name'] == country_name].sort_values(by='Year')
    last_year = country_data['Year'].max()
    last_poverty_rate = country_data[country_data['Year'] == last_year]['Poverty Rate'].values[0]
    country_code = country_data['Country Code Encoded'].values[0]

    forecast_years = []
    forecast_rates = []

    for i in range(1, years_to_forecast + 1):
        future_year = last_year + i
        X_future = pd.DataFrame({
            'Year': [future_year],
            'Poverty Rate Lag1': [last_poverty_rate],
            'Country Code Encoded': [country_code]
        })
        pred = model.predict(X_future)[0]
        forecast_years.append(future_year)
        forecast_rates.append(pred)
        last_poverty_rate = pred

    return forecast_years, forecast_rates

# Streamlit app UI
st.title("🌍 Africa Poverty Rate Forecasting (SDG 1)")
st.markdown("This app uses XGBoost to forecast future poverty rates based on historical data.")

# Sidebar inputs
country = st.selectbox("Select Country", sorted(df['Country Name'].unique()))
n_years = st.slider("Years to Forecast", 1, 15, 5)

# Run forecast
forecast_years, forecast_rates = forecast_poverty(country, n_years)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
hist = df[df['Country Name'] == country].sort_values(by='Year')
ax.plot(hist['Year'], hist['Poverty Rate'], label='Historical', marker='o')
ax.plot(forecast_years, forecast_rates, label='Forecast', linestyle='--', marker='x', color='orange')
ax.set_title(f"Poverty Rate Forecast for {country}")
ax.set_xlabel("Year")
ax.set_ylabel("Poverty Rate")
ax.legend()
ax.grid(True)
st.pyplot(fig)
