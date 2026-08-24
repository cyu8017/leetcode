# LeetCode 3807 - Minimum Cost to Repair Edges to Traverse a Graph
# https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges = sorted(edges, key=lambda e: e[2])
        m = len(edges)
        if m == 0:
            return -1

        def check(idx: int) -> bool:
            g = [[] for _ in range(n)]
            for i in range(idx + 1):
                g[edges[i][0]].append(edges[i][1])
                g[edges[i][1]].append(edges[i][0])
            q = [0]
            vis = [False] * n
            vis[0] = True
            dist = 0
            while q:
                nq = []
                for u in q:
                    if u == n - 1:
                        return dist <= k
                    for v in g[u]:
                        if not vis[v]:
                            vis[v] = True
                            nq.append(v)
                q = nq
                dist += 1
            return False

        l, r = 0, m - 1
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        if check(l):
            return edges[l][2]
        return -1
