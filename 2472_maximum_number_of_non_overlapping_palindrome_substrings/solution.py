# LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n - 1):
            is_pal[i][i + 1] = s[i] == s[i + 1]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            for j in range(i + k - 1, n):
                if is_pal[i][j] and 1 + dp[j + 1] > dp[i]:
                    dp[i] = 1 + dp[j + 1]
        return dp[0]
