# LeetCode 3784 - Minimum Deletion Cost to Make All Characters Equal
# https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        tot = 0
        g = {}
        for i in range(len(cost)):
            tot += cost[i]
            g[s[i]] = g.get(s[i], 0) + cost[i]
        ans = tot
        for x in g.values():
            ans = min(ans, tot - x)
        return ans
