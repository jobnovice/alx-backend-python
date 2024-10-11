#!/usr/bin/env python3
"""annotation example number seven depicted"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns the string alongside with square of whatever was sent for
    us"""
    to_tup: Tuple[str, float] = (k, v*v)
    return to_tup
