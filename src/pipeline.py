from __future__ import annotations
import pandas as pd
from pathlib import Path

def load(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["signup_date"])
    return df

def featureize(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["tenure_days"] = (pd.Timestamp.today().normalize() - df["signup_date"]).dt.days
    df["assist_per_hour"] = (df["monthly_ai_assist_calls"] / (df["monthly_usage_hours"].replace(0, 1))).round(2)
    return df

def simple_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["value_score"] = (df["monthly_usage_hours"] * 0.6 + df["monthly_ai_assist_calls"] * 0.4).round(1)
    return df
