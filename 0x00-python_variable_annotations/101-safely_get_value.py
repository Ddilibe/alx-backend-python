#!/usr/bin/env python3
""" Script that contains method that safely gets value from dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
        Function that safely gets value from dictionary.
        Args:
            "params @dct - Dictionary to get value from.
            "params @key - Key to get value from.
            "params @default - Default value to return if key is not found.
        Returns:
            Value from dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
