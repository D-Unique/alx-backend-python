#!/usr/bin/env python3
"""This module contains a function that return a union of Any and a typevar"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """this function a union of Any and a typevar"""
    if key in dct:
        return dct[key]
    else:
        return default
