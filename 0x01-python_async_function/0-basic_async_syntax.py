#!/usr/bin/env python3
"The basics of async."
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """first go at async function

    Args:
        max_delay (int, optional): _description_. Defaults to 10.
    """
    TheDelay = random.uniform(0, max_delay)
    await asyncio.sleep(TheDelay)
    return TheDelay