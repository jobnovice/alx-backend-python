#!/usr/bin/envpython3
"""Write a function use the regular functiosyntax to do this)"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task for wait_random."""
    return asyncio.create_task(wait_random(max_delay))
