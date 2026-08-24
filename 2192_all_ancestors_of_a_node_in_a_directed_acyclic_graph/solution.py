# LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        indeg = [0] * (n)
        for a, b in edges:
            g[a].append(b)
            indeg[b] += 1
        anc = [set() for _ in range(n)]
        q = []
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            u = q.pop(0)
            for v in g[u]:
                anc[v].add(u)
                for x in anc[u]:
                    anc[v].add(x)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return [sorted(s) for s in anc]
