#!/usr/bin/env python3

'''
    Variable Annotations
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Returns a float multiplier function '''
    return lambda value: value * multiplier
