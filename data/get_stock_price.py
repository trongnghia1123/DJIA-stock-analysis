import yfinance as yf
import pandas as pd
from datetime import date

DJIA_TICKERS = [
    "AAPL", "AMGN", "AMZN", "AXP", "BA", "CAT", "CRM", "CSCO", "CVX", "DIS",
    "GS", "HD", "HON", "IBM", "JNJ", "JPM", "KO", "MCD", "MMM",
    "MRK", "MSFT", "NKE", "NVDA", "PG", "SHW", "TRV", "UNH", "V", "VZ", "WMT"
]

START_DATE = "2023-01-01"
END_DATE = date.today().strftime("%Y-%m-%d")
OUTPUT_FILE = "./djia_stock_price.csv"


def fetch_one_ticker(ticker: str) -> pd.DataFrame:
    print(f"Downloading {ticker}...")

    
    df = yf.download(
        ticker,
        start=START_DATE,
        end=END_DATE,
        progress=False,
        auto_adjust=False,
        group_by="column"   
    )

    if df.empty:
        return pd.DataFrame()


    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    
    if "Dividends" not in df.columns:
        df["Dividends"] = 0.0
    if "Stock Splits" not in df.columns:
        df["Stock Splits"] = 0.0

    df["Ticker"] = ticker
    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    
    df = df[
        [
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Ticker",
        ]
    ]

    return df


def main():
    all_data = []

    for ticker in DJIA_TICKERS:
        df = fetch_one_ticker(ticker)
        if not df.empty:
            all_data.append(df)

    if not all_data:
        print("No data downloaded")
        return

    final_df = pd.concat(all_data, ignore_index=True)
    final_df = final_df.sort_values(["Ticker", "Date"])

    
    assert list(final_df.columns) == [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Ticker",
    ]

    final_df.to_csv(OUTPUT_FILE, index=False)

    print("\n DONE")
    print(f"Rows: {len(final_df):,}")
    print(f"Columns: {list(final_df.columns)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
