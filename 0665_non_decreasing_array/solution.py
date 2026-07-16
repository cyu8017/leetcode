# LeetCode 0665 - Non-decreasing Array
# https://leetcode.com/problems/non-decreasing-array/

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            if changed:
                return False
            changed = True
            if i >= 2 and nums[i] < nums[i - 2]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]
        return True
