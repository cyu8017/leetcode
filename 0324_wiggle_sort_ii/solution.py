# LeetCode 0324 - Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        sorted_nums = sorted(nums)
        left = (len(nums) - 1) // 2
        right = len(nums) - 1
        for index in range(len(nums)):
            if index % 2 == 0:
                nums[index] = sorted_nums[left]
                left -= 1
            else:
                nums[index] = sorted_nums[right]
                right -= 1
