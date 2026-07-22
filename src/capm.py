"""
=========================================================
CAPM (Capital Asset Pricing Model)
Project: Oberoi Realty Valuation
=========================================================
Calculates:

✓ Beta
✓ Market Risk Premium
✓ Cost of Equity

Output:
CAPM.csv
=========================================================
"""

import pandas as pd
import numpy as np
from config import *


def get_metric(metrics_df, metric):

    row = metrics_df.loc[
        metrics_df["Metric"] == metric
    ]

    if row.empty:

        return np.nan

    return row.iloc[0]["Value"]


def calculate_capm():

    print("\nCalculating CAPM...\n")

    # ---------------------------------------
    # Read Company Metrics
    # ---------------------------------------

    metrics = pd.read_csv(
        RAW_DATA / "Company_Metrics.csv"
    )

    beta = pd.to_numeric(
    get_metric(metrics, "Beta"),
    errors="coerce"
)

    # ---------------------------------------
    # Assumptions
    # ---------------------------------------

    # Update these with current values if needed
    risk_free_rate = 0.07      # 7%
    market_return = 0.13       # 13%

    market_risk_premium = (
        market_return - risk_free_rate
    )

    # ---------------------------------------
    # Missing Beta?
    # ---------------------------------------

    if pd.isna(beta):
        print("Beta not available. Using Beta = 1.0")
        beta = 1.0

    # ---------------------------------------
    # CAPM
    # ---------------------------------------

    cost_of_equity = (

        risk_free_rate +

        beta * market_risk_premium

    )

    # ---------------------------------------
    # Save
    # ---------------------------------------

    capm = pd.DataFrame({

        "Metric": [

            "Risk Free Rate",

            "Market Return",

            "Market Risk Premium",

            "Beta",

            "Cost of Equity"

        ],

        "Value": [

            risk_free_rate,

            market_return,

            market_risk_premium,

            beta,

            cost_of_equity

        ]

    })

    capm.to_csv(

        OUTPUT /

        "CAPM.csv",

        index=False

    )

    print(capm)

    print("\n✓ CAPM Saved")

    return capm


if __name__ == "__main__":

    calculate_capm()