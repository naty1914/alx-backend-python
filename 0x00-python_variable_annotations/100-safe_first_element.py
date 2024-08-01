#!/usr/bin/env python3
""" A module that provides a function that returns an element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ It returns an element"""
    if lst:
        return lst[0]
    else:
        return None
