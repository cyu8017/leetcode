from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(r, c, pr, pc):
            seen.add((r, c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != grid[r][c] or (nr, nc) == (pr, pc):
                    continue
                if (nr, nc) in seen or dfs(nr, nc, r, c):
                    return True
            return False
        return any((r, c) not in seen and dfs(r, c, -1, -1) for r in range(m) for c in range(n))
