# LeetCode 2874 - Maximum Value of an Ordered Triplet II
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_i = 0
        max_diff = 0
        for v in nums:
            if max_diff * v > ans:
                ans = max_diff * v
            if max_i - v > max_diff:
                max_diff = max_i - v
            if v > max_i:
                max_i = v
        return ans
