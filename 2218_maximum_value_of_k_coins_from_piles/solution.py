# LeetCode 2218 - Maximum Value of K Coins From Piles
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from typing import List
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pile in piles:
            ndp = dp[:]
            sum = 0
            take = 1
            while take <= len(pile) and take <= k:
                sum += pile[take - 1]
                for j in range(take, (k) + 1):
                    ndp[j] = max(ndp[j], dp[j - take] + sum)
                take += 1
            dp = ndp
        return dp[k]
