#!/usr/bin/env python3

'''
    Variable Annotations
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Returns KV '''
    return (k, v**2)
