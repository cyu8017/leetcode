# LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def bfs_depth(start: int) -> int:
            dist = [-1] * (n + 1)
            q = deque([start])
            dist[start] = 1
            best = 1
            while q:
                u = q.popleft()
                if dist[u] > best:
                    best = dist[u]
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return best

        color = [-1] * (n + 1)
        components = []
        for i in range(1, n + 1):
            if color[i] != -1:
                continue
            comp = []
            q = deque([i])
            color[i] = 0
            bipartite = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        bipartite = False
            if not bipartite:
                return -1
            components.append(comp)
        ans = 0
        for comp in components:
            best = 0
            for u in comp:
                best = max(best, bfs_depth(u))
            ans += best
        return ans
