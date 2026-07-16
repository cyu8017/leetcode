# LeetCode 0163 - Missing Ranges
# https://leetcode.com/problems/missing-ranges/

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result: list[list[int]] = []
        prev = lower - 1
        for num in nums + [upper + 1]:
            if num - prev >= 2:
                result.append([prev + 1, num - 1])
            prev = num
        return result
