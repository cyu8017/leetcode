# LeetCode 2636 - Promise Pool
# https://leetcode.com/problems/promise-pool/

from typing import Callable, List


class Solution:
    def promisePool(self, functions: List[Callable], n: int = 1):
        i = 0

        def worker() -> None:
            nonlocal i
            while i < len(functions):
                cur = i
                i += 1
                functions[cur]()

        limit = min(n, len(functions))
        for _ in range(limit):
            worker()
        return None
