from src.data.validate_data import summarize_dataframe
import pandas as pd


def test_summarize_dataframe():
    df = pd.DataFrame({"a": [1, 2, 2], "b": [None, "x", "x"]})
    result = summarize_dataframe(df)
    assert result["rows"] == 3
    assert result["columns"] == 2
    assert result["duplicate_rows"] == 1
    assert result["total_missing_cells"] == 1
