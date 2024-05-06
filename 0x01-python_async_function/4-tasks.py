#!/usr/bin/env python3
"""Modify the wait_n function"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    res = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(res)
    return [task.result() for task in completed_tasks]
