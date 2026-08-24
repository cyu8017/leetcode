# LeetCode 2204 - Distance to a Cycle in Undirected Graph
# https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

from typing import List
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        deg = [0] * (n)
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
            deg[e[0]] += 1
            deg[e[1]] += 1
        q = []
        for i in range(n):
            if deg[i] == 1:
                q.append(i)
        onCycle = [True] * (n)
        while q:
            u = q.pop(0)
            onCycle[u] = False
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 1:
                    q.append(v)
        ans = [-1] * (n)
        qq = []
        for i in range(n):
            if onCycle[i]:
                ans[i] = 0
                qq.append(i)
        while qq:
            u = qq.pop(0)
            for v in g[u]:
                if ans[v] == -1:
                    ans[v] = ans[u] + 1
                    qq.append(v)
        return ans
