# LeetCode 0080 - Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1

        return write
