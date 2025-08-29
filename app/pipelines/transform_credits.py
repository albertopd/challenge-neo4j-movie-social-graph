import pandas as pd
from app.utils.parse_helpers import parse_json


def _transform_json_columns(chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Parses JSON columns ('cast', 'crew') in the given DataFrame chunk using parse_json.
    Args:
        chunk (pd.DataFrame): DataFrame containing columns to transform.
    Returns:
        pd.DataFrame: DataFrame with parsed JSON columns.
    """
    json_columns = [
        "cast",
        "crew"
    ]

    for col in json_columns:
        if col in chunk.columns:
            chunk[col] = chunk[col].apply(parse_json)
    return chunk


def transform_credits(chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Applies a series of transformations to the credits DataFrame chunk.
    Currently transforms JSON columns using helper functions.
    Args:
        chunk (pd.DataFrame): DataFrame to transform.
    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    for func in [
        _transform_json_columns
    ]:
        chunk = func(chunk)
    return chunk
