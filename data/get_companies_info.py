import yfinance as yf
import pandas as pd
import time

DJIA_TICKERS = [
    "AAPL", "AMGN", "AMZN", "AXP", "BA", "CAT", "CRM", "CSCO", "CVX", "DIS",
    "GS", "HD", "HON", "IBM", "JNJ", "JPM", "KO", "MCD", "MMM",
    "MRK", "MSFT", "NKE", "NVDA", "PG", "SHW", "TRV", "UNH", "V", "VZ", "WMT"
]

OUTPUT_FILE = "./djia_company_info.csv"


def fetch_company_info(ticker: str) -> dict:
    print(f"Fetching info for {ticker}...")
    t = yf.Ticker(ticker)
    info = t.info

    return {
        "symbol": info.get("symbol", ticker),
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "country": info.get("country"),
        "website": info.get("website"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "dividend_yield": info.get("dividendYield"),
        "52_week_high": info.get("fiftyTwoWeekHigh"),
        "52_week_low": info.get("fiftyTwoWeekLow"),
        "description": info.get("longBusinessSummary"),
    }


def main():
    records = []

    for ticker in DJIA_TICKERS:
        try:
            record = fetch_company_info(ticker)
            records.append(record)
            time.sleep(1.5)  # tránh bị rate-limit
        except Exception as e:
            print(f"Failed for {ticker}: {e}")

    df = pd.DataFrame(records)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\n DONE")
    print(f"Companies: {len(df)}")
    print(f"Saved to: {OUTPUT_FILE}")
    print(df.head(3))


if __name__ == "__main__":
    main()
