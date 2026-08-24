# LeetCode 2295 - Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/

from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {x: i for i, x in enumerate(nums)}
        for a, b in operations:
            i = pos[a]
            nums[i] = b
            del pos[a]
            pos[b] = i
        return nums
