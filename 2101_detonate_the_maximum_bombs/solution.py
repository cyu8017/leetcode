# LeetCode 2101 - Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/

from collections import deque
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                dx = bombs[j][0] - x1
                dy = bombs[j][1] - y1
                if dx * dx + dy * dy <= r1 * r1:
                    g[i].append(j)
        ans = 0
        for i in range(n):
            vis = [False] * n
            q = deque([i])
            vis[i] = True
            cnt = 0
            while q:
                u = q.popleft()
                cnt += 1
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)
            ans = max(ans, cnt)
        return ans
