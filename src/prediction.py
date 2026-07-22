"""
=========================================================
PRICE PREDICTION
Project: Oberoi Realty Valuation
=========================================================
Predicts:
✓ 1 Month Price
✓ 2 Month Price
✓ 3 Month Price

Output:
Price_Prediction.csv
=========================================================
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from config import *


def predict_prices():

    print("\nPredicting Future Prices...\n")

    # ---------------------------------------------
    # Read Historical Prices
    # ---------------------------------------------

    df = pd.read_csv(
        RAW_DATA / "Historical_Prices.csv"
    )

    # ---------------------------------------------
    # Find Close Price Column
    # ---------------------------------------------

    if "Close" in df.columns:
        close = df["Close"]

    elif "Adj Close" in df.columns:
        close = df["Adj Close"]

    else:
        raise Exception("Close price not found.")

    close = close.dropna().reset_index(drop=True)

    # ---------------------------------------------
    # Create Regression Data
    # ---------------------------------------------

    X = np.arange(len(close)).reshape(-1, 1)

    y = close.values

    model = LinearRegression()

    model.fit(X, y)

    # ---------------------------------------------
    # Forecast
    # ---------------------------------------------

    days_1 = len(close) + 30
    days_2 = len(close) + 60
    days_3 = len(close) + 90

    pred1 = model.predict([[days_1]])[0]
    pred2 = model.predict([[days_2]])[0]
    pred3 = model.predict([[days_3]])[0]

    # ---------------------------------------------
    # Save Results
    # ---------------------------------------------

    prediction = pd.DataFrame({

        "Period": [

            "Current",

            "1 Month",

            "2 Months",

            "3 Months"

        ],

        "Predicted Price": [

            close.iloc[-1],

            pred1,

            pred2,

            pred3

        ]

    })

    prediction.to_csv(

        OUTPUT /

        "Price_Prediction.csv",

        index=False

    )

    print(prediction)

    print("\n✓ Price Prediction Saved")

    return prediction


if __name__ == "__main__":

    predict_prices()