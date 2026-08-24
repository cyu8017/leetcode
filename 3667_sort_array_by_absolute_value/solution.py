# LeetCode 3667 - Sort Array By Absolute Value
# https://leetcode.com/problems/sort-array-by-absolute-value/

from typing import List


class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        nums.sort(key=abs)
        return nums
