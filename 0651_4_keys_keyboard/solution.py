# LeetCode 0651 - 4 Keys Keyboard
# https://leetcode.com/problems/4-keys-keyboard/


class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(1, n + 1):
            for j in range(i - 2):
                # After j presses, Ctrl-A + Ctrl-C, then paste (i - j - 2) times
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[n]
