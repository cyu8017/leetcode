# LeetCode 1692 - Count Ways to Distribute Candies
# Stirling numbers of the second kind S(n, k).

class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, k), 0, -1):
                dp[j] = (dp[j - 1] + j * dp[j]) % MOD
            dp[0] = 0
        return dp[k]
