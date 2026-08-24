# LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        m = n >> 1
        ans = abs(nums[m] - k)
        if nums[m] > k:
            i = m - 1
            while i >= 0 and nums[i] > k:
                ans += nums[i] - k
                i -= 1
        else:
            i = m + 1
            while i < n and nums[i] < k:
                ans += k - nums[i]
                i += 1
        return ans
