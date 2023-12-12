#!/usr/bin/env python3

'''
    Async Comprehension
'''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        Asyncronosly generates a list of random numbers
    '''

    return [r async for r in async_generator()]
