# LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp0 = dp1 = dp2 = 0
        for v in nums:
            cost = k - v if v < k else 0
            nd0 = cost + min(dp0, dp1, dp2)
            dp0, dp1, dp2 = dp1, dp2, nd0
        return min(dp0, dp1, dp2)
