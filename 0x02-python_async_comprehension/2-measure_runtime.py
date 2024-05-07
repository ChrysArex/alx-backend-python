#!/usr/bin/env python3
"""Define the measure_runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime of executing four time async_comprehension
    and return the value"""
    s = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    mes = time.perf_counter() - s
    return mes
