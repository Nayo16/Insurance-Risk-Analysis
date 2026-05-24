import pandas as pd
from pathlib import Path


def load_insurance_data(path: str | Path = "data/insurance_data.csv") -> pd.DataFrame:
    """Load the insurance dataset with sensible dtypes and parsing.

    Parameters
    ----------
    path: str or Path
        Path to CSV file
    """
    p = Path(path)
    df = pd.read_csv(p, sep='\t', parse_dates=["TransactionDate"])

    # basic dtype fixes
    numeric_cols = [
        "TotalPremium",
        "TotalClaims",
        "CustomValueEstimate",
        "ClaimAmount",
        "AnnualPremium",
        "Deductible",
        "AnnualIncome",
        "RiskScore",
        "Age",
        "NCD",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "Claimed" in df.columns:
        df["Claimed"] = (
            df["Claimed"].astype(str)
            .str.strip()
            .str.upper()
            .map({"TRUE": True, "FALSE": False})
            .fillna(df["Claimed"])
        )

    return df
