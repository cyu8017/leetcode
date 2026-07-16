# LeetCode 0322 - Coin Change
# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] = min(dp[value], dp[value - coin] + 1)
        return -1 if dp[amount] == max_value else dp[amount]
