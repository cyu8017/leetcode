class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        mod = 1_000_000_007
        dp = [[0] * (rollMax[j] + 1) for j in range(6)]
        for j in range(6): dp[j][1] = 1
        for _ in range(1, n):
            totals = [sum(row) % mod for row in dp]
            nxt = [[0] * len(dp[j]) for j in range(6)]
            for j in range(6):
                nxt[j][1] = (sum(totals) - totals[j]) % mod
                for run in range(2, len(dp[j])):
                    nxt[j][run] = dp[j][run - 1]
            dp = nxt
        return sum(map(sum, dp)) % mod
