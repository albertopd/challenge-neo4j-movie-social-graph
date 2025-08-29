import pandas as pd
from app.utils.parse_helpers import parse_json


def _transform_json_columns(chunk: pd.DataFrame) -> pd.DataFrame:
    json_columns = [
        "cast",
        "crew"
    ]

    for col in json_columns:
        if col in chunk.columns:
            chunk[col] = chunk[col].apply(parse_json)
    return chunk


def transform_credits(chunk: pd.DataFrame) -> pd.DataFrame:
    for func in [
        _transform_json_columns
    ]:
        chunk = func(chunk)
    return chunk
