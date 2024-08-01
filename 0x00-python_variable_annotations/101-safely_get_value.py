#!/usr/bin/env python3
""" A module  returns  a value  safely from mapping"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ It returns safely a value from mapping"""
    if key in dct:
        return dct[key]
    else:
        return default
