# LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            x, s = num, 0
            while x > 0:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1
