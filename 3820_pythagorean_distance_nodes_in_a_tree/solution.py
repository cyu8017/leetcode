# LeetCode 3820 - Pythagorean Distance Nodes in a Tree
# https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

from typing import List


class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def bfs(start: int) -> List[int]:
            dist = [1000000000] * n
            q = [start]
            dist[start] = 0
            qi = 0
            while qi < len(q):
                u = q[qi]
                qi += 1
                for v in g[u]:
                    if dist[v] > dist[u] + 1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist

        d1, d2, d3 = bfs(x), bfs(y), bfs(z)
        ans = 0
        for i in range(n):
            a = sorted([d1[i], d2[i], d3[i]])
            x0, x1, x2 = a[0], a[1], a[2]
            if x0 * x0 + x1 * x1 == x2 * x2:
                ans += 1
        return ans
