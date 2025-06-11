import pandas as pd

def clean_crypto_data(filepath="data/raw/crypto_raw.csv"):
    df = pd.read_csv(filepath)
    df = df[
        ['id', 'symbol', 'name', 'current_price', 'market_cap', 
         'total_volume', 'price_change_percentage_24h', 'fetched_at']
    ]
    df.columns = ['id', 'symbol', 'name', 'price', 'market_cap', 
                  'volume', 'pct_change_24h', 'timestamp']

    # ✅ Sort by timestamp and market cap (most recent data comes last)
    df.sort_values(by=["timestamp", "market_cap"], ascending=[True, False], inplace=True)

    df.to_csv("data/processed/crypto_cleaned.csv", index=False)
    return df

if __name__ == "__main__":
    clean_crypto_data()