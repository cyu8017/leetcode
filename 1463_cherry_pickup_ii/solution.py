from typing import List, Optional

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {(0, n - 1): grid[0][0] + (grid[0][n-1] if n > 1 else 0)}
        for r in range(1, m):
            nxt = {}
            for (a, b), score in dp.items():
                for na in (a-1, a, a+1):
                    for nb in (b-1, b, b+1):
                        if 0 <= na < n and 0 <= nb < n:
                            val = score + grid[r][na] + (grid[r][nb] if na != nb else 0)
                            nxt[na, nb] = max(nxt.get((na, nb), -1), val)
            dp = nxt
        return max(dp.values())
