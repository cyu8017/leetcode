# LeetCode 2952 - Minimum Number of Coins to be Added
# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        ans = 0
        reach = 0
        i = 0
        while reach < target:
            if i < len(coins) and coins[i] <= reach + 1:
                reach += coins[i]
                i += 1
            else:
                reach += reach + 1
                ans += 1
        return ans
