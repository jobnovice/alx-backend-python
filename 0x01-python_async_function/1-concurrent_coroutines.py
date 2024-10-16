#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines concurrently and returns a sorted list
    of delays."""
    new_list = []

    # Spawn n wait_random coroutines and await their results
    for _ in range(n):
        delay = await wait_random(max_delay)
        new_list.append(delay)

    # Implement Bubble Sort to sort new_list in ascending order
    k = len(new_list)
    for i in range(k):
        for j in range(0, k - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

    return new_list
