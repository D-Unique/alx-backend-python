#!/usr/bin/env python3
"""
This module contains a fuction that returns a values
with the appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """this function returns a list"""
    return [(i, len(i)) for i in lst]
