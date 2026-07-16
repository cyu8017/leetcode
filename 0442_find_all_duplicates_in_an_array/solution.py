# LeetCode 0442 - Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result: list[int] = []
        for number in nums:
            index = abs(number) - 1
            if nums[index] < 0:
                result.append(abs(number))
            else:
                nums[index] = -nums[index]
        return result
