#!/usr/bin/env python3
"""complex type in functions implemenated in here"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """wrote some annotations for the callable  function that we defined"""
    def multiply(value: float) -> float:
        """multiplies the float with the multiplier"""
        return value * multiplier
    return multiply
