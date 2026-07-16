# LeetCode 0312 - Burst Balloons
# https://leetcode.com/problems/burst-balloons/

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        size = len(balloons)
        dp = [[0] * size for _ in range(size)]
        for length in range(3, size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                for mid in range(left + 1, right):
                    coins = (
                        dp[left][mid]
                        + dp[mid][right]
                        + balloons[left] * balloons[mid] * balloons[right]
                    )
                    dp[left][right] = max(dp[left][right], coins)
        return dp[0][size - 1]
