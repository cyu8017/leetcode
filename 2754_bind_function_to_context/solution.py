# LeetCode 2754 - Bind Function to Context
# https://leetcode.com/problems/bind-function-to-context/

from typing import Any, Callable


class Solution:
    def bindPolyfill(self, fn: Callable, obj: Any) -> Callable:
        def bound(*args):
            try:
                return fn.__get__(obj, type(obj))(*args)
            except Exception:
                return fn(*args)

        return bound
