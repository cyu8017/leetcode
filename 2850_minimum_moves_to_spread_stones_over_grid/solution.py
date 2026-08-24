# LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        extras = []
        zeros = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append([i, j])
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        extras.append([i, j])
        if not zeros:
            return 0
        best = 1 << 30

        def dfs(i: int, cost: int) -> None:
            nonlocal best
            if cost >= best:
                return
            if i == len(zeros):
                best = cost
                return
            for j in range(len(extras)):
                if extras[j][0] < 0:
                    continue
                e = extras[j]
                extras[j] = [-1, e[1]]
                d = abs(e[0] - zeros[i][0]) + abs(e[1] - zeros[i][1])
                dfs(i + 1, cost + d)
                extras[j] = e

        dfs(0, 0)
        return best
