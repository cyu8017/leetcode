# LeetCode 2856 - Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/

from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        mx = 0
        for v in nums:
            c = freq.get(v, 0) + 1
            freq[v] = c
            if c > mx:
                mx = c
        if mx <= n // 2:
            return n % 2
        return 2 * mx - n
