# LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        if k == 0 or k > n:
            return 0

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[1][1] = 1
        for sticks in range(2, n + 1):
            dp[sticks][1] = (sticks - 1) * dp[sticks - 1][1] % mod
            for visible in range(2, sticks + 1):
                dp[sticks][visible] = (
                    dp[sticks - 1][visible - 1] + (sticks - 1) * dp[sticks - 1][visible]
                ) % mod

        return dp[n][k]
