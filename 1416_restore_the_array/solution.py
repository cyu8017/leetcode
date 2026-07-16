class Solution:
    def numberOfArrays(self, s, k):
        mod, n = 1_000_000_007, len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                continue
            value = 0
            for j in range(i, n):
                value = value * 10 + int(s[j])
                if value > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % mod
        return dp[0]
