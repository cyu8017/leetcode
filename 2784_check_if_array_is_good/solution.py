# LeetCode 2784 - Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1:
            return False
        freq = [0] * (n + 1)
        for v in nums:
            if v < 1 or v > n:
                return False
            freq[v] += 1
        for i in range(1, n):
            if freq[i] != 1:
                return False
        return freq[n] == 2
