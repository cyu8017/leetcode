# LeetCode 3339 - Find the Number of K-Even Arrays
# https://leetcode.com/problems/find-the-number-of-k-even-arrays/


class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007
        even = m // 2
        odd = m - even
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
        dp[1][0][0] = odd
        dp[1][0][1] = even
        for i in range(1, n):
            for j in range(k + 1):
                dp[i + 1][j][0] = (
                    dp[i + 1][j][0]
                    + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod
                ) % mod
                dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod
                if j < k:
                    dp[i + 1][j + 1][1] = (
                        dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod
                    ) % mod
        return (dp[n][k][0] + dp[n][k][1]) % mod
