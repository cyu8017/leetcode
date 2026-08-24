# LeetCode 2620 - Counter
# https://leetcode.com/problems/counter/

from typing import Callable


class Solution:
    def createCounter(self, n: int) -> Callable[[], int]:
        def counter() -> int:
            nonlocal n
            v = n
            n += 1
            return v

        return counter
