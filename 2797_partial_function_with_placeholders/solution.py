# LeetCode 2797 - Partial Function with Placeholders
# https://leetcode.com/problems/partial-function-with-placeholders/

from typing import Any, Callable, List


class Solution:
    def partial(self, fn: Callable, args: List[Any]) -> Callable:
        def wrapped(*rest_args):
            full = []
            ri = 0
            for a in args:
                if a == "_":
                    if ri < len(rest_args):
                        full.append(rest_args[ri])
                        ri += 1
                else:
                    full.append(a)
            while ri < len(rest_args):
                full.append(rest_args[ri])
                ri += 1
            return fn(*full)

        return wrapped
