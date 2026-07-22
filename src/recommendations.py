"""
=========================================================
RECOMMENDATION ENGINE
Project: Oberoi Realty Valuation
=========================================================

Creates an investment recommendation using:

1. DCF Valuation
2. Dividend Discount Model
3. P/E Ratio
4. P/B Ratio
5. P/S Ratio
6. CAPM
7. Technical Analysis (RSI)

Output:
Recommendation.csv
=========================================================
"""

import sys
from pathlib import Path
import pandas as pd

# -------------------------------------------------------
# Allow importing config.py from project root
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config import *

# -------------------------------------------------------
# Helper Functions
# -------------------------------------------------------

def get_ratio(df, ratio_name):
    """Return a financial ratio value."""
    return float(
        df.loc[df["Ratio"] == ratio_name, "Value"].iloc[0]
    )


def get_metric(df, metric_name):
    """Return a metric value."""
    return float(
        df.loc[df["Metric"] == metric_name, "Value"].iloc[0]
    )

def add_recommendation(
    recommendations,
    method,
    actual,
    benchmark,
    signal,
    reason
):
    """Append a recommendation entry."""
    recommendations.append({
        "Method": method,
        "Actual": actual,
        "Benchmark": benchmark,
        "Signal": signal,
        "Reason": reason
    })


# -------------------------------------------------------
# Main
# -------------------------------------------------------

def generate_recommendation():

    print("\nGenerating Recommendation...\n")

    # ---------------------------------------------------
    # Load Data
    # ---------------------------------------------------

    ratios = pd.read_csv(OUTPUT / "Financial_Ratios.csv")
    dcf = pd.read_csv(OUTPUT / "DCF_Valuation.csv")
    ddm = pd.read_csv(OUTPUT / "DDM_Valuation.csv")
    capm = pd.read_csv(OUTPUT / "CAPM.csv")
    tech = pd.read_csv(OUTPUT / "Technical_Indicators.csv")

    # Current Market Price (latest close)

    market_price = float(tech["Close"].iloc[-1])

    recommendations = []

    # ---------------------------------------------------
    # DCF
    # ---------------------------------------------------

    dcf_value = get_metric(dcf, "Intrinsic Value Per Share")

    dcf_signal = "BUY" if dcf_value > market_price else "SELL"

    add_recommendation(
    recommendations,
    "DCF",
    round(dcf_value, 2),
    round(market_price, 2),
    dcf_signal,
    "Intrinsic Value vs Market Price"
)

    # ---------------------------------------------------
    # DDM
    # ---------------------------------------------------

    ddm_value = get_metric(ddm, "Intrinsic Value")

    ddm_signal = "BUY" if ddm_value > market_price else "SELL"

    add_recommendation(
    recommendations,
    "DDM",
    round(ddm_value, 2),
    round(market_price, 2),
    ddm_signal,
    "Dividend Discount Model"
)

    # ---------------------------------------------------
    # P/E
    # ---------------------------------------------------

    pe = get_ratio(ratios, "P/E")
    sector_pe = 35.0

    if pe < sector_pe * 0.90:
        pe_signal = "BUY"
    elif pe > sector_pe * 1.10:
        pe_signal = "SELL"
    else:
        pe_signal = "HOLD"

    add_recommendation(
    recommendations,
    "P/E",
    round(pe, 2),
    sector_pe,
    pe_signal,
    "Compared with Sector Average"
)

    # ---------------------------------------------------
    # P/B
    # ---------------------------------------------------

    pb = get_ratio(ratios, "P/B")
    sector_pb = 5.0

    if pb < sector_pb * 0.90:
        pb_signal = "BUY"
    elif pb > sector_pb * 1.10:
        pb_signal = "SELL"
    else:
        pb_signal = "HOLD"

    add_recommendation(
    recommendations,
    "P/B",
    round(pb, 2),
    sector_pb,
    pb_signal,
    "Compared with Sector Average"
)

    # ---------------------------------------------------
    # P/S
    # ---------------------------------------------------

    ps = get_ratio(ratios, "P/S")
    sector_ps = 12.0

    if ps < sector_ps * 0.90:
        ps_signal = "BUY"
    elif ps > sector_ps * 1.10:
        ps_signal = "SELL"
    else:
        ps_signal = "HOLD"

    
    add_recommendation(
        recommendations,
        "P/S",
        round(ps, 2),
        sector_ps,
        ps_signal,
        "Compared with Sector Average"
)

    # ---------------------------------------------------
    # CAPM
    # ---------------------------------------------------

    cost_of_equity = get_metric(capm, "Cost of Equity")

    if cost_of_equity < 0.10:
        capm_signal = "BUY"
    elif cost_of_equity > 0.15:
        capm_signal = "SELL"
    else:
        capm_signal = "HOLD"

    add_recommendation(
    recommendations,
    "CAPM",
    round(cost_of_equity * 100, 2),
    "10% - 15%",
    capm_signal,
    "Cost of Equity"
)

    # ---------------------------------------------------
    # Technical Analysis
    # ---------------------------------------------------

    rsi_signal = str(tech["RSI_Signal"].iloc[-1]).upper()

    if rsi_signal not in ["BUY", "SELL", "HOLD"]:
        rsi_signal = "HOLD"

    latest_rsi = round(float(tech["RSI"].iloc[-1]), 2)

    add_recommendation(
    recommendations,
    "Technical",
    latest_rsi,
    "RSI (30 / 70)",
    rsi_signal,
    "Latest RSI Signal"
)

    # ---------------------------------------------------
    # Majority Vote
    # ---------------------------------------------------

    signals = [r["Signal"] for r in recommendations]

    buy_votes = signals.count("BUY")
    hold_votes = signals.count("HOLD")
    sell_votes = signals.count("SELL")

    vote_summary = {
    "BUY": buy_votes,
    "HOLD": hold_votes,
    "SELL": sell_votes
}

    max_votes = max(vote_summary.values())

    leaders = [
        signal
        for signal, votes in vote_summary.items()
        if votes == max_votes
]

    if len(leaders) == 1:
        overall = leaders[0]
    else:
        overall = "HOLD"

    add_recommendation(
        recommendations,
        "OVERALL",
        f"BUY={buy_votes}, HOLD={hold_votes}, SELL={sell_votes}",
        "-",
        overall,
        "Majority Vote Across All Methods"
)

    # ---------------------------------------------------
    # Save Output
    # ---------------------------------------------------

    recommendation_df = pd.DataFrame(recommendations)

    recommendation_df.to_csv(
        OUTPUT / "Recommendation.csv",
        index=False
    )

    print(recommendation_df)

    print("\n✓ Recommendation Saved")

    return recommendation_df


if __name__ == "__main__":
    generate_recommendation()