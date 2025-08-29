import pandas as pd
from app.utils.parse_helpers import parse_date, parse_dict


def _transform_dict_columns(chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Parses specified columns in the DataFrame chunk as dictionaries using parse_dict.
    Args:
        chunk (pd.DataFrame): DataFrame containing columns to transform.
    Returns:
        pd.DataFrame: DataFrame with parsed dictionary columns.
    """
    dict_columns = [
        "genres",
        "keywords",
        "production_companies",
        "production_countries",
        "spoken_languages",
    ]
    for col in dict_columns:
        if col in chunk.columns:
            chunk[col] = chunk[col].apply(parse_dict)
    return chunk


def _transform_release_date(chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Parses the 'release_date' column in the DataFrame chunk into datetime objects using parse_date.
    Args:
        chunk (pd.DataFrame): DataFrame containing the 'release_date' column.
    Returns:
        pd.DataFrame: DataFrame with parsed release dates.
    """
    if "release_date" in chunk.columns:
        chunk["release_date"] = chunk["release_date"].apply(parse_date)
    return chunk


def transform_movies(chunk: pd.DataFrame) -> pd.DataFrame:
    """
    Applies a series of transformations to the movies DataFrame chunk.
    Transforms dictionary columns and release date column using helper functions.
    Args:
        chunk (pd.DataFrame): DataFrame to transform.
    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    for func in [
        _transform_dict_columns,
        _transform_release_date
    ]:
        chunk = func(chunk)
    return chunk
