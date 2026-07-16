from functools import cache
from math import gcd
class Solution:
    def maxScore(self, nums):
        n = len(nums)
        @cache
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
            step = mask.bit_count() // 2 + 1
            best = 0
            for i in range(n):
                if mask >> i & 1:
                    continue
                for j in range(i + 1, n):
                    if mask >> j & 1:
                        continue
                    best = max(
                        best,
                        step * gcd(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j)),
                    )
            return best
        return dp(0)
