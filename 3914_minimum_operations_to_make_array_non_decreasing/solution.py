# LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
# https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            ans += max(0, nums[i - 1] - nums[i])
        return ans
