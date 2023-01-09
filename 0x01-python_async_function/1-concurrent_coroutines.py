#!/usr/bin/env python3
""" Script that executes multiple coroutines at the same time with async """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Function that calculates the time taken to finidh a particular
        coroutine

        Args:
            :param @n - the first argument and the number of times
            to loop over wait_random
            :param @max_delay - The second argument and the time to
            delay the function

        Return:
            Function returns a list of floats
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
