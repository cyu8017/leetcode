# LeetCode 3787 - Find Diameter Endpoints of a Tree
# https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

from typing import List, Tuple


class Solution:
    def findSpecialNodes(self, n: int, edges: List[List[int]]) -> str:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def bfs(start: int) -> Tuple[int, List[int]]:
            dist = [-1] * n
            dist[start] = 0
            q = [start]
            far = start
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                if dist[u] > dist[far]:
                    far = u
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return far, dist

        a, _ = bfs(0)
        b, dist1 = bfs(a)
        _, dist2 = bfs(b)
        d = dist1[b]
        ans = ["0"] * n
        for i in range(n):
            if dist1[i] == d or dist2[i] == d:
                ans[i] = "1"
        return "".join(ans)
