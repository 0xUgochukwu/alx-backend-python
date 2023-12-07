#!/usr/bin/env python3

'''
    Variable Annotations
'''

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    ''' Safely Get a Value '''
    if key in dct:
        return dct[key]
    else:
        return default
