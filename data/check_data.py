import pandas as pd

FILE_PATH = "djia_stock_price.csv"


def main():
    print(" Loading data...")
    df = pd.read_csv(FILE_PATH)

    print("\n BASIC INFO")
    print(df.info())

    print("\n COLUMNS")
    print(df.columns.tolist())

    # Missing values
    # -------------------------
    print("\n MISSING VALUES")
    missing = df.isna().sum()
    print(missing[missing > 0] if missing.sum() > 0 else " No missing values")

    # Duplicate primary key
    # -------------------------
    print("\n🔑 DUPLICATE (ticker, date)")
    dup = df.duplicated(subset=["ticker", "date"]).sum()
    print(f" Duplicates found: {dup}" if dup > 0 else " No duplicates")

    # Price logic checks
    # -------------------------
    print("\n PRICE VALIDATION")

    invalid_price = df[
        (df["High"] < df["Low"]) |
        (df["Close"] > df["High"]) |
        (df["Close"] < df["Low"]) |
        (df["Open"] > df["High"]) |
        (df["Open"] < df["Low"])
    ]

    print(f" Invalid price rows: {len(invalid_price)}" if not invalid_price.empty else " Price logic OK")

    # Volume check
    # -------------------------
    print("\n VOLUME CHECK")
    invalid_volume = df[df["Volume"] <= 0]
    print(f" Invalid volume rows: {len(invalid_volume)}" if not invalid_volume.empty else " Volume OK")

    # Date range
    # -------------------------
    df["date"] = pd.to_datetime(df["date"])
    print("\n DATE RANGE")
    print(f"From {df['date'].min().date()} to {df['date'].max().date()}")

    # Summary
    # -------------------------
    print("\n DATASET SUMMARY")
    print(f"Rows: {len(df):,}")
    print(f"Tickers: {df['ticker'].nunique()}")
    print(f"Avg rows per ticker: {len(df) // df['ticker'].nunique():,}")

    print("\n DATA CHECK COMPLETED")


if __name__ == "__main__":
    main()
