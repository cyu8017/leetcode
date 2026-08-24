# LeetCode 3560 - Find Minimum Log Transportation Cost
# https://leetcode.com/problems/find-minimum-log-transportation-cost/


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        x = max(n, m)
        if x <= k:
            return 0
        return k * (x - k)
