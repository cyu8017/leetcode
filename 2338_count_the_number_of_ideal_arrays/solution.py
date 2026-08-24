# LeetCode 2338 - Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 1000000007
        max_len = 14
        comb = [[0] * (max_len + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, min(max_len, i) + 1):
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
        dp = [[0] * (max_len + 1) for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1
        for length in range(2, max_len + 1):
            for v in range(1, maxValue + 1):
                m = 2 * v
                while m <= maxValue:
                    dp[m][length] = (dp[m][length] + dp[v][length - 1]) % mod
                    m += v
        ans = 0
        for v in range(1, maxValue + 1):
            for length in range(1, min(max_len, n) + 1):
                ans = (ans + (dp[v][length] * comb[n - 1][length - 1]) % mod) % mod
        return ans
