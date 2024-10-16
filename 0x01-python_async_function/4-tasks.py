#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines concurrently and returns"""
    # Spawn n wait_random coroutines and collect the tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Await all the tasks and gather their results
    results = await asyncio.gather(*tasks)

    # Sort the results (delays) in ascending order
    return sorted(results)
