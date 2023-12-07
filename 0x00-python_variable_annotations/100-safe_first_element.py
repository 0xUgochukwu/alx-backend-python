#!/usr/bin/env python3

'''
    Variable Annotations
'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Return first Element '''
    if lst:
        return lst[0]
    else:
        return None
