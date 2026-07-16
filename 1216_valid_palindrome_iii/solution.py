class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            previous = 0
            for j in range(i + 1, len(s)):
                old = dp[j]
                if s[i] == s[j]: dp[j] = previous
                else: dp[j] = 1 + min(dp[j], dp[j - 1])
                previous = old
        return not s or dp[-1] <= k
