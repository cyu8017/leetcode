# LeetCode 0746 - Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for c in reversed(cost):
            a, b = c + min(a, b), a
        return min(a, b)
