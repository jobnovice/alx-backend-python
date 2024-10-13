#!/usr/bin/env python3
"""TypeVar is know going to be immplemenated"""
from typing import Mapping, Any, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Return dct[key] if key exists, else default."""
    return dct[key] if key in dct else deault
