#!/usr/bin/env python3

""" Script testing the basics of asyncio """
import random
import asyncio


async def wait_random(j: int = 10) -> int:
    """
        Function that takes an integer gets random
        waits asynchoronusly

        Args:
            :param @j [int] - First argument in the function

        Return:
            This function returns an integer
    """
    num = random.uniform(0, j)
    await asyncio.sleep(num)
    return num
