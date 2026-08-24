# LeetCode 2959 - Number of Possible Sets of Closing Branches
# https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << n):
            dist = [[1 << 29] * n for _ in range(n)]
            for i in range(n):
                dist[i][i] = 0
            for r in roads:
                u, v, w = r[0], r[1], r[2]
                if (mask & (1 << u)) != 0 and (mask & (1 << v)) != 0:
                    if w < dist[u][v]:
                        dist[u][v] = w
                        dist[v][u] = w
            for k in range(n):
                if (mask & (1 << k)) == 0:
                    continue
                for i in range(n):
                    if (mask & (1 << i)) == 0:
                        continue
                    for j in range(n):
                        if (mask & (1 << j)) == 0:
                            continue
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
            ok = True
            i = 0
            while i < n and ok:
                if (mask & (1 << i)) == 0:
                    i += 1
                    continue
                for j in range(n):
                    if (mask & (1 << j)) == 0:
                        continue
                    if dist[i][j] > maxDistance:
                        ok = False
                        break
                i += 1
            if ok:
                ans += 1
        return ans
