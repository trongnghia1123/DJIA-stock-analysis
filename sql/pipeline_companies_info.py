import pandas as pd
from sqlalchemy import create_engine, text

# ================= CONFIG =================
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "djia_db"

TABLE_NAME = "dim_company"
CSV_FILE = "./data/djia_company_info.csv"
# =========================================


def main():
    # Kết nối DB
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    df = pd.read_csv(CSV_FILE)
    df = df.rename(
        columns={
            "52_week_high": "high_52_week",
            "52_week_low": "low_52_week",
        }
    )

    df = df.dropna(subset=["symbol"])

    # Ghi dữ liệu
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

    with engine.begin() as conn:
        # PRIMARY KEY
        conn.execute(text(f"""
            ALTER TABLE {TABLE_NAME}
            ADD CONSTRAINT pk_dim_company
            PRIMARY KEY (symbol);
        """))

    print("dim_company loaded successfully")
    print("PRIMARY KEY: symbol")


if __name__ == "__main__":
    main()
