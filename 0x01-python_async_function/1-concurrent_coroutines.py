#!/usr/bin/env python3
"""This script  execute multiple coroutines at the same time with async"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    res = [wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(res)
    return [task.result() for task in completed_tasks]
