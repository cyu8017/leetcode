# LeetCode 2859 - Sum of Values at Indices With K Set Bits
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, val in enumerate(nums):
            x, bits = i, 0
            while x:
                bits += x & 1
                x >>= 1
            if bits == k:
                ans += val
        return ans
