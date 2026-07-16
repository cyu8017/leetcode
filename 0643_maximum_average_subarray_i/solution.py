# LeetCode 0643 - Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        best = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            best = max(best, window)
        return best / k
