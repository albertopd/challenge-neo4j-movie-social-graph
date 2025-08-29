import pandas as pd
from app.utils.parse_helpers import parse_date, parse_dict


def _transform_dict_columns(chunk: pd.DataFrame) -> pd.DataFrame:
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
    if "release_date" in chunk.columns:
        chunk["release_date"] = chunk["release_date"].apply(parse_date)
    return chunk


def transform_movies(chunk: pd.DataFrame) -> pd.DataFrame:
    for func in [
        _transform_dict_columns,
        _transform_release_date
    ]:
        chunk = func(chunk)
    return chunk
