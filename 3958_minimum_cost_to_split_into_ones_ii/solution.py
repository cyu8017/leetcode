# LeetCode 3958 - Minimum Cost To Split Into Ones II
# https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/


class Solution:
    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2
