from pathlib import Path

# -----------------------------
# Project Information
# -----------------------------

TICKER = "OBEROIRLTY.NS"
COMPANY = "Oberoi Realty Ltd"

# -----------------------------
# Data Period
# -----------------------------

PRICE_PERIOD = "5y"
PRICE_INTERVAL = "1d"

# -----------------------------
# Folder Structure
# -----------------------------

BASE_DIR = Path(__file__).parent

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"
EXTERNAL_DATA = BASE_DIR / "data" / "external"

OUTPUT = BASE_DIR / "output"
CHARTS = BASE_DIR / "charts"
REPORT = BASE_DIR / "report"

folders = [
    RAW_DATA,
    PROCESSED_DATA,
    EXTERNAL_DATA,
    OUTPUT,
    CHARTS,
    REPORT
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)