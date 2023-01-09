#!/usr/bin/env python3
""" Script testing the basics of asyncio """


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        Function that takes an integer gets random
        waits asynchoronusly

        Args:
            :param @j [int] - First argument in the function
            and the max delay to return.

        Return:
            This function returns an integer
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
