from collections import deque

class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        n = len(grid)
        start, target = (0, 0, 0), (n - 1, n - 2, 0)
        q, seen = deque([(start, 0)]), {start}
        while q:
            (r, c, orient), moves = q.popleft()
            if (r, c, orient) == target: return moves
            nxt = []
            if orient == 0:
                if c + 2 < n and grid[r][c + 2] == 0: nxt.append((r, c + 1, 0))
                if r + 1 < n and grid[r + 1][c] == grid[r + 1][c + 1] == 0:
                    nxt += [(r + 1, c, 0), (r, c, 1)]
            else:
                if r + 2 < n and grid[r + 2][c] == 0: nxt.append((r + 1, c, 1))
                if c + 1 < n and grid[r][c + 1] == grid[r + 1][c + 1] == 0:
                    nxt += [(r, c + 1, 1), (r, c, 0)]
            for state in nxt:
                if state not in seen:
                    seen.add(state)
                    q.append((state, moves + 1))
        return -1
