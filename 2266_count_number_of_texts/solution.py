# LeetCode 2266 - Count Number of Texts
# https://leetcode.com/problems/count-number-of-texts/


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 1000000007
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            max_press = 4 if pressedKeys[i - 1] in ("7", "9") else 3
            for j in range(2, max_press + 1):
                if j > i:
                    break
                if pressedKeys[i - j] != pressedKeys[i - 1]:
                    break
                dp[i] = (dp[i] + dp[i - j]) % mod
        return dp[n]
