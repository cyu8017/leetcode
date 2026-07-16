# LeetCode 1034 - Coloring A Border
# https://leetcode.com/problems/coloring-a-border/

class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        component: set[tuple[int, int]] = set()
        stack = [(row, col)]
        component.add((row, col))
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == original and (nr, nc) not in component:
                    component.add((nr, nc))
                    stack.append((nr, nc))

        border: list[tuple[int, int]] = []
        for r, c in component:
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) not in component:
                    border.append((r, c))
                    break
        for r, c in border:
            grid[r][c] = color
        return grid
