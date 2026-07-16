# LeetCode 0128 - Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        best = 0
        for num in values:
            if num - 1 in values:
                continue
            length = 1
            while num + length in values:
                length += 1
            best = max(best, length)
        return best
