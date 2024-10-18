#!/usr/bin/env python3
"""This module contains a coroutine function that takes a random number """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ this is a asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) and waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
