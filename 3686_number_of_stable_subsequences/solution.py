# LeetCode 3686 - Number of Stable Subsequences
# https://leetcode.com/problems/number-of-stable-subsequences/

from typing import List


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 1000000007
        a1 = a2 = b1 = b2 = 0
        for x in nums:
            if x % 2 == 1:
                na1 = (1 + b1 + b2) % MOD
                na2 = a1
                a1 = (a1 + na1) % MOD
                a2 = (a2 + na2) % MOD
            else:
                nb1 = (1 + a1 + a2) % MOD
                nb2 = b1
                b1 = (b1 + nb1) % MOD
                b2 = (b2 + nb2) % MOD
        return (((a1 + a2) % MOD + b1) % MOD + b2) % MOD
