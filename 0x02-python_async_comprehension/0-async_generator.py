#!/usr/bin/env python3
"""A module that provides an async generator function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """It waits for a random amount of time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
