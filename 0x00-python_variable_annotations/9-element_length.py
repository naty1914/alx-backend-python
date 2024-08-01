#!/usr/bin/env python3
""" A module that provides a function that returns a tuple"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """It returns a tuple"""
    return [(i, len(i)) for i in lst]
