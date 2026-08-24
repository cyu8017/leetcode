# LeetCode 2821 - Delay the Resolution of Each Promise
# https://leetcode.com/problems/delay-the-resolution-of-each-promise/

import asyncio
from typing import Callable, List


class Solution:
    def delayAll(self, functions: List[Callable], ms: int) -> List[Callable]:
        def wrap(fn: Callable) -> Callable:
            async def delayed():
                try:
                    result = fn()
                    if hasattr(result, "__await__"):
                        result = await result
                    await asyncio.sleep(ms / 1000.0)
                    return result
                except Exception:
                    await asyncio.sleep(ms / 1000.0)
                    raise

            return delayed

        return [wrap(fn) for fn in functions]
