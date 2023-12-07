#!/usr/bin/env python3

'''
    Variable Annotations
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns elements lengths '''
    return [(i, len(i)) for i in lst]
