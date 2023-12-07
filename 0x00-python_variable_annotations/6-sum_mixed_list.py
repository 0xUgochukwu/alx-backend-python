#!/usr/bin/env python3

'''
    Variable Annotations
'''

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Sums up a list of floats & integers '''
    return float(sum(mxd_lst))
