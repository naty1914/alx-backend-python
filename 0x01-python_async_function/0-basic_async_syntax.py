#!/usr/bin/env python3
""" A module that that provides a function that takes an integer and
returns a float"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """It waits for a random amount of time"""
    wait_random = random.uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return wait_random
