# LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1
        seen = set(nums)
        while total in seen:
            total += 1
        return total
