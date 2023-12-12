#!/usr/bin/env python3

'''
    Async Comprehension
'''


from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
        Asyncronosly generates random numbers
    '''

    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
