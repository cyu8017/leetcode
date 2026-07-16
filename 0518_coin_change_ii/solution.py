# LeetCode 0518 - Coin Change II
# https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] += dp[value - coin]
        return dp[amount]
