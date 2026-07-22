"""
=========================================================
DIVIDEND DISCOUNT MODEL (DDM)
Project: Oberoi Realty Valuation
=========================================================
Calculates:

✓ Average Dividend
✓ Dividend Growth Rate
✓ Required Return
✓ Intrinsic Value

Output:
DDM_Valuation.csv
=========================================================
"""

import pandas as pd
import numpy as np

from src import capm
from config import *


def calculate_ddm():

    print("\nCalculating Dividend Discount Model...\n")

    # -----------------------------------------
    # Read Dividend History
    # -----------------------------------------

    dividends = pd.read_csv(
        RAW_DATA / "Dividend_History.csv"
    )

    if dividends.empty:

        print("No dividend history available.")

        return

    # -----------------------------------------
    # Get dividend column
    # -----------------------------------------

    dividend = dividends.iloc[:, -1]

    dividend = dividend.dropna()

    if len(dividend) < 2:

        print("Not enough dividend data.")

        return

    # -----------------------------------------
    # Current Dividend
    # -----------------------------------------

    D0 = dividend.iloc[-1]

    # -----------------------------------------
    # Growth Rate
    # -----------------------------------------

    growth_rates = dividend.pct_change()

    growth = growth_rates.mean()

    # Keep growth reasonable
    if np.isnan(growth):

        growth = 0.05

    growth = min(max(growth, 0), 0.15)

    # -----------------------------------------
    # Required Return
    # -----------------------------------------

    # Load CAPM results
    capm = pd.read_csv(OUTPUT / "CAPM.csv")

# Cost of Equity from CAPM
    REQUIRED_RETURN = float(
        capm.loc[
            capm["Metric"] == "Cost of Equity",
            "Value"
        ].iloc[0]
)

    # -----------------------------------------
    # Next Year's Dividend
    # -----------------------------------------

    D1 = D0 * (1 + growth)

    # -----------------------------------------
    # Gordon Growth Model
    # -----------------------------------------

    if REQUIRED_RETURN <= growth:

        intrinsic = np.nan

    else:

        intrinsic = D1 / (
            REQUIRED_RETURN - growth
        )

    # -----------------------------------------
    # Save Results
    # -----------------------------------------

    results = pd.DataFrame({

        "Metric": [

            "Current Dividend",

            "Dividend Growth",

            "Required Return",

            "Intrinsic Value"

        ],

        "Value": [

            D0,

            growth,

            REQUIRED_RETURN,

            intrinsic

        ]

    })

    results.to_csv(

        OUTPUT /

        "DDM_Valuation.csv",

        index=False

    )

    print(results)

    print("\n✓ DDM Valuation Saved")

    return results


if __name__ == "__main__":

    calculate_ddm()