#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs async_comprehension four times in parallel and returns
    the execution time"""
    start_time = time.time()

    # Run four async comprehensions in parallel using asyncio.gather
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()  # Correct the call here
    return end_time - start_time
