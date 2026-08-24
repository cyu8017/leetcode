# LeetCode 3247 - Number of Subsequences with Odd Sum
# https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

from typing import List


class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        mod = 1000000007
        f = [0, 0]
        for x in nums:
            g = [0, 0]
            if x % 2 == 1:
                g[0] = (f[0] + f[1]) % mod
                g[1] = (f[0] + f[1] + 1) % mod
            else:
                g[0] = (f[0] + f[0] + 1) % mod
                g[1] = (f[1] + f[1]) % mod
            f = g
        return f[1]
