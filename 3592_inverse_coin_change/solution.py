# LeetCode 3592 - Inverse Coin Change
# https://leetcode.com/problems/inverse-coin-change/

from typing import List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [0] * (n + 1)
        coins = []
        dp[0] = 1
        for amt in range(1, n + 1):
            ways = numWays[amt - 1]
            if dp[amt] == ways:
                continue
            if dp[amt] + 1 == ways:
                coins.append(amt)
                for x in range(amt, n + 1):
                    dp[x] += dp[x - amt]
                if dp[amt] != ways:
                    return []
                continue
            return []
        return coins
