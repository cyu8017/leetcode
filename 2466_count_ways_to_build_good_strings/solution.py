# LeetCode 2466 - Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1000000007
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % mod
            if i >= low:
                ans = (ans + dp[i]) % mod
        return ans
