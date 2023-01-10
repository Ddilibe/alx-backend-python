#!/usr/bin/env python3
""" Script containing an Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
        Function that yields different numbers at different times
        which is generated randomly.

        Return:
            This function returns an iterator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
