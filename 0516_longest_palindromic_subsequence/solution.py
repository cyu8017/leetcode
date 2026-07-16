# LeetCode 0516 - Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for index in range(length - 1, -1, -1):
            dp[index][index] = 1
            for end in range(index + 1, length):
                if s[index] == s[end]:
                    dp[index][end] = dp[index + 1][end - 1] + 2
                else:
                    dp[index][end] = max(dp[index + 1][end], dp[index][end - 1])
        return dp[0][length - 1]
