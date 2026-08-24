# LeetCode 3341 - Find Minimum Time to Reach Last Room I
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dist = [[1 << 30] * n for _ in range(m)]
        h = [[0, 0, 0]]
        dist[0][0] = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while h:
            h.sort(key=lambda a: a[0])
            t, r, c = h.pop(0)
            if t != dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                start = max(t, moveTime[nr][nc])
                nt = start + 1
                if nt < dist[nr][nc]:
                    dist[nr][nc] = nt
                    h.append([nt, nr, nc])
        return -1
