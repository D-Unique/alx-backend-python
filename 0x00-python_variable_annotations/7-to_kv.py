#!/usr/bin/env python3
""" This module contains a funtion that a"""
from typing import Union, Tuple


def to_kv(k:str, v: Union[int,float] ) -> Tuple[str,float]:
    """this function returns a tuple of str and float"""

    return (k, v**2)





