# LeetCode 3568 - Minimum Moves to Clean the Classroom
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        d = [[0] * n for _ in range(m)]
        x = y = cnt = 0
        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == "S":
                    x, y = i, j
                elif c == "L":
                    d[i][j] = cnt
                    cnt += 1
        if cnt == 0:
            return 0
        vis = [[[[False] * (1 << cnt) for _ in range(energy + 1)] for _ in range(n)] for _ in range(m)]
        q = [[x, y, energy, (1 << cnt) - 1]]
        vis[x][y][energy][(1 << cnt) - 1] = True
        dirs = [-1, 0, 1, 0, -1]
        ans = 0
        while q:
            t = q
            q = []
            for s in t:
                i, j, cur_energy, mask = s
                if mask == 0:
                    return ans
                if cur_energy <= 0:
                    continue
                for kk in range(4):
                    nx, ny = i + dirs[kk], j + dirs[kk + 1]
                    if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != "X":
                        nxt_energy = energy if classroom[nx][ny] == "R" else cur_energy - 1
                        nxt_mask = mask
                        if classroom[nx][ny] == "L":
                            nxt_mask &= ~(1 << d[nx][ny])
                        if not vis[nx][ny][nxt_energy][nxt_mask]:
                            vis[nx][ny][nxt_energy][nxt_mask] = True
                            q.append([nx, ny, nxt_energy, nxt_mask])
            ans += 1
        return -1
