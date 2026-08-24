# LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for x in nums:
            if x < k:
                ans += 1
        return ans
