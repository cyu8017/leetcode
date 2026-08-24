# LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for x in nums:
            if x > 0:
                pos += 1
            elif x < 0:
                neg += 1
        return max(pos, neg)
