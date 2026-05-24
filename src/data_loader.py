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
    df = pd.read_csv(p, parse_dates=["TransactionMonth"], infer_datetime_format=True)

    # basic dtype fixes
    for col in ["TotalPremium", "TotalClaims", "CustomValueEstimate", "SumInsured"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
