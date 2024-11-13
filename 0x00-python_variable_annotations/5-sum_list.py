#!/usr/bin/env python3
""" annotation module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns list sum as a float
    """
    total: float = 0
    for i in input_list:
        total += i
    return total
