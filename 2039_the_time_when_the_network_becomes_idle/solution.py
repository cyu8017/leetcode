# LeetCode 2039 - The Time When the Network Becomes Idle
# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

from collections import deque
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        dist = [-1] * n
        q = deque([0])
        dist[0] = 0
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        ans = 0
        for i in range(1, n):
            rnd = dist[i] * 2
            last_send = ((rnd - 1) // patience[i]) * patience[i]
            ans = max(ans, last_send + rnd)
        return ans + 1
