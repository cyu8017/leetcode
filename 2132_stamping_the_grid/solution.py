# LeetCode 2132 - Stamping the Grid
# https://leetcode.com/problems/stamping-the-grid/

from typing import List
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j]
        diff = [[0] * (n + 1) for _ in range(m + 1)]
        i = 0
        while i + stampHeight - 1 < m:
            j = 0
            while j + stampWidth - 1 < n:
                sum = pref[i + stampHeight][j + stampWidth] - pref[i][j + stampWidth] - pref[i + stampHeight][j] + pref[i][j]
                if sum == 0:
                    diff[i][j] += 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1
                j += 1
            i += 1
        cur = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = diff[i][j]
                if i > 0:
                    v += cur[i - 1][j]
                if j > 0:
                    v += cur[i][j - 1]
                if i > 0 and j > 0:
                    v -= cur[i - 1][j - 1]
                cur[i][j] = v
                if grid[i][j] == 0 and v == 0:
                    return False
        return True
