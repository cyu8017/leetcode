from collections import deque
from typing import List

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "B": box = (r, c)
                elif grid[r][c] == "S": player = (r, c)
                elif grid[r][c] == "T": target = (r, c)
        def reachable(start, blocked):
            seen, stack = {start}, [start]
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nxt = (r + dr, c + dc)
                    if (0 <= nxt[0] < m and 0 <= nxt[1] < n and
                            grid[nxt[0]][nxt[1]] != "#" and nxt != blocked and nxt not in seen):
                        seen.add(nxt); stack.append(nxt)
            return seen
        queue = deque([(box, player, 0)])
        seen = {(box, player)}
        while queue:
            b, p, pushes = queue.popleft()
            if b == target:
                return pushes
            can_reach = reachable(p, b)
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                stand = (b[0] - dr, b[1] - dc)
                nb = (b[0] + dr, b[1] + dc)
                if (stand in can_reach and 0 <= nb[0] < m and 0 <= nb[1] < n
                        and grid[nb[0]][nb[1]] != "#"):
                    state = (nb, b)
                    if state not in seen:
                        seen.add(state)
                        queue.append((nb, b, pushes + 1))
        return -1
