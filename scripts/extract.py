import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd

load_dotenv()

url = os.getenv("COINGECKO_API")
currencies = os.getenv("CURRENCIES")
vs_currency = os.getenv("CURRENCY_UNIT")

def fetch_crypto_data():
    params = {
        "vs_currency": vs_currency,
        "ids": currencies,
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.json_normalize(data)
    df["fetched_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df

if __name__ == "__main__":
    df = fetch_crypto_data()

    filepath = "data/raw/crypto_raw.csv"
    
    if os.path.exists(filepath):
        existing_df = pd.read_csv(filepath)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_csv(filepath, index=False)