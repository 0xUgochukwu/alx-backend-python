#!/usr/bin/env python3

'''
    Async
'''


from asyncio import as_completed
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
        spawns multiple tasks and returns them
    '''

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in as_completed(tasks)]
