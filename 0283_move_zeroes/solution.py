# LeetCode 0283 - Move Zeroes
# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        for index in range(insert, len(nums)):
            nums[index] = 0
