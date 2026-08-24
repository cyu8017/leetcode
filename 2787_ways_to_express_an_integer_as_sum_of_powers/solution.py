# LeetCode 2787 - Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1000000007
        powers = []
        i = 1
        while True:
            p = 1
            for _ in range(x):
                p *= i
                if p > n:
                    break
            if p > n:
                break
            powers.append(p)
            i += 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD
        return dp[n]
