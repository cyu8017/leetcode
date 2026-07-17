# LeetCode 1895 - Largest Magic Square
# https://leetcode.com/problems/largest-magic-square/

class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_prefix = [[0] * (cols + 1) for _ in range(rows)]
        col_prefix = [[0] * (rows + 1) for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j]

        def row_sum(row: int, col_start: int, col_end: int) -> int:
            return row_prefix[row][col_end + 1] - row_prefix[row][col_start]

        def col_sum(col: int, row_start: int, row_end: int) -> int:
            return col_prefix[col][row_end + 1] - col_prefix[col][row_start]

        def is_magic(row_start: int, col_start: int, size: int) -> bool:
            target = row_sum(row_start, col_start, col_start + size - 1)
            for row in range(row_start, row_start + size):
                if row_sum(row, col_start, col_start + size - 1) != target:
                    return False
            for col in range(col_start, col_start + size):
                if col_sum(col, row_start, row_start + size - 1) != target:
                    return False
            diag1 = sum(grid[row_start + offset][col_start + offset] for offset in range(size))
            diag2 = sum(
                grid[row_start + offset][col_start + size - 1 - offset] for offset in range(size)
            )
            return diag1 == target and diag2 == target

        for size in range(min(rows, cols), 0, -1):
            for row_start in range(rows - size + 1):
                for col_start in range(cols - size + 1):
                    if is_magic(row_start, col_start, size):
                        return size
        return 1
