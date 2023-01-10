#!/usr/bin/env python3
""" Script that run time for four parallel comprehensions """
import asyncio
from time import perf_counter
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        Function tha measures the time taken to run four parallel
        comprehension

        Return:
            This function returns the time taken in seconds as floats
    """
    start = perf_counter()
    coroutines = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coroutines)
    return perf_counter() - start
