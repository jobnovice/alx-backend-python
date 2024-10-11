#!/usr/bin/env python3
"""complex types and mixed lists are going to be covered in this module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """union annotates the function accepts both types"""
    ttsum: float = 0.0
    for x in mxd_lst:
        ttsum += x
    return ttsum
