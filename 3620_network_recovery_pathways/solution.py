# LeetCode 3620 - Network Recovery Pathways
# https://leetcode.com/problems/network-recovery-pathways/

from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = 2147483647, 0
        for e in edges:
            u, v, w = e[0], e[1], e[2]
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            l = min(l, w)
            r = max(r, w)
        if l == 2147483647:
            return -1

        def check(mid: int) -> bool:
            INF = 1073741823
            dist = [INF] * n
            dist[0] = 0
            pq = [[0, 0]]
            while pq:
                pq.sort(key=lambda x: x[0])
                d, u = pq.pop(0)
                if d > k:
                    return False
                if u == n - 1:
                    return True
                if dist[u] < d:
                    continue
                for v, w in g[u]:
                    if w < mid:
                        continue
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        pq.append([nd, v])
            return False

        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l if check(l) else -1
