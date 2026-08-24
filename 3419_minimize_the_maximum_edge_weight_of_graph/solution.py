# LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

from typing import List


class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def ok(mid: int) -> bool:
            g = [[] for _ in range(n)]
            for e in edges:
                if e[2] <= mid:
                    g[e[1]].append(e[0])
            vis = [False] * n
            q = [0]
            vis[0] = True
            cnt = 1
            while q:
                u = q.pop(0)
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        cnt += 1
                        q.append(v)
            return cnt == n

        lo, hi, ans = 1, 1000001, -1
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid
            else:
                lo = mid + 1
        return ans
