# LeetCode 0414 - Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None

        for value in nums:
            if value == first or value == second or value == third:
                continue
            if first is None or value > first:
                third, second, first = second, first, value
            elif second is None or value > second:
                third, second = second, value
            elif third is None or value > third:
                third = value

        return third if third is not None else first
