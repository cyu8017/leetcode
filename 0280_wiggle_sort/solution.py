# LeetCode 0280 - Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for index in range(1, len(nums)):
            if index % 2 == 1 and nums[index] < nums[index - 1]:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
            elif index % 2 == 0 and nums[index] > nums[index - 1]:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
