# LeetCode 2665 - Counter II
# https://leetcode.com/problems/counter-ii/

from typing import Callable, Dict


class Solution:
    def createCounter(self, init: int) -> Dict[str, Callable[[], int]]:
        cur = init

        def increment() -> int:
            nonlocal cur
            cur += 1
            return cur

        def decrement() -> int:
            nonlocal cur
            cur -= 1
            return cur

        def reset() -> int:
            nonlocal cur
            cur = init
            return cur

        return {"increment": increment, "decrement": decrement, "reset": reset}
