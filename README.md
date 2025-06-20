# 🧪 A/B Test Results Analyzer

A Streamlit web app to analyze A/B test results.  
It calculates conversion rates, performs a z-test for statistical significance, and provides insights through clean visuals.

## 🚀 Features

- 📤 Upload CSV files with `group` and `converted` columns
- 📊 View conversion rates and visual comparisons
- ✅ Automatically detects statistical significance (z-test, p-value)
- 📈 Interactive charts using Seaborn & Matplotlib
- 🔒 Built with Python, Pandas, Streamlit, and statsmodels

## 📁 Sample CSV Format

```
user_id,group,converted
1,A,0
2,B,1
3,A,1
4,B,1
...
```

## 📸 Screenshots

![App UI](screenshots/ui.png)

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Live Demo

[Click here to view deployed app](#) <!--(http://localhost:8501)-->

## 🧠 Learnings

- Designed for product, UX, and marketing teams to validate experiments
- Demonstrated ability to communicate analytical results through visual and statistical insights
