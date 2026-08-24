# LeetCode 2189 - Number of Ways to Build House of Cards
# https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/
class Solution:
    def houseOfCards(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        k = 1
        while 3 * k - 1 <= n:
            cost = 3 * k - 1
            for j in range(n, (cost) - 1, -1):
                dp[j] += dp[j - cost]
            k += 1
        return dp[n]
