#!/usr/bin/env python3
""" A module that provides a function takes an integer and returns
asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """it takes and integer and returns asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
