# LeetCode 3313 - Find the Last Marked Nodes in Tree
# https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

from typing import List, Tuple


class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def bfs(start: int) -> Tuple[int, List[int]]:
            dist = [-1] * n
            q = [start]
            dist[start] = 0
            far = start
            qi = 0
            while qi < len(q):
                u = q[qi]
                qi += 1
                if dist[u] > dist[far]:
                    far = u
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return far, dist

        u = bfs(0)[0]
        v, du = bfs(u)
        dv = bfs(v)[1]
        return [u if du[i] >= dv[i] else v for i in range(n)]
