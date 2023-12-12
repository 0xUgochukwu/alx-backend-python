#!/usr/bin/env python3

'''
    Async Comprehension
'''


from asyncio import gather
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''
        Measures Asynchronous runtime
    '''
    start = time()
    await gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return (end - start)
