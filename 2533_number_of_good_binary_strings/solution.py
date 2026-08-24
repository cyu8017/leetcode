# LeetCode 2533 - Number of Good Binary Strings
# https://leetcode.com/problems/number-of-good-binary-strings/


class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD = 1000000007
        dp = [0] * (maxLength + 1)
        dp[0] = 1
        for i in range(maxLength + 1):
            if dp[i] == 0:
                continue
            if i + oneGroup <= maxLength:
                dp[i + oneGroup] = (dp[i + oneGroup] + dp[i]) % MOD
            if i + zeroGroup <= maxLength:
                dp[i + zeroGroup] = (dp[i + zeroGroup] + dp[i]) % MOD
        ans = 0
        for i in range(minLength, maxLength + 1):
            ans = (ans + dp[i]) % MOD
        return ans
