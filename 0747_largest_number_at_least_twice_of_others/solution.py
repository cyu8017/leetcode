# LeetCode 0747 - Largest Number At Least Twice of Others
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = second = -1
        index = -1
        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                index = i
            elif num > second:
                second = num
        return index if first >= 2 * second else -1
