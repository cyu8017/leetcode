# LeetCode 2430 - Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            length = 1
            while i + 2 * length <= n:
                if lcp[i][i + length] >= length:
                    dp[i] = max(dp[i], 1 + dp[i + length])
                length += 1
        return dp[0]
