#!/usr/bin/env python3 
"""duck type annotation in python"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples
    where each tuple contains the sequence and its length."""
    return [(i, len(i)) for i in lst]
