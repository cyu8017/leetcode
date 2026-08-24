# LeetCode 3466 - Maximum Coin Collection
# https://leetcode.com/problems/maximum-coin-collection/

from typing import List


class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        n = len(lane1)
        neg = -(10**18)
        dp = [[lane1[0], neg], [lane2[0], neg]]
        ans = max(dp[0][0], dp[1][0])
        for i in range(1, n):
            ndp = [[0, 0], [0, 0]]
            ndp[0][0] = max(dp[0][0], 0) + lane1[i]
            ndp[1][0] = max(dp[1][0], 0) + lane2[i]
            ndp[0][1] = max(dp[0][1], dp[1][0]) + lane1[i]
            ndp[1][1] = max(dp[1][1], dp[0][0]) + lane2[i]
            if lane1[i] > ndp[0][0]:
                ndp[0][0] = lane1[i]
            if lane2[i] > ndp[1][0]:
                ndp[1][0] = lane2[i]
            for a in range(2):
                for b in range(2):
                    dp[a][b] = ndp[a][b]
                    if dp[a][b] > ans:
                        ans = dp[a][b]
        return ans
