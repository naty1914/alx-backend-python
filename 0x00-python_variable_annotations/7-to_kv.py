#!/usr/bin/env python3
""" A module that provides a function that returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple"""
    return (k, v**2)
