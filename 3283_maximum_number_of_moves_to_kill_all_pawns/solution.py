# LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
# https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

from collections import deque
from typing import Dict, List


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        DIRS = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

        def knightDist(x: int, y: int, pts: List[List[int]]) -> List[int]:
            np = len(pts)
            ans = [-1] * np
            vis = [[False] * 50 for _ in range(50)]
            q = deque([[x, y, 0]])
            vis[x][y] = True
            need: Dict[int, List[int]] = {}
            for i in range(np):
                key = (pts[i][0] << 32) | (pts[i][1] & 0xFFFFFFFF)
                if key not in need:
                    need[key] = []
                need[key].append(i)
            found = 0
            while q and found < np:
                cur = q.popleft()
                key = (cur[0] << 32) | (cur[1] & 0xFFFFFFFF)
                idxs = need.get(key)
                if idxs:
                    for i in idxs:
                        if ans[i] == -1:
                            ans[i] = cur[2]
                            found += 1
                for d in DIRS:
                    nx, ny = cur[0] + d[0], cur[1] + d[1]
                    if nx < 0 or ny < 0 or nx >= 50 or ny >= 50 or vis[nx][ny]:
                        continue
                    vis[nx][ny] = True
                    q.append([nx, ny, cur[2] + 1])
            return ans

        n = len(positions)
        pts = [[0, 0] for _ in range(n + 1)]
        pts[0][0], pts[0][1] = kx, ky
        for i in range(n):
            pts[i + 1][0] = positions[i][0]
            pts[i + 1][1] = positions[i][1]
        dist = []
        for i in range(n + 1):
            dist.append(knightDist(pts[i][0], pts[i][1], pts))
        N = 1 << n
        memo = [[-1] * (n + 1) for _ in range(N)]

        def dfs(mask: int, cur: int, turn: int) -> int:
            if mask == N - 1:
                return 0
            if memo[mask][cur] != -1:
                return memo[mask][cur]
            best = -(1 << 30) if turn == 0 else (1 << 30)
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    continue
                d = dist[cur][i + 1]
                v = d + dfs(mask | (1 << i), i + 1, 1 - turn)
                if turn == 0:
                    if v > best:
                        best = v
                elif v < best:
                    best = v
            memo[mask][cur] = best
            return best

        return dfs(0, 0, 0)
