from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        high = [[0] * n for _ in range(m)]
        low = [[0] * n for _ in range(m)]
        high[0][0] = low[0][0] = grid[0][0]
        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    continue
                values = []
                if r:
                    values += [high[r - 1][c] * grid[r][c], low[r - 1][c] * grid[r][c]]
                if c:
                    values += [high[r][c - 1] * grid[r][c], low[r][c - 1] * grid[r][c]]
                high[r][c], low[r][c] = max(values), min(values)
        return high[-1][-1] % MOD if high[-1][-1] >= 0 else -1
