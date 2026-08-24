# LeetCode 3342 - Find Minimum Time to Reach Last Room II
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        INF = 1 << 30
        dist = [[[INF, INF] for _ in range(n)] for _ in range(m)]
        pq = [[0, 0, 0, 0]]
        dist[0][0][0] = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while pq:
            pq.sort(key=lambda a: a[0])
            t, r, c, parity = pq.pop(0)
            if t != dist[r][c][parity]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            cost = 2 if parity == 1 else 1
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                start = max(t, moveTime[nr][nc])
                nt = start + cost
                np = 1 - parity
                if nt < dist[nr][nc][np]:
                    dist[nr][nc][np] = nt
                    pq.append([nt, nr, nc, np])
        return -1
