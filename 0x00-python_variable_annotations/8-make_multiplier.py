#!/usr/bin/env python3
"""
This module contains a function that accepts a
float and return a callable
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """this fuction takes float and returns a callable"""
    def callback(m: float) -> float:
        """this function take a float and returns a float"""
        return m * multiplier
    return callback
