#!/usr/bin/env python3
"""
This module contains a function that takes unknown
type and return unknown type
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function return type Optional"""
    if lst:
        return lst[0]
    else:
        return None
