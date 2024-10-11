#!/usr/bin/env python3
"""type annotated function to return string after accpeting a float"""


def to_str(n: float) -> str:
    """returns the string represenation of an object
        Args:
            n: a float number
        returns: string
    """
    return n.__str__()
