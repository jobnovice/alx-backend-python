#!/usr/bin/env python3
"""TypeVar is know going to be immplemenated"""

from typing import TypeVar, Dict

T = TypeVar('T')


def safely_get_value(dct: Mapping[str, T], key: str,
                     default: Optional[T] = None) -> Optional[T]:
    """function annotated using TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
