class Solution:
    def numOfArrays(self, n, m, k):
        mod = 1_000_000_007
        dp = [[0] * (m + 1) for _ in range(k + 1)]
        for maximum in range(1, m + 1):
            dp[1][maximum] = 1
        for _ in range(1, n):
            nxt = [[0] * (m + 1) for _ in range(k + 1)]
            for cost in range(1, k + 1):
                prefix = 0
                for maximum in range(1, m + 1):
                    prefix = (prefix + dp[cost - 1][maximum - 1]) % mod
                    nxt[cost][maximum] = (maximum * dp[cost][maximum] + prefix) % mod
            dp = nxt
        return sum(dp[k]) % mod
