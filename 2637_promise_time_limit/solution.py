# LeetCode 2637 - Promise Time Limit
# https://leetcode.com/problems/promise-time-limit/

import time
from typing import Any, Callable


class Solution:
    def timeLimit(self, fn: Callable, t: int) -> Callable:
        def wrapped(*args: Any):
            start = time.time()
            res = fn(*args)
            if (time.time() - start) * 1000 > t:
                raise TimeoutError("Time Limit Exceeded")
            return res

        return wrapped
