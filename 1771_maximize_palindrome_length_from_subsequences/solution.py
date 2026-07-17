class Solution:
    def longestPalindrome(self, word1, word2):
        s = word1 + word2
        n = len(s)
        n1 = len(word1)
        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 if j == i + 1 else dp[i + 1][j - 1] + 2
                    if i < n1 <= j:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return ans
