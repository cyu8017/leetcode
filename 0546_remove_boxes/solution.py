# LeetCode 0546 - Remove Boxes
# https://leetcode.com/problems/remove-boxes/

from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(left: int, right: int, streak: int) -> int:
            if left > right:
                return 0
            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                streak += 1

            best = (streak + 1) ** 2 + dp(left, right - 1, 0)
            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    best = max(best, dp(left, i, streak + 1) + dp(i + 1, right - 1, 0))
            return best

        return dp(0, len(boxes) - 1, 0)
