# LeetCode 2666 - Allow One Function Call
# https://leetcode.com/problems/allow-one-function-call/

from typing import Any, Callable


class Solution:
    def once(self, fn: Callable) -> Callable:
        called = False
        res = None

        def wrapper(*args: Any) -> Any:
            nonlocal called, res
            if called:
                return None
            called = True
            res = fn(*args)
            return res

        return wrapper
