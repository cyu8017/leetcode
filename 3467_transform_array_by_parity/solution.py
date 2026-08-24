# LeetCode 3467 - Transform Array by Parity
# https://leetcode.com/problems/transform-array-by-parity/

from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] %= 2
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
