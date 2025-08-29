import ast
import json
import pandas as pd
from dateutil import parser
from datetime import datetime


def parse_dict(value: str) -> dict | None:
    """
    Safely parses a string representation of a dictionary into a Python dict.
    Returns None if parsing fails or input is not a valid string.
    Args:
        value (str): String to parse.
    Returns:
        dict | None: Parsed dictionary or None if invalid.
    """
    if not isinstance(value, str) or not value.strip():
        return None

    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return None


def parse_list(value: str) -> list[str] | None:
    """
    Parses a comma-separated string into a list of strings.
    Returns None if input is not a valid string.
    Args:
        value (str): Comma-separated string.
    Returns:
        list[str] | None: List of strings or None if invalid.
    """
    if not isinstance(value, str) or not value.strip():
        return None

    return [item.strip() for item in value.split(",") if item.strip()]


def parse_date(value: str) -> datetime | None:
    """
    Parses a string into a datetime object using dateutil.parser.
    Returns None if parsing fails or input is empty/NaN.
    Args:
        value (str): String to parse as date.
    Returns:
        datetime | None: Parsed datetime or None if invalid.
    """
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
    """
    Parses a JSON string into a Python dict or list.
    Returns None if parsing fails or input is not a valid string.
    Args:
        value (str): JSON string to parse.
    Returns:
        dict | list | None: Parsed object or None if invalid.
    """
    if not isinstance(value, str) or not value.strip():
        return None
    
    try:
        return json.loads(value)
    except (TypeError, ValueError, json.JSONDecodeError):
        return None