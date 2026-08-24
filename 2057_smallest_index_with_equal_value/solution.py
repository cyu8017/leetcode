# LeetCode 2057 - Smallest Index With Equal Value
# https://leetcode.com/problems/smallest-index-with-equal-value/

from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if i % 10 == v:
                return i
        return -1
