#!/usr/bin/env python3
"""A module that provides a function that measures the runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """It measures the runtime"""
    tasks = [async_comprehension() for i in range(3)]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
