# LeetCode 2632 - Curry
# https://leetcode.com/problems/curry/

from typing import Any, Callable


class Solution:
    def curry(self, fn: Callable) -> Callable:
        arity = fn.__code__.co_argcount

        def curried(*args: Any):
            if len(args) >= arity:
                return fn(*args)

            def nxt(*next_args: Any):
                return curried(*args, *next_args)

            return nxt

        return curried
