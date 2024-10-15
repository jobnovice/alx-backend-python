#!/usr/bin/env python3
"""0-basic_async_syntax.py the basics of Async"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """minimalstic implementaion of concurrency"""
    start_time = time.time()
    await asyncio.sleep(random.uniform(0, max_delay))
    end_time = time.time()
    duration = end_time - start_time
    return duration
