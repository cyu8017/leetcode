# LeetCode 2870 - Minimum Number of Operations to Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
        ans = 0
        for c in freq.values():
            if c == 1:
                return -1
            ans += (c + 2) // 3
        return ans
