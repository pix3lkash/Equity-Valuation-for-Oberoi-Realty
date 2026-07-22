"""
=========================================================
RATIO ANALYSIS
Project: Oberoi Realty Valuation
=========================================================
Calculates key financial ratios

Output:
Financial_Ratios.csv
=========================================================
"""

import pandas as pd
import numpy as np
from config import *


def get_metric(metrics_df, metric_name):
    """Return a metric value from Company_Metrics.csv"""

    row = metrics_df.loc[metrics_df["Metric"] == metric_name]

    if row.empty:
        return np.nan

    return row.iloc[0]["Value"]


def process_ratios():

    print("\nCalculating Financial Ratios...\n")

    # --------------------------------------------
    # Read Files
    # --------------------------------------------

    financial = pd.read_csv(
        PROCESSED_DATA / "Financial_Summary.csv",
        index_col=0
    )

    metrics = pd.read_csv(
        RAW_DATA / "Company_Metrics.csv"
    )

    # --------------------------------------------
    # Latest Year
    # --------------------------------------------

    latest = financial.columns[-1]

    revenue = pd.to_numeric(financial.loc["Revenue", latest], errors="coerce")
    net_income = pd.to_numeric(financial.loc["Net Income", latest], errors="coerce")
    equity = pd.to_numeric(financial.loc["Equity", latest], errors="coerce")
    assets = pd.to_numeric(financial.loc["Total Assets", latest], errors="coerce")
    liabilities = pd.to_numeric(financial.loc["Total Liabilities", latest], errors="coerce")
    debt = pd.to_numeric(financial.loc["Total Debt", latest], errors="coerce")
    current_assets = pd.to_numeric(financial.loc["Current Assets", latest], errors="coerce")
    current_liabilities = pd.to_numeric(financial.loc["Current Liabilities", latest], errors="coerce")
    operating_cf = pd.to_numeric(financial.loc["Operating Cash Flow", latest], errors="coerce")

    print("Latest year:", latest)
    print("Operating CF:", operating_cf)
    print("Current Liabilities:", current_liabilities)
    # --------------------------------------------
    # Company Metrics
    # --------------------------------------------

    pe = get_metric(metrics, "Trailing PE")
    pb = get_metric(metrics, "Price to Book")
    eps = get_metric(metrics, "Trailing EPS")
    market_cap = pd.to_numeric(get_metric(metrics, "Market Cap"), errors="coerce")
    shares = pd.to_numeric(get_metric(metrics, "Shares Outstanding"), errors="coerce")
    beta = pd.to_numeric(get_metric(metrics, "Beta"), errors="coerce")

    # --------------------------------------------
    # Calculations
    # --------------------------------------------

    roe = net_income / equity if equity else np.nan

    roa = net_income / assets if assets else np.nan

    debt_equity = debt / equity if equity else np.nan

    current_ratio = (
        current_assets / current_liabilities
        if current_liabilities else np.nan
    )

    net_margin = (
        net_income / revenue
        if revenue else np.nan
    )

    operating_cf_ratio = (
        operating_cf / current_liabilities
        if current_liabilities else np.nan
    )

    # --------------------------------------------
    # Placeholder values
    # --------------------------------------------

    ps = np.nan
    peg = np.nan

    if market_cap and revenue:
        ps = market_cap / revenue

    # PEG requires earnings growth
    # We will calculate it later

    # --------------------------------------------
    # Output Table
    # --------------------------------------------

    ratios = pd.DataFrame({

        "Ratio": [

            "P/E",

            "P/B",

            "P/S",

            "PEG",

            "EPS",

            "ROE",

            "ROA",

            "Debt to Equity",

            "Current Ratio",

            "Net Profit Margin",

            "Operating Cash Flow Ratio",

            "Beta"

        ],

        "Value": [

            pe,

            pb,

            ps,

            peg,

            eps,

            roe,

            roa,

            debt_equity,

            current_ratio,

            net_margin,

            operating_cf_ratio,

            beta

        ]

    })

    ratios.to_csv(

        OUTPUT /

        "Financial_Ratios.csv",

        index=False

    )

    print("✓ Financial_Ratios.csv Saved")

    print(ratios)

    return ratios


if __name__ == "__main__":

    process_ratios()