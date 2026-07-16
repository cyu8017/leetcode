# LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for left in range(n - 2, -1, -1):
            diagonal = 0
            for right in range(left + 1, n):
                old = dp[right]
                if s[left] == s[right]:
                    dp[right] = diagonal
                else:
                    dp[right] = 1 + min(dp[right], dp[right - 1])
                diagonal = old
        return dp[-1] if dp else 0
