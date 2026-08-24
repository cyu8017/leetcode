# LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
# https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

import asyncio
from typing import Callable, List


class Solution:
    def promiseAllSettled(self, functions: List[Callable]):
        async def run_one(fn: Callable):
            try:
                value = fn()
                if hasattr(value, "__await__"):
                    value = await value
                return {"status": "fulfilled", "value": value}
            except Exception as reason:
                return {"status": "rejected", "reason": reason}

        async def run_all():
            return await asyncio.gather(*(run_one(fn) for fn in functions))

        return run_all()
