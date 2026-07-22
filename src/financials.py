"""
=========================================================
FINANCIAL STATEMENTS PROCESSING
Project: Oberoi Realty Valuation
=========================================================
Reads raw financial statements from Yahoo Finance

Creates a clean financial summary

Output:
Financial_Summary.csv
=========================================================
"""

import pandas as pd
from config import *


# -------------------------------------------------------
# Helper Function
# -------------------------------------------------------

def get_value(df, possible_names):
    """
    Search for a financial statement row using
    several possible names.
    """

    for name in possible_names:

        if name in df.index:

            return df.loc[name]

    return pd.Series(dtype="float64")


# -------------------------------------------------------
# Main Function
# -------------------------------------------------------

def process_financials():

    print("\nProcessing Financial Statements...\n")

    # ---------------------------------------------
    # Read Files
    # ---------------------------------------------

    income = pd.read_csv(
        RAW_DATA / "Annual_Income_Statement.csv",
        index_col=0
    )

    balance = pd.read_csv(
        RAW_DATA / "Annual_Balance_Sheet.csv",
        index_col=0
    )

    cashflow = pd.read_csv(
        RAW_DATA / "Annual_Cash_Flow.csv",
        index_col=0
    )

    # ---------------------------------------------
    # Income Statement
    # ---------------------------------------------

    revenue = get_value(
        income,
        [
            "Total Revenue",
            "Operating Revenue",
            "Revenue"
        ]
    )

    ebit = get_value(
        income,
        [
            "EBIT",
            "Operating Income"
        ]
    )

    net_income = get_value(
        income,
        [
            "Net Income",
            "Net Income Common Stockholders",
            "Net Income From Continuing Operation Net Minority Interest"
        ]
    )

    gross_profit = get_value(
        income,
        [
            "Gross Profit"
        ]
    )

    operating_expense = get_value(
        income,
        [
            "Operating Expense",
            "Operating Expenses"
        ]
    )

    # ---------------------------------------------
    # Balance Sheet
    # ---------------------------------------------

    total_assets = get_value(
        balance,
        [
            "Total Assets"
        ]
    )

    total_liabilities = get_value(
        balance,
        [
            "Total Liabilities Net Minority Interest",
            "Total Liabilities"
        ]
    )

    equity = get_value(
        balance,
        [
            "Stockholders Equity",
            "Total Equity Gross Minority Interest",
            "Common Stock Equity"
        ]
    )

    cash = get_value(
        balance,
        [
            "Cash Cash Equivalents And Short Term Investments",
            "Cash And Cash Equivalents",
            "Cash"
        ]
    )

    debt = get_value(
        balance,
        [
            "Total Debt",
            "Long Term Debt",
            "Long Term Debt And Capital Lease Obligation"
        ]
    )

    current_assets = get_value(
        balance,
        [
            "Current Assets",
            "Total Current Assets"
        ]
    )

    current_liabilities = get_value(
        balance,
        [
            "Current Liabilities",
            "Total Current Liabilities"
        ]
    )

    # ---------------------------------------------
    # Cash Flow Statement
    # ---------------------------------------------

    depreciation = get_value(
        cashflow,
        [
            "Depreciation",
            "Depreciation And Amortization",
            "Reconciled Depreciation"
        ]
    )

    capex = get_value(
        cashflow,
        [
            "Capital Expenditure",
            "Capital Expenditures"
        ]
    )

    # Operating Cash Flow
    operating_cashflow = pd.to_numeric(
        cashflow.loc["Operating Cash Flow"],
        errors="coerce"
)

    free_cashflow = get_value(
        cashflow,
        [
            "Free Cash Flow"
        ]
    )

    # ---------------------------------------------
    # Working Capital
    # ---------------------------------------------

    working_capital = current_assets - current_liabilities

    # ---------------------------------------------
    # Financial Summary
    # ---------------------------------------------

    summary = pd.DataFrame({

        "Revenue": revenue,

        "EBIT": ebit,

        "Net Income": net_income,

        "Gross Profit": gross_profit,

        "Operating Expense": operating_expense,

        "Total Assets": total_assets,

        "Total Liabilities": total_liabilities,

        "Equity": equity,

        "Cash": cash,

        "Total Debt": debt,

        "Current Assets": current_assets,

        "Current Liabilities": current_liabilities,

        "Working Capital": working_capital,

        "Depreciation": depreciation,

        "CapEx": capex,

        "Operating Cash Flow": operating_cashflow,

        "Free Cash Flow": free_cashflow

    })

    summary = summary.T

    summary.to_csv(

        PROCESSED_DATA /

        "Financial_Summary.csv"

    )

    print("✓ Financial Summary Saved")

    print(summary)

    return summary


# -------------------------------------------------------
# Run File Directly
# -------------------------------------------------------

if __name__ == "__main__":

    process_financials()