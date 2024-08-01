#!/usr/bin/env python3
"""A module that provides a function that returns the sum of the list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """It returns the sum of the list as a float"""
    return sum(mxd_lst)
