# LeetCode 2572 - Count the Number of Square-Free Subsets
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/

from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 1000000007
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        def mask_of(x: int) -> int:
            mask = 0
            for i, p in enumerate(PRIMES):
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                    if cnt > 1:
                        return -1
                if cnt == 1:
                    mask |= 1 << i
            return mask

        dp = [0] * (1 << 10)
        dp[0] = 1
        for x, c in freq.items():
            if x == 1:
                continue
            m = mask_of(x)
            if m < 0:
                continue
            for state in range((1 << 10) - 1, -1, -1):
                if (state & m) == 0:
                    dp[state | m] = (dp[state | m] + dp[state] * c) % MOD
        ans = 0
        for v in dp:
            ans = (ans + v) % MOD
        ones = freq.get(1, 0)
        mul = 1
        for _ in range(ones):
            mul = mul * 2 % MOD
        ans = ans * mul % MOD
        ans = (ans - 1 + MOD) % MOD
        return ans
