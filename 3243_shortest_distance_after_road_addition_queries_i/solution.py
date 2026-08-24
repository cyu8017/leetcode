# LeetCode 3243 - Shortest Distance After Road Addition Queries I
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append(i + 1)

        def bfs() -> int:
            q = deque([0])
            vis = [False] * n
            vis[0] = True
            d = 0
            while True:
                k = len(q)
                while k > 0:
                    u = q.popleft()
                    if u == n - 1:
                        return d
                    for v in g[u]:
                        if not vis[v]:
                            vis[v] = True
                            q.append(v)
                    k -= 1
                d += 1

        ans = [0] * len(queries)
        for i in range(len(queries)):
            g[queries[i][0]].append(queries[i][1])
            ans[i] = bfs()
        return ans
