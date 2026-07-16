# LeetCode 0805 - Split Array With Same Average
# https://leetcode.com/problems/split-array-with-same-average/

from functools import lru_cache
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        nums.sort()

        @lru_cache(None)
        def find(target: int, count: int, index: int) -> bool:
            if count == 0:
                return target == 0
            if index == n or count + index > n or target < 0:
                return False
            return find(target - nums[index], count - 1, index + 1) or find(
                target, count, index + 1
            )

        for size in range(1, n):
            if total * size % n == 0 and find(total * size // n, size, 0):
                return True
        return False
