"""Utilities for discovering and loading the Divar dataset."""
from pathlib import Path
import pandas as pd


def find_csv_files(input_dir: str | Path) -> list[Path]:
    """Return CSV files under input_dir recursively."""
    directory = Path(input_dir)
    if not directory.exists():
        raise FileNotFoundError(f"Input directory does not exist: {directory}")
    return sorted(directory.rglob("*.csv"))


def load_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a CSV file without silently changing its source file."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    return pd.read_csv(path, **kwargs)
