import ast
import json
import pandas as pd
from dateutil import parser
from datetime import datetime


def parse_dict(value: str) -> dict | None:
    if not isinstance(value, str) or not value.strip():
        return None

    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return None


def parse_list(value: str) -> list[str] | None:
    if not isinstance(value, str) or not value.strip():
        return None

    return [item.strip() for item in value.split(",") if item.strip()]


def parse_date(value: str) -> datetime | None:
    if pd.isna(value):
        return None
    
    strvalue = str(value).strip()
    if not strvalue:
        return None
    
    try:
        return parser.parse(strvalue, fuzzy=True)
    except (ValueError, OverflowError, TypeError):
        return None
    
    
def parse_json(value: str) -> dict | list | None:
    if not isinstance(value, str) or not value.strip():
        return None
    
    try:
        return json.loads(value)
    except (TypeError, ValueError, json.JSONDecodeError):
        return None