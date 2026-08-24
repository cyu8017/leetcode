# LeetCode 2708 - Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/

from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        prod, used, i = 1, False, 0
        while i + 1 < n and nums[i] < 0 and nums[i + 1] < 0:
            prod *= nums[i] * nums[i + 1]
            used = True
            i += 2
        neg_left = i < n and nums[i] < 0
        while i < n:
            if nums[i] > 0:
                prod *= nums[i]
                used = True
            i += 1
        if not used:
            if neg_left:
                for x in nums:
                    if x == 0:
                        return 0
                return nums[n - 1]
            return 0
        return prod
