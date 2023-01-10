#!/usr/bin/env python3
""" Script that visualizes the async comprehension """
import asyncio
import random
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[int]:
	"""
		Function that generates 10 different numbers using async comprehension
		over async generation

		Return:
			This function returns a list of integers
	"""
	return [i async for i in async_generator()]