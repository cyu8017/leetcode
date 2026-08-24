# LeetCode 2370 - Longest Ideal Subsequence
# https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        ans = 0
        for ch in s:
            c = ord(ch) - 97
            best = 0
            for p in range(26):
                if abs(c - p) <= k and dp[p] > best:
                    best = dp[p]
            dp[c] = best + 1
            ans = max(ans, dp[c])
        return ans
