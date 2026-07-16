# LeetCode 0879 - Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for members, p in zip(group, profit):
            for people in range(n, members - 1, -1):
                for prof in range(minProfit, -1, -1):
                    np = min(minProfit, prof + p)
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD
        return sum(dp[people][minProfit] for people in range(n + 1)) % MOD
