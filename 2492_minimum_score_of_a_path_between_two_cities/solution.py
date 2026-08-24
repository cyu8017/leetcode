# LeetCode 2492 - Minimum Score of a Path Between Two Cities
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

from collections import deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for r in roads:
            g[r[0]].append((r[1], r[2]))
            g[r[1]].append((r[0], r[2]))
        vis = [False] * (n + 1)
        ans = 1 << 30
        q = deque([1])
        vis[1] = True
        while q:
            u = q.popleft()
            for v, w in g[u]:
                if w < ans:
                    ans = w
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
        return ans
