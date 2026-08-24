# LeetCode 3710 - Maximum Partition Factor
# https://leetcode.com/problems/maximum-partition-factor/

from typing import List


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0

        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def ok(d: int) -> bool:
            g = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if dist(i, j) < d:
                        g[i].append(j)
                        g[j].append(i)
            color = [-1] * n
            for i in range(n):
                if color[i] != -1:
                    continue
                q = [i]
                color[i] = 0
                while q:
                    u = q.pop(0)
                    for v in g[u]:
                        if color[v] == -1:
                            color[v] = color[u] ^ 1
                            q.append(v)
                        elif color[v] == color[u]:
                            return False
            return True

        lo, hi = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                hi = max(hi, dist(i, j))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
