from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])

        def dfs(r: int, c: int) -> bool:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0
            ok = grid1[r][c] == 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not dfs(nr, nc):
                    ok = False
            return ok

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and dfs(r, c):
                    ans += 1
        return ans
