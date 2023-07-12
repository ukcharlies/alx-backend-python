#!/usr/bin/env python3
"""Measure the runtime."""
from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function to measure the run

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): max delay

    Returns:
        float: the run time
    """
    startHere = time()
    run(wait_n(n, max_delay))
    return (time() - startHere) / n
