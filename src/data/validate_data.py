"""Basic data validation helpers."""
import pandas as pd


def summarize_dataframe(df: pd.DataFrame) -> dict:
    """Return basic shape, duplicate, and missingness information."""
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "duplicate_rows": int(df.duplicated().sum()),
        "total_missing_cells": int(df.isna().sum().sum()),
        "memory_mb": round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2),
    }


def column_profile(df: pd.DataFrame) -> pd.DataFrame:
    """Create a compact per-column profile."""
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2),
        "unique_count": df.nunique(dropna=True),
    }).sort_values("missing_pct", ascending=False)
