
# 📊 Crypto Market BI Project

Welcome to my Business Intelligence project focused on the cryptocurrency market. This project walks through a complete ETL pipeline—from collecting real-time crypto data to analyzing and visualizing it—all using Python, CoinGecko API, Power BI, and a Machine Learning model deployed with Streamlit.

## 🧠 What This Project Is About

In today's data-driven world, being able to turn real-time market data into actionable insights is a powerful skill. This project was built as part of my master's course in Business Intelligence and demonstrates how to create a fully automated, production-ready pipeline for crypto analytics.

It starts with retrieving up-to-date data from the CoinGecko API, then processes and stores that data, and finally presents it in both a one-page Power BI dashboard and an ML-powered Streamlit web app.

## ⚙️ Key Features

- 🔁 **ETL Automation**: Fully automated data pipeline (Extract, Transform, Load)
- 📡 **API Integration**: Collects real-time prices of 20+ popular cryptocurrencies
- 🧹 **Data Cleaning**: Preprocessing with pandas to ensure consistency and reliability
- 💾 **Storage**: Cleaned data is saved into a local SQLite database
- 📊 **Power BI Dashboard**: Interactive report with KPIs, slicers, trend lines, and 24h % changes
- 📧 **Email Alerts**: Get notified when the pipeline runs successfully—or fails
- 🧰 **Task Scheduler**: Runs on a set schedule (Windows Task Scheduler)
- 🐳 **Docker-Ready**: Project includes a Dockerfile (optional)
- 🤖 **ML Integration**: Predicts crypto price using RandomForest for top 5 coins
- 🖥️ **Streamlit App**: Interactive web app for price prediction
- 🔐 **Secure Config**: Uses `.env` for environment variables

## 📁 Project Structure

```
crypto_bi_project/
├── app.py                  # Streamlit app for ML predictions
├── crypto_price_model.pkl  # Trained ML model
├── ml/
│   └── train_model.py      # ML training pipeline
├── data/
│   ├── raw/
│   └── processed/
├── database/
│   └── coingecko.db
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── pipeline_scheduler.py
├── send_email.py
├── .env
├── etl.log
├── Dockerfile
├── requirements.txt
├── README.md
└── dashboard/
    └── crypto_dashboard.pbix
```

## 🔧 How to Set Up and Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crypto_market.git
cd crypto_market
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` File

Create a `.env` file in the project root with:
```
COINGECKO_API=https://api.coingecko.com/api/v3/coins/markets
CURRENCIES=bitcoin,ethereum,tether,binancecoin,solana,usd-coin,xrp,dogecoin,cardano,toncoin,avalanche,polkadot,tron,chainlink,polygon,litecoin,uniswap,internet-computer,filecoin,stellar
CURRENCY_UNIT=usd
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_TO=recipient_email@gmail.com
```

### 5. Run the ETL Pipeline

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

Or full pipeline:
```bash
python pipeline_scheduler.py
```

### 6. Run Streamlit App

```bash
streamlit run app.py
```

## 📊 Dashboard Overview

- Coin Slicer: View data for specific coin
- KPIs: Current price, 24h % change, market cap, volume
- Trend Lines: Visualize market trends over time
- Latest Snapshot: Always shows data from most recent timestamp

## 🤖 ML App (via Streamlit)

The Streamlit app lets users predict the price of the top 5 coins using:

- Market cap
- Trading volume
- 24h % change
- Coin symbol (auto-filtered)

Model used: `RandomForestRegressor` trained on cleaned dataset.

## 📬 Email Alerts

Get notified when the ETL pipeline succeeds or fails.

## 🧠 What I Learned

- Real-world ETL pipeline design
- API integration & automation
- Data cleaning and transformation
- Power BI dashboarding
- Machine learning model deployment
- Streamlit app design
- Version control with Git & GitHub

## 📫 Let’s Connect

If you're interested in similar projects or want to collaborate, feel free to connect with me on LinkedIn or check out my other repositories!

⭐ If you found this helpful, give it a star on GitHub!
