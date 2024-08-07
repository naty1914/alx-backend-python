#!/usr/bin/env python3
"""A module that provides an async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """It returns numbers using async comprehension"""
    n = [n async for n in async_generator()]
    return n
