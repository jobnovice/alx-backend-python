#!/usr/bin/env python3
"""Asynchronus comprehension defined"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Async Generator that generates random number b/n 1and10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
