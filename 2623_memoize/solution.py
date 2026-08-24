# LeetCode 2623 - Memoize
# https://leetcode.com/problems/memoize/

from typing import Any, Callable


class Solution:
    def memoize(self, fn: Callable) -> Callable:
        cache = {}

        def wrapped(x: Any) -> Any:
            if x in cache:
                return cache[x]
            r = fn(x)
            cache[x] = r
            return r

        return wrapped
