# LeetCode 2757 - Generate Circular Array Values
# https://leetcode.com/problems/generate-circular-array-values/

from typing import Any, Generator, List, Optional


class Solution:
    def cycleGenerator(
        self, arr: List[Any], startIndex: int
    ) -> Generator[Any, Optional[int], None]:
        i = startIndex
        jump = yield arr[i]
        while True:
            n = len(arr)
            i = ((i + (jump or 0)) % n + n) % n
            jump = yield arr[i]
