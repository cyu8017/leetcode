# LeetCode 2327 - Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 1000000007
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0
        for day in range(2, n + 1):
            if day - delay >= 1:
                share = (share + dp[day - delay]) % mod
            if day - forget >= 1:
                share = (share - dp[day - forget] + mod) % mod
            dp[day] = share
        ans = 0
        for day in range(n - forget + 1, n + 1):
            if day >= 1:
                ans = (ans + dp[day]) % mod
        return ans
