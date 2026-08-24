# LeetCode 3681 - Maximum XOR of Subsequences
# https://leetcode.com/problems/maximum-xor-of-subsequences/

from typing import List


class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0] * 32
        for x in nums:
            cur = x
            for b in range(31, -1, -1):
                if (cur & (1 << b)) == 0:
                    continue
                if basis[b] == 0:
                    basis[b] = cur
                    break
                cur ^= basis[b]
        ans = 0
        for b in range(31, -1, -1):
            if (ans ^ basis[b]) > ans:
                ans ^= basis[b]
        return ans
