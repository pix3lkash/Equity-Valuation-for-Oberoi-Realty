"""
=========================================================
CHART GENERATION
Project: Oberoi Realty Valuation
=========================================================
Generates all charts used in the Excel report.
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
from config import *


def generate_charts():

    print("\nGenerating Charts...\n")

    # -------------------------------------------------
    # Price History
    # -------------------------------------------------

    prices = pd.read_csv(RAW_DATA / "Historical_Prices.csv")

    prices["Date"] = pd.to_datetime(
        prices["Date"],
        format="%Y-%m-%d"
    )

    plt.figure(figsize=(10, 5))
    plt.plot(prices["Date"], prices["Close"])
    plt.title("Oberoi Realty Share Price")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.grid(True)

    plt.savefig(CHARTS / "price_history.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # Financial Summary
    # -------------------------------------------------

    financial = pd.read_csv(
        PROCESSED_DATA / "Financial_Summary.csv",
        index_col=0
    )

    revenue = financial.loc["Revenue"]
    income = financial.loc["Net Income"]

    plt.figure(figsize=(9, 5))

    plt.plot(
        revenue.index,
        revenue.values / 1e9,
        marker="o",
        label="Revenue"
    )

    plt.plot(
        income.index,
        income.values / 1e9,
        marker="o",
        label="Net Income"
    )

    plt.legend()
    plt.grid(True)
    plt.ylabel("₹ Billion")
    plt.title("Revenue vs Net Income")

    plt.savefig(CHARTS / "revenue_vs_profit.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # Balance Sheet
    # -------------------------------------------------

    assets = financial.loc["Total Assets"] / 1e9
    liabilities = financial.loc["Total Liabilities"] / 1e9
    equity = financial.loc["Equity"] / 1e9

    plt.figure(figsize=(10, 5))

    plt.bar(assets.index, assets, label="Assets")
    plt.bar(liabilities.index, liabilities, label="Liabilities")
    plt.bar(equity.index, equity, label="Equity")

    plt.legend()
    plt.ylabel("₹ Billion")
    plt.title("Balance Sheet")

    plt.savefig(CHARTS / "balance_sheet.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # Technical Indicators
    # -------------------------------------------------

    tech = pd.read_csv(
        OUTPUT / "Technical_Indicators.csv"
    )

    tech["Date"] = pd.to_datetime(
        tech["Date"],
        format="%Y-%m-%d"
    )

    plt.figure(figsize=(12, 5))

    plt.plot(
        tech["Date"],
        tech["Close"],
        label="Close"
    )

    plt.plot(
        tech["Date"],
        tech["SMA_50"],
        label="50 DMA"
    )

    plt.plot(
        tech["Date"],
        tech["SMA_200"],
        label="200 DMA"
    )

    plt.legend()
    plt.grid(True)
    plt.title("Moving Average Analysis")

    plt.savefig(CHARTS / "technical_indicators.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # DCF Waterfall
    # -------------------------------------------------

    dcf = pd.read_csv(
        OUTPUT / "DCF_Valuation.csv"
    )

    values = dcf.iloc[5:10]

    plt.figure(figsize=(8, 5))

    plt.bar(
        values["Metric"],
        values["Value"] / 1e9
    )

    plt.ylabel("₹ Billion")
    plt.xticks(rotation=20)
    plt.title("DCF Valuation Components")
    plt.tight_layout()

    plt.savefig(CHARTS / "dcf_waterfall.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # Valuation Comparison
    # -------------------------------------------------

    market_price = 1882.7

    dcf_value = dcf.loc[
        dcf["Metric"] == "Intrinsic Value Per Share",
        "Value"
    ].values[0]

    ddm = pd.read_csv(
        OUTPUT / "DDM_Valuation.csv"
    )

    ddm_value = ddm.loc[
        ddm["Metric"] == "Intrinsic Value",
        "Value"
    ].values[0]

    plt.figure(figsize=(6, 5))

    plt.bar(
        ["Market", "DCF", "DDM"],
        [market_price, dcf_value, ddm_value]
    )

    plt.ylabel("₹")
    plt.title("Valuation Comparison")

    plt.savefig(CHARTS / "valuation_comparison.png", dpi=300)
    plt.close()

    # -------------------------------------------------
    # Price Prediction
    # -------------------------------------------------

    pred = pd.read_csv(
        OUTPUT / "Price_Prediction.csv"
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        pred["Period"],
        pred["Predicted Price"],
        marker="o"
    )

    plt.grid(True)
    plt.ylabel("₹")
    plt.title("Predicted Share Price")

    plt.savefig(CHARTS / "predicted_prices.png", dpi=300)
    plt.close()

    print("✓ Charts created successfully")


if __name__ == "__main__":
    generate_charts()