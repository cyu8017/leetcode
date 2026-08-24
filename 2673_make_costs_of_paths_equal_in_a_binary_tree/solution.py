# LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = 2 * i + 1, 2 * i + 2
            ans += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
        return ans
