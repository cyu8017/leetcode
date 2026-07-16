# LeetCode 0448 - Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for number in nums:
            index = abs(number) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [index + 1 for index, value in enumerate(nums) if value > 0]
