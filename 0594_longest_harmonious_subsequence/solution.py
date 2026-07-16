# LeetCode 0594 - Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 0
        for value, count in counts.items():
            if value + 1 in counts:
                best = max(best, count + counts[value + 1])
        return best
