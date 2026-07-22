import pandas as pd
from config import *

info = pd.read_csv(RAW_DATA / "Company_Info.csv")

print(
    info[info["Field"].str.contains("share", case=False, na=False)]
)