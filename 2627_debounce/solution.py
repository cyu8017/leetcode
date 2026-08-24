# LeetCode 2627 - Debounce
# https://leetcode.com/problems/debounce/

from typing import Any, Callable, List


class Solution:
    def debounce(self, fn: Callable, t: int) -> Callable:
        timer = {"id": None}

        def wrapped(*args: Any) -> Any:
            timer["id"] = {"args": args, "t": t}
            return fn(*args)

        return wrapped
