# LeetCode 2256 - Minimum Average Difference
# https://leetcode.com/problems/minimum-average-difference/

from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left = 0
        best_diff = float("inf")
        best_idx = 0
        for i in range(n):
            left += nums[i]
            left_avg = left // (i + 1)
            right_avg = 0
            if i != n - 1:
                right_avg = (total - left) // (n - i - 1)
            diff = abs(left_avg - right_avg)
            if diff < best_diff:
                best_diff = diff
                best_idx = i
        return best_idx
