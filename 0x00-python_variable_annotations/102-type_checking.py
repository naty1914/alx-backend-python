#!/usr/bin/env python3
""" A module that provides a function that returns a list"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """It returns a list with each elements of input
       tuple multiplied by factor
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
