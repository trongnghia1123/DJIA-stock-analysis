import pandas as pd
from sqlalchemy import create_engine, text

# ================= CONFIG =================
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "djia_db"

TABLE_NAME = "fact_stock_price"
CSV_FILE = "./data/djia_stock_price.csv"
# =========================================


def main():
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Load CSV
    df = pd.read_csv(CSV_FILE)

    df["date"] = pd.to_datetime(df["Date"]).dt.date
    df = df.rename(columns={"Ticker": "ticker"})
    df = df.drop(columns=["Date"])

    # Load data
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

    with engine.begin() as conn:
        # FOREIGN KEY
        conn.execute(text(f"""
            ALTER TABLE {TABLE_NAME}
            ADD CONSTRAINT fk_stock_company
            FOREIGN KEY (ticker)
            REFERENCES dim_company(symbol);
        """))

        # INDEX cho performance
        conn.execute(text(f"""
            CREATE INDEX idx_stock_ticker
            ON {TABLE_NAME}(ticker);
        """))

        conn.execute(text(f"""
            CREATE INDEX idx_stock_date
            ON {TABLE_NAME}(date);
        """))

    print("fact_stock_price loaded successfully")
    print("FOREIGN KEY: ticker → dim_company(symbol)")
    print("Indexes created on ticker & date")


if __name__ == "__main__":
    main()
