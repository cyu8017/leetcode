class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            take = 0
            dp[i] = -10**18
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take - dp[j + 1])
        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
