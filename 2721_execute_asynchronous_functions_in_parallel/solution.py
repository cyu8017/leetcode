# LeetCode 2721 - Execute Asynchronous Functions in Parallel
# https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

import asyncio
from typing import Any, Callable, List


class Solution:
    def promiseAll(self, functions: List[Callable]) -> Any:
        async def run() -> List[Any]:
            n = len(functions)
            if n == 0:
                return []
            ans = [None] * n
            done = 0

            async def one(i: int, fn: Callable) -> None:
                nonlocal done
                result = fn()
                if asyncio.iscoroutine(result) or hasattr(result, "__await__"):
                    ans[i] = await result
                else:
                    ans[i] = result
                done += 1

            await asyncio.gather(*(one(i, fn) for i, fn in enumerate(functions)))
            return ans

        return run()
