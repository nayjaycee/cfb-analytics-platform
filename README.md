# 🏈 College Football Analytics Platform

A data science + ML project using the [CollegeFootballData API](https://collegefootballdata.com/), covering seasons 2000–present.
Includes automated data pulls, feature engineering (Elo, records, streaks), predictive models, and an interactive dashboard.

## Tech
Python, pandas, scikit-learn, XGBoost, Streamlit, CFBD API.

## Structure

```
cfb-analytics-platform/
├── data/ # local storage (ignored by git)
│ ├── raw/ # raw API data
│ └── processed/ # cleaned & merged datasets
│
├── notebooks/ # EDA and experiments
│ ├── 01_data_collection.ipynb
│ ├── 02_feature_engineering.ipynb
│ └── 03_modeling.ipynb
│
├── src/ # reusable modules (API, records, features, modeling)
│ ├── cfbd_client.py
│ ├── data_cleaning.py
│ ├── feature_engineering.py
│ └── modeling.py
│
├── dashboard/ # Streamlit app
│ └── app.py
│
├── requirements.txt
└── README.md
```
## 🎯 Goals
1. Explore long-term trends in college football
2. Build predictive models for game outcomes
3. Deploy an interactive analytics platform

---

*Developed by [Joshua Cushing](https://www.linkedin.com/in/joshuacushing/)*

