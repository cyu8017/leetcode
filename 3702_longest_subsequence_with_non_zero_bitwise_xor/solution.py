# LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xorv = 0
        cnt0 = 0
        for x in nums:
            xorv ^= x
            if x == 0:
                cnt0 += 1
        n = len(nums)
        if xorv != 0:
            return n
        if cnt0 == n:
            return 0
        return n - 1
