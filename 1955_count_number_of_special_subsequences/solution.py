from typing import List

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        a = b = c = 0
        for x in nums:
            if x == 0:
                a = (a * 2 + 1) % MOD
            elif x == 1:
                b = (b * 2 + a) % MOD
            else:
                c = (c * 2 + b) % MOD
        return c
