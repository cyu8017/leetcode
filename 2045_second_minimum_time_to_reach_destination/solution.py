# LeetCode 2045 - Second Minimum Time to Reach Destination
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/

from collections import deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        q = deque([(1, 0)])
        dist1[1] = 0
        while q:
            u, d = q.popleft()
            for v in g[u]:
                nd = d + 1
                if dist1[v] == -1:
                    dist1[v] = nd
                    q.append((v, nd))
                elif dist2[v] == -1 and nd > dist1[v]:
                    dist2[v] = nd
                    q.append((v, nd))
        steps = dist2[n]
        ans = 0
        for _ in range(steps):
            if (ans // change) % 2 == 1:
                ans += change - ans % change
            ans += time
        return ans
