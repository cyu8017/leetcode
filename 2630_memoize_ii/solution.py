# LeetCode 2630 - Memoize II
# https://leetcode.com/problems/memoize-ii/

from typing import Any, Callable


class Solution:
    def memoize(self, fn: Callable) -> Callable:
        root = {}
        RES = object()

        def wrapped(*args: Any) -> Any:
            node = root
            for a in args:
                if a not in node:
                    node[a] = {}
                node = node[a]
            if RES in node:
                return node[RES]
            v = fn(*args)
            node[RES] = v
            return v

        return wrapped
