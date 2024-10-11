#!/usr/bin/env python3
"""new module imitated from variable annotaion"""


from typing import List
def sum_list(input_list: List[float]) -> float:
    """accpets lists of float and returns their sum
        Args:
            input_list: accpets list of floats
        returns: their sum as a float
    """
    their_sum: float = 0.0
    for i in input_list:
        their_sum += i
    return their_sum
