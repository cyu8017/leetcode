# LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        for x in nums:
            seen.add(x)
            if x > 0 and -x in seen and x > ans:
                ans = x
            if x < 0 and -x in seen and -x > ans:
                ans = -x
        return ans
