#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Sequence, Union, Any, Iterable


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """annotated the function to accept any sequence"""
    if lst:
        return lst[0]
    else:
        return None
