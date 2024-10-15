#!/usr/bin/env python3
import random
import asyncio
"""This module contains a coroutine function that takes a random number """
wait_random = __import__('0-basic_async_syntax').wait_random
async def wait_n(n: int, max_delay: int) -> 

 You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.
async def wait_random(max_delay=10):
    """this is an async function"""
    await asyncio.sleep(random.uniform(0, max_delay))
    num = random.uniform(0, max_delay)
    return num
