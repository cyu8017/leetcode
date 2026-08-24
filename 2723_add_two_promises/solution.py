# LeetCode 2723 - Add Two Promises
# https://leetcode.com/problems/add-two-promises/

import asyncio
from typing import Any, Awaitable, Union


class Solution:
    async def addTwoPromises(self, promise1: Union[Awaitable, Any], promise2: Union[Awaitable, Any]) -> Any:
        async def resolve(p: Any) -> Any:
            if asyncio.iscoroutine(p) or hasattr(p, "__await__"):
                return await p
            return p

        return (await resolve(promise1)) + (await resolve(promise2))
