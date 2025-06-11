import pandas as pd
import sqlite3

def load_to_sqlite():
    df = pd.read_csv("data/processed/crypto_cleaned.csv")

    # Optional: remove duplicates if re-running ETL multiple times per day
    df.drop_duplicates(subset=["id", "timestamp"], keep="last", inplace=True)

    conn = sqlite3.connect("database/coingecko.db")
    df.to_sql("crypto_prices", conn, if_exists="append", index=False)
    conn.close()

    print(f"{len(df)} records loaded into SQLite.")

if __name__ == "__main__":
    load_to_sqlite()
