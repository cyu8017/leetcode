# LeetCode 3336 - Find the Number of Subsequences With Equal GCD
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

from typing import List


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 1000000007
        max_v = 0
        for x in nums:
            if x > max_v:
                max_v = x
        dp = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        dp[0][0] = 1
        for x in nums:
            ndp = [[0] * (max_v + 1) for _ in range(max_v + 1)]
            for a in range(max_v + 1):
                for b in range(max_v + 1):
                    ndp[a][b] = dp[a][b]
            for a in range(max_v + 1):
                for b in range(max_v + 1):
                    if dp[a][b] == 0:
                        continue
                    na = x if a == 0 else gcd(a, x)
                    nb = x if b == 0 else gcd(b, x)
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
            dp = ndp
        ans = 0
        for g in range(1, max_v + 1):
            ans = (ans + dp[g][g]) % mod
        return ans
