# LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        ans = [0]

        def dfs(u: int, p: int) -> int:
            people = 1
            for v in g[u]:
                if v != p:
                    people += dfs(v, u)
            if u != 0:
                ans[0] += (people + seats - 1) // seats
            return people

        dfs(0, -1)
        return ans[0]
