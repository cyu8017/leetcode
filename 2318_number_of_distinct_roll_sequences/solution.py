# LeetCode 2318 - Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/


class Solution:
    def distinctSequences(self, n: int) -> int:
        mod = 1000000007

        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        dp = [[[0] * 7 for _ in range(7)] for _ in range(n + 1)]
        for a in range(1, 7):
            dp[1][a][0] = 1
        for i in range(2, n + 1):
            for prev in range(1, 7):
                for pprev in range(7):
                    if dp[i - 1][prev][pprev] == 0:
                        continue
                    for cur in range(1, 7):
                        if cur == prev or cur == pprev or gcd(cur, prev) != 1:
                            continue
                        dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod
        ans = 0
        for a in range(1, 7):
            for b in range(7):
                ans = (ans + dp[n][a][b]) % mod
        return ans
