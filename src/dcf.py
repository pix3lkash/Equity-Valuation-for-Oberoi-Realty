"""
=========================================================
DISCOUNTED CASH FLOW (DCF) VALUATION
Project: Oberoi Realty Valuation
=========================================================
"""

import pandas as pd
from config import *


def get_row(df, names):
    """Return the first matching row from the financial summary."""
    for name in names:
        if name in df.index:
            return df.loc[name]
    return pd.Series(dtype="float64")


def calculate_dcf():

    print("\nCalculating DCF Valuation...\n")

    # -------------------------------------------------
    # Load processed financial summary
    # -------------------------------------------------

    financial = pd.read_csv(
        PROCESSED_DATA / "Financial_Summary.csv",
        index_col=0
    )

    # Most recent year
    latest = financial.columns[-1]

    # -------------------------------------------------
    # Required financials
    # -------------------------------------------------

    revenue = financial.loc["Revenue", latest]
    ebit = financial.loc["EBIT", latest]
    depreciation = financial.loc["Depreciation", latest]
    capex = financial.loc["CapEx", latest]
    working_capital_current = financial.loc["Working Capital", latest]

    previous_year = financial.columns[-2]

    working_capital_previous = financial.loc[
        "Working Capital",
        previous_year
]

    delta_working_capital = (
        working_capital_current - working_capital_previous
)

    cash = financial.loc["Cash", latest]
    debt = financial.loc["Total Debt", latest]

    # -------------------------------------------------
    # Assumptions
    # -------------------------------------------------

    TAX_RATE = 0.25

    GROWTH_RATE = 0.08

    TERMINAL_GROWTH = 0.04

    WACC = 0.11

    company_info = pd.read_csv(
        RAW_DATA / "Company_Info.csv"
)

    SHARES_OUTSTANDING = float(
        company_info.loc[
            company_info["Field"] == "sharesOutstanding",
        "Value"
    ].iloc[0]
)

    print(f"Shares Outstanding: {SHARES_OUTSTANDING:,.0f}")    

    # -------------------------------------------------
    # NOPAT
    # -------------------------------------------------

    nopat = ebit * (1 - TAX_RATE)

    # -------------------------------------------------
    # FCFF
    # -------------------------------------------------

    fcff = (
        nopat
        + depreciation
        - abs(capex)
        - delta_working_capital
    )

    # -------------------------------------------------
    # Project FCFF
    # -------------------------------------------------

    projected_fcff = []

    current = fcff

    for _ in range(5):

        current *= (1 + GROWTH_RATE)

        projected_fcff.append(current)

    # -------------------------------------------------
    # Discount FCFF
    # -------------------------------------------------

    discounted = []

    for year, cashflow in enumerate(projected_fcff, start=1):

        pv = cashflow / ((1 + WACC) ** year)

        discounted.append(pv)

    # -------------------------------------------------
    # Terminal Value
    # -------------------------------------------------

    terminal_fcff = projected_fcff[-1] * (1 + TERMINAL_GROWTH)

    terminal_value = terminal_fcff / (
        WACC - TERMINAL_GROWTH
    )

    terminal_pv = terminal_value / ((1 + WACC) ** 5)

    # -------------------------------------------------
    # Enterprise Value
    # -------------------------------------------------

    enterprise_value = sum(discounted) + terminal_pv

    # -------------------------------------------------
    # Equity Value
    # -------------------------------------------------

    equity_value = enterprise_value + cash - debt

    intrinsic_value = equity_value / SHARES_OUTSTANDING

    # -------------------------------------------------
    # Save Results
    # -------------------------------------------------

    dcf = pd.DataFrame({

        "Metric": [

            "Revenue",

            "EBIT",

            "NOPAT",

            "Depreciation",

            "CapEx",

            "FCFF",

            "Enterprise Value",

            "Cash",

            "Debt",

            "Equity Value",

            "Intrinsic Value Per Share"

        ],

        "Value": [

            revenue,

            ebit,

            nopat,

            depreciation,

            capex,

            fcff,

            enterprise_value,

            cash,

            debt,

            equity_value,

            intrinsic_value

        ]

    })

    dcf.to_csv(

        OUTPUT /

        "DCF_Valuation.csv",

        index=False

    )

    print(dcf)

    print("\n✓ DCF Valuation Saved")

    return dcf


if __name__ == "__main__":

    calculate_dcf()