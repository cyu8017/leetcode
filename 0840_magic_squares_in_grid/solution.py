# LeetCode 0840 - Magic Squares In Grid
# https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        def magic(r: int, c: int) -> bool:
            vals = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if sorted(vals) != list(range(1, 10)):
                return False
            a = grid
            return (
                a[r][c] + a[r][c + 1] + a[r][c + 2] == 15
                and a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15
                and a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15
                and a[r][c] + a[r + 1][c] + a[r + 2][c] == 15
                and a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15
                and a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15
                and a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15
                and a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15
            )

        return sum(1 for i in range(rows - 2) for j in range(cols - 2) if magic(i, j))
