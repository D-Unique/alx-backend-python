#!/usr/bin/env python3
import random
import asyncio
"""This module contains a coroutine function that takes a random number """


async def wait_random(max_delay=10):
    """this is an async function"""
    await asyncio.sleep(random.uniform(0, max_delay))
    num = random.uniform(0, max_delay)
    return num
