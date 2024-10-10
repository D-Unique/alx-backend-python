#!/usr/bin/env python3
""" this module contains a function that accepts a list
 mxd_lst of integers and floats returns a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """this function return a sum of type float"""
    return sum(mxd_lst)
