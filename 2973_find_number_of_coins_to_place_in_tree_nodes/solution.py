# LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        ans = [0] * n

        def dfs(u: int, p: int) -> List[int]:
            vals = [cost[u]]
            for v in g[u]:
                if v == p:
                    continue
                vals = vals + dfs(v, u)
            vals.sort()
            if len(vals) < 3:
                ans[u] = 1
            else:
                m = len(vals)
                cand1 = vals[m - 1] * vals[m - 2] * vals[m - 3]
                cand2 = vals[0] * vals[1] * vals[m - 1]
                best = max(cand1, cand2)
                if best < 0:
                    best = 0
                ans[u] = best
            if len(vals) <= 5:
                return vals
            return [vals[0], vals[1], vals[len(vals) - 3], vals[len(vals) - 2], vals[len(vals) - 1]]

        dfs(0, -1)
        return ans
