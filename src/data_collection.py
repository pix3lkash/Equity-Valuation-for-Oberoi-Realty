"""
=========================================================
DATA COLLECTION MODULE
Author: Your Name
Project: Oberoi Realty Stock Valuation
=========================================================
Downloads

✓ Historical Prices
✓ Company Information
✓ Company Metrics
✓ Annual Financial Statements
✓ Quarterly Financial Statements
✓ Balance Sheet
✓ Cash Flow
✓ Dividend History
✓ Stock Split History

Everything is saved into /data/raw
=========================================================
"""

import yfinance as yf
import pandas as pd
from config import *

# ---------------------------------------------------
# Helper Function
# ---------------------------------------------------

def save_csv(df, filename):

    try:
        path = RAW_DATA / filename
        df.to_csv(path)
        print(f"✓ Saved {filename}")

    except Exception as e:
        print(f"Could not save {filename}")
        print(e)


# ---------------------------------------------------
# Main Function
# ---------------------------------------------------

def collect_data():

    print("\nDownloading data from Yahoo Finance...\n")

    stock = yf.Ticker(TICKER)

    # ===================================================
    # 1. Historical Prices
    # ===================================================

    print("Downloading Historical Prices...")

    prices = yf.download(
        TICKER,
        period=PRICE_PERIOD,
        interval=PRICE_INTERVAL,
        auto_adjust=False,
        progress=False
    )

    # Flatten MultiIndex columns if present
    if isinstance(prices.columns, pd.MultiIndex):
        prices.columns = prices.columns.get_level_values(0)

    save_csv(prices, "Historical_Prices.csv")

    # ===================================================
    # 2. Company Information
    # ===================================================

    print("Downloading Company Information...")

    info = stock.info

    info_df = pd.DataFrame(
        list(info.items()),
        columns=["Field", "Value"]
    )

    save_csv(info_df, "Company_Info.csv")

    # ===================================================
    # 3. Company Metrics
    # ===================================================

    print("Downloading Company Metrics...")

    metrics = {

        "Company": info.get("longName"),

        "Ticker": TICKER,

        "Current Price": info.get("currentPrice"),

        "Previous Close": info.get("previousClose"),

        "Open": info.get("open"),

        "52 Week High": info.get("fiftyTwoWeekHigh"),

        "52 Week Low": info.get("fiftyTwoWeekLow"),

        "Market Cap": info.get("marketCap"),

        "Enterprise Value": info.get("enterpriseValue"),

        "Shares Outstanding": info.get("sharesOutstanding"),

        "Trailing EPS": info.get("trailingEps"),

        "Forward EPS": info.get("forwardEps"),

        "Trailing PE": info.get("trailingPE"),

        "Forward PE": info.get("forwardPE"),

        "Book Value": info.get("bookValue"),

        "Price to Book": info.get("priceToBook"),

        "Dividend Rate": info.get("dividendRate"),

        "Dividend Yield": info.get("dividendYield"),

        "Payout Ratio": info.get("payoutRatio"),

        "Beta": info.get("beta"),

        "Currency": info.get("currency"),

        "Sector": info.get("sector"),

        "Industry": info.get("industry")

    }

    metrics_df = pd.DataFrame(
        metrics.items(),
        columns=["Metric", "Value"]
    )

    save_csv(metrics_df, "Company_Metrics.csv")

    # ===================================================
    # 4. Annual Income Statement
    # ===================================================

    print("Downloading Annual Income Statement...")

    income = stock.financials

    save_csv(
        income,
        "Annual_Income_Statement.csv"
    )

    # ===================================================
    # 5. Quarterly Income Statement
    # ===================================================

    print("Downloading Quarterly Income Statement...")

    q_income = stock.quarterly_financials

    save_csv(
        q_income,
        "Quarterly_Income_Statement.csv"
    )

    # ===================================================
    # 6. Annual Balance Sheet
    # ===================================================

    print("Downloading Balance Sheet...")

    balance = stock.balance_sheet

    save_csv(
        balance,
        "Annual_Balance_Sheet.csv"
    )

    # ===================================================
    # 7. Quarterly Balance Sheet
    # ===================================================

    print("Downloading Quarterly Balance Sheet...")

    q_balance = stock.quarterly_balance_sheet

    save_csv(
        q_balance,
        "Quarterly_Balance_Sheet.csv"
    )

    # ===================================================
    # 8. Annual Cash Flow
    # ===================================================

    print("Downloading Cash Flow Statement...")

    cashflow = stock.cashflow

    save_csv(
        cashflow,
        "Annual_Cash_Flow.csv"
    )

    # ===================================================
    # 9. Quarterly Cash Flow
    # ===================================================

    print("Downloading Quarterly Cash Flow...")

    q_cashflow = stock.quarterly_cashflow

    save_csv(
        q_cashflow,
        "Quarterly_Cash_Flow.csv"
    )

    # ===================================================
    # 10. Dividend History
    # ===================================================

    print("Downloading Dividend History...")

    dividends = stock.dividends

    dividends.to_frame(
        name="Dividend"
    ).to_csv(
        RAW_DATA / "Dividend_History.csv"
    )

    print("✓ Saved Dividend_History.csv")

    # ===================================================
    # 11. Stock Splits
    # ===================================================

    print("Downloading Stock Split History...")

    splits = stock.splits

    splits.to_frame(
        name="Split Ratio"
    ).to_csv(
        RAW_DATA / "Stock_Splits.csv"
    )

    print("✓ Saved Stock_Splits.csv")

    # ===================================================
    # Finished
    # ===================================================

    print("\n===================================")
    print("DATA COLLECTION COMPLETE")
    print("===================================")

    print("\nFiles Created:\n")

    files = [

        "Historical_Prices.csv",

        "Company_Info.csv",

        "Company_Metrics.csv",

        "Annual_Income_Statement.csv",

        "Quarterly_Income_Statement.csv",

        "Annual_Balance_Sheet.csv",

        "Quarterly_Balance_Sheet.csv",

        "Annual_Cash_Flow.csv",

        "Quarterly_Cash_Flow.csv",

        "Dividend_History.csv",

        "Stock_Splits.csv"

    ]

    for f in files:
        print("✓", f)