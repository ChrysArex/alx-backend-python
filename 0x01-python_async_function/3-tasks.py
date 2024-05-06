#!/usr/bin/env python3
"""Define a function that create an asyncio.Task"""


import asyncio
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """returns a asyncio.Task."""
    return asyncio.ensure_future(wait_random(max_delay))
