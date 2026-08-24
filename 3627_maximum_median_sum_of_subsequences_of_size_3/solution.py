# LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n // 3, n, 2):
            ans += nums[i]
        return ans
