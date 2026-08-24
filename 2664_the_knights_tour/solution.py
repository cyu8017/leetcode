# LeetCode 2664 - The Knight's Tour
# https://leetcode.com/problems/the-knights-tour/

from typing import List


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        ans = [[-1] * n for _ in range(m)]

        def dfs(x: int, y: int, step: int) -> bool:
            ans[x][y] = step
            if step == m * n - 1:
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                    if dfs(nx, ny, step + 1):
                        return True
            ans[x][y] = -1
            return False

        dfs(r, c, 0)
        return ans
