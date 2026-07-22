"""
=========================================================
TECHNICAL ANALYSIS
Project: Oberoi Realty Valuation
=========================================================
Calculates:
✓ SMA 20
✓ SMA 50
✓ SMA 200
✓ EMA 20
✓ RSI (14)
✓ MACD
✓ Bollinger Bands
✓ Daily Returns

Output:
Technical_Indicators.csv
=========================================================
"""

import pandas as pd
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
from config import *


def process_technicals():

    print("\nCalculating Technical Indicators...\n")

    # -------------------------------------
    # Read Historical Prices
    # -------------------------------------

    df = pd.read_csv(
        RAW_DATA / "Historical_Prices.csv"
    )

    # -------------------------------------
    # Find the Close column
    # -------------------------------------

    if "Close" in df.columns:
        close = df["Close"]

    elif "Adj Close" in df.columns:
        close = df["Adj Close"]

    else:
        raise ValueError(
            "Could not find Close price column."
        )

    # -------------------------------------
    # Moving Averages
    # -------------------------------------

    df["SMA_20"] = SMAIndicator(
        close,
        window=20
    ).sma_indicator()

    df["SMA_50"] = SMAIndicator(
        close,
        window=50
    ).sma_indicator()

    df["SMA_200"] = SMAIndicator(
        close,
        window=200
    ).sma_indicator()

    # -------------------------------------
    # EMA
    # -------------------------------------

    df["EMA_20"] = EMAIndicator(
        close,
        window=20
    ).ema_indicator()

    # -------------------------------------
    # RSI
    # -------------------------------------

    df["RSI"] = RSIIndicator(
        close,
        window=14
    ).rsi()

    # -------------------------------------
    # MACD
    # -------------------------------------

    macd = MACD(close)

    df["MACD"] = macd.macd()

    df["MACD_Signal"] = macd.macd_signal()

    df["MACD_Histogram"] = macd.macd_diff()

    # -------------------------------------
    # Bollinger Bands
    # -------------------------------------

    bb = BollingerBands(close)

    df["BB_High"] = bb.bollinger_hband()

    df["BB_Low"] = bb.bollinger_lband()

    df["BB_Middle"] = bb.bollinger_mavg()

    # -------------------------------------
    # Daily Returns
    # -------------------------------------

    df["Daily_Return"] = close.pct_change()

    # -------------------------------------
    # Trading Signal
    # -------------------------------------

    signal = []

    for _, row in df.iterrows():

        if row["RSI"] < 30:

            signal.append("BUY")

        elif row["RSI"] > 70:

            signal.append("SELL")

        else:

            signal.append("HOLD")

    df["RSI_Signal"] = signal

    # -------------------------------------
    # Save
    # -------------------------------------

    df.to_csv(

        OUTPUT /

        "Technical_Indicators.csv",

        index=False

    )

    print("✓ Technical_Indicators.csv Saved")

    return df


if __name__ == "__main__":

    process_technicals()