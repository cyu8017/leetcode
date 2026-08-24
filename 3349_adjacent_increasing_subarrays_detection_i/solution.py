# LeetCode 3349 - Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

from typing import List


def inc(nums: List[int], start: int, k: int) -> bool:
    for i in range(start, start + k - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            if inc(nums, i, k) and inc(nums, i + k, k):
                return True
        return False
