#!/usr/bin/env python3
"""This script define an asynchronous coroutine that waits for a random
delay between 0 and max_delay seconds and eventually returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait it execution for waits for a random delay between 0 and
    max_delay second and return
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
