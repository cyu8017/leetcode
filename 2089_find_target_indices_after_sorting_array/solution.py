# LeetCode 2089 - Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = eq = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                eq += 1
        return [less + i for i in range(eq)]
