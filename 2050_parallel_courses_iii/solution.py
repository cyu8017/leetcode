# LeetCode 2050 - Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/

from collections import deque
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        dist = [0] * (n + 1)
        for u, v in relations:
            g[u].append(v)
            indeg[v] += 1
        q = deque()
        for i in range(1, n + 1):
            dist[i] = time[i - 1]
            if indeg[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            for v in g[u]:
                dist[v] = max(dist[v], dist[u] + time[v - 1])
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return max(dist[1:])
