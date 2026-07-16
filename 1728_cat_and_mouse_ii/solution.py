from functools import lru_cache
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        total_open = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "#":
                    total_open += 1
                if grid[r][c] == "M":
                    mouse = r * cols + c
                elif grid[r][c] == "C":
                    cat = r * cols + c
                elif grid[r][c] == "F":
                    food = r * cols + c

        def moves(pos: int, jump: int) -> list[int]:
            r, c = divmod(pos, cols)
            out = [pos]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                for step in range(1, jump + 1):
                    nr, nc = r + dr * step, c + dc * step
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == "#":
                        break
                    out.append(nr * cols + nc)
            return out

        mouse_moves = {}
        cat_moves = {}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "#":
                    pos = r * cols + c
                    mouse_moves[pos] = moves(pos, mouseJump)
                    cat_moves[pos] = moves(pos, catJump)

        @lru_cache(None)
        def win(m: int, c: int, turn: int) -> bool:
            if turn >= 2 * total_open:
                return False
            if m == food:
                return True
            if c == food or c == m:
                return False
            if turn % 2 == 0:
                return any(win(nm, c, turn + 1) for nm in mouse_moves[m])
            return all(win(m, nc, turn + 1) for nc in cat_moves[c])

        return win(mouse, cat, 0)
