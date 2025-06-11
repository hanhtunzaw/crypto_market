
# 📊 Crypto Market BI Project

Welcome to my Business Intelligence project focused on the cryptocurrency market. This project walks through a complete ETL pipeline—from collecting real-time crypto data to analyzing and visualizing it—all using Python, CoinGecko API, and Power BI.

## 🧠 What This Project Is About

In today's data-driven world, being able to turn real-time market data into actionable insights is a powerful skill. This project was built as part of my master's course in Business Intelligence and demonstrates how to create a fully automated, production-ready pipeline for crypto analytics.

It starts with retrieving up-to-date data from the CoinGecko API, then processes and stores that data, and finally presents it in a one-page Power BI dashboard designed for quick, interactive insights.

## ⚙️ Key Features

- 🔁 **ETL Automation**: Fully automated data pipeline (Extract, Transform, Load)
- 📡 **API Integration**: Collects real-time prices of 20+ popular cryptocurrencies
- 🧹 **Data Cleaning**: Preprocessing with pandas to ensure consistency and reliability
- 💾 **Storage**: Cleaned data is saved into a local SQLite database
- 📊 **Power BI Dashboard**: One-page interactive report with KPIs, slicers, trend lines, and 24h % changes
- 📧 **Email Alerts**: Get notified when the pipeline runs successfully—or fails
- 🧰 **Task Scheduler**: Runs on a set schedule (Windows Task Scheduler)
- 🐳 **Docker-Ready**: Project includes a Dockerfile (optional)
- 🤖 **ML Integration (Optional)**: Framework ready for adding machine learning prediction
- 🔐 **Secure Config**: Uses `.env` for environment variables

## 📁 Project Structure

```
crypto_bi_project/
├── data/
│   ├── raw/                  # Raw data from API
│   └── processed/            # Cleaned and transformed data
├── database/
│   └── coingecko.db          # SQLite database file
├── scripts/
│   ├── extract.py            # Pulls data from CoinGecko API
│   ├── transform.py          # Cleans and formats the data
│   ├── load.py               # Loads data into SQLite
├── pipeline_scheduler.py     # Runs the full pipeline with logging and alerts
├── send_email.py             # Handles sending status emails
├── .env                      # Stores API endpoint and currency list
├── etl.log                   # Log file with ETL status and errors
├── Dockerfile                # (Optional) Docker container setup
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── dashboard/
    └── crypto_dashboard.pbix # Power BI dashboard (interactive report)
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
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up `.env` File

Create a `.env` file in the project root and include:

```
COINGECKO_API=https://api.coingecko.com/api/v3/coins/markets
CURRENCIES=bitcoin,ethereum,tether,binancecoin,solana,usd-coin,xrp,dogecoin,cardano,toncoin,avalanche,polkadot,tron,chainlink,polygon,litecoin,uniswap,internet-computer,filecoin,stellar
CURRENCY_UNIT=usd
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_TO=recipient_email@gmail.com
```

### 5. Run the ETL Pipeline Manually

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

### 6. Or Run the Full Pipeline with Logging and Email Alerts

```bash
python pipeline_scheduler.py
```

### 7. Automate with Task Scheduler (Windows)

- Open Task Scheduler
- Create a basic task
- Point it to run `python pipeline_scheduler.py` using full path to Python

## 📊 Dashboard Overview

The Power BI report provides a quick and clear look into the crypto market. It includes:

- 🔎 **Coin Slicer**: View data for any specific coin
- 🧮 **KPIs**: Current price, 24h % change, market cap, volume
- 📈 **Trend Lines**: Visualize 24h % change over time
- ⏱️ **Latest Data Only**: Measures are filtered to always reflect the most recent timestamp

## 📬 Email Alerts

If something goes wrong (or right!), the pipeline sends an email using Gmail SMTP. You just need to:

- Add your credentials and app password to `.env`
- Use the logging and alert system in `pipeline_scheduler.py`

## 🐳 Optional: Run in Docker

```bash
docker build -t crypto-etl .
docker run crypto-etl
```

## 📈 Bonus: Add ML Later

Structure is ready to plug in regression models to predict price trends. Just create a new `ml.py` and plug into the pipeline.

## 🧠 What I Learned

This project sharpened my skills in:

- Real-world ETL pipeline design
- API integration and automation
- Data cleaning and modeling
- Power BI dashboarding
- Workflow orchestration
- Email automation
- Version control with Git & GitHub
- Secure credential handling with `.env`

## 📫 Let’s Connect

If you're interested in similar projects or want to collaborate, feel free to connect with me on [LinkedIn](https://www.linkedin.com) or check out my other repositories!

---

Feel free to star ⭐ this repo if you found it helpful!
