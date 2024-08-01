#!/usr/bin/env python3
""" A module that provides a function that returns a function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """It returns a function that multiplies a float by multiplier"""
    def multiplier_f(number: float) -> float:
        """It multiplies a float by multiplier"""
        return number * multiplier
    return multiplier_f
