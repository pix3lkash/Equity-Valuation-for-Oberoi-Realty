# Oberoi Realty Equity Valuation & Financial Analysis

A complete Python-based financial analysis pipeline that automatically downloads financial data from Yahoo Finance, performs ratio analysis, technical analysis, intrinsic valuation, and generates a professional Excel report.

---

# Overview

This project automates the valuation of Oberoi Realty Ltd. (NSE: OBEROIRLTY) using multiple financial models.

The project:
- downloads financial data directly from Yahoo Finance
- cleans and processes statements
- calculates important financial ratios
- performs technical analysis
- estimates intrinsic value using DCF
- values dividends using DDM
- calculates cost of equity using CAPM
- predicts future prices using linear regression
- generates a professional Excel report

---

# Features

-Automatic data collection using yfinance
-Income Statement processing
-Balance Sheet processing
-Cash Flow processing
-Financial Ratio Analysis
- P/E
- P/B
- P/S
- ROE
- ROA
- Current Ratio
- Debt-to-Equity
- Net Profit Margin
- Operating Cash Flow Ratio
- EPS
- Beta

Technical Indicators:
- SMA
- EMA
- RSI
- MACD
- Bollinger Bands
- Daily Returns
- Volatility
-Discounted Cash Flow (DCF)
-Dividend Discount Model (DDM)
-CAPM Cost of Equity

---

# Project Workflow

Yahoo Finance
      │
      ▼
Data Collection
      │
      ▼
Financial Statement Cleaning
      │
      ▼
Financial Ratios
      │
      ▼
Technical Analysis
      │
      ▼
DCF Valuation
      │
      ▼
Dividend Discount Model
      │
      ▼
    CAPM
      │
      ▼
Price Prediction
      │
      ▼
Excel Report

---

#Project Structure

OberoiStock/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config.py
│
├── data/
│   ├── raw/
│   │   ├── Annual_Income_Statement.csv
│   │   ├── Annual_Balance_Sheet.csv
│   │   ├── Annual_Cash_Flow.csv
│   │   ├── Historical_Prices.csv
│   │   ├── Company_Info.csv
│   │   ├── Company_Metrics.csv
│   │   ├── Dividend_History.csv
│   │   └── ...
│   │
│   └── processed/
│       ├── Financial_Summary.csv
│       ├── Financial_Ratios.csv
│       └── Technical_Indicators.csv
│
├── output/
│   ├── CAPM.csv
│   ├── DCF_Valuation.csv
│   ├── DDM_Valuation.csv
│   ├── Price_Prediction.csv
│   └── ...
│
├── report/
│   └── Final_Report.xlsx
│
├── charts/
│   ├── price_chart.png
│   ├── rsi.png
│   ├── macd.png
│   └── ...
│
└── src/
    ├── data_collection.py
    ├── financials.py
    ├── ratios.py
    ├── technicals.py
    ├── dcf.py
    ├── ddm.py
    ├── capm.py
    ├── prediction.py
    ├── report.py
    └── test.py

---

# Tech Stack

Python

Libraries:
- pandas
- numpy
- yfinance
- matplotlib
- scikit-learn
- openpyxl
- yfinance
- ta

Finance Concepts:
- CAPM
- Discounted Cash Flow
- Dividend Discount Model
- Financial Ratio Analysis
- Technical Indicators

---

# Financial Models Used

1. Discounted Cash Flow (DCF)

Enterprise Value is calculated using projected Free Cash Flow to Firm (FCFF).

Formula

FCFF = NOPAT + Depreciation − CapEx

Projected for five years and discounted using WACC.

2. Dividend Discount Model (DDM)

Intrinsic Value = D₁ / (r − g)

where
- D₁ = Expected Dividend
- r = Cost of Equity (CAPM)
- g = Dividend Growth Rate

3. CAPM

Cost of Equity = Risk Free Rate + Beta × Market Risk Premium

4. Financial Ratios

The project calculates:
- Profitability Ratios
- Liquidity Ratios
- Leverage Ratios
- Valuation Ratios
- Cash Flow Ratios

---

# Sample Results

Latest Financial Highlights

| Metric | Value |
|---------|--------:|
| Revenue | ₹60.09 Billion |
| Net Income | ₹25.07 Billion |
| Operating Cash Flow | ₹13.80 Billion |
| Current Ratio | 3.99 |
| ROE | 13.99% |
| ROA | 9.90% |
| DCF Intrinsic Value | ₹436.01/share |
| Current Market Price | ~₹1883/share |

---

# Assumptions

The valuation uses the following assumptions:

- Tax Rate = 25%
- FCFF Growth Rate (Years 1–5): 8%
- Terminal Growth = 4%
- WACC = 11%
- Cost of Equity = CAPM
- Shares Outstanding = Yahoo Finance

---

# Limitations

The project is intended for educational purposes.

Limitations include:
- Uses Yahoo Finance data
- Simplified DCF assumptions
- Constant growth model
- Simple linear regression for price prediction
- Does not include sensitivity analysis
- Does not include Monte Carlo simulation

---

# How to Run

Clone the repository
git clone https://github.com/yourusername/Oberoi-Realty-Valuation.git

Install dependencies

pip install -r requirements.txt

Run

python main.py

The generated report will be available in report/Final_Report.xlsx

---

# Future Improvements

- Monte Carlo DCF Simulation
- Relative Valuation (P/E, EV/EBITDA)
- Sensitivity Analysis
- Streamlit Dashboard
- Portfolio Comparison
- Peer Company Analysis
- LSTM-based Price Prediction
- Interactive Visualizations

---