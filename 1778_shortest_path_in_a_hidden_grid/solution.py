class GridMaster:
    DIR = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    OPP = {"U": "D", "D": "U", "L": "R", "R": "L"}

    def __init__(self, grid):
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.r = self.c = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == -1:
                    self.r, self.c = i, j

    def canMove(self, direction):
        dr, dc = self.DIR[direction]
        nr, nc = self.r + dr, self.c + dc
        return 0 <= nr < self.m and 0 <= nc < self.n and self.grid[nr][nc] != 0

    def move(self, direction):
        if self.canMove(direction):
            dr, dc = self.DIR[direction]
            self.r += dr
            self.c += dc

    def isTarget(self):
        return self.grid[self.r][self.c] == 2

class Solution:
    def findShortestPath(self, master):
        if isinstance(master, list):
            master = GridMaster(master)
        from collections import deque

        world = {(0, 0): 1}
        target = None
        if master.isTarget():
            return 0

        def dfs(r, c):
            nonlocal target
            for d, (dr, dc) in GridMaster.DIR.items():
                if not master.canMove(d):
                    continue
                master.move(d)
                nr, nc = r + dr, c + dc
                if (nr, nc) not in world:
                    world[(nr, nc)] = 2 if master.isTarget() else 1
                    if master.isTarget():
                        target = (nr, nc)
                    dfs(nr, nc)
                master.move(GridMaster.OPP[d])

        dfs(0, 0)
        if target is None:
            return -1
        q = deque([(0, 0, 0)])
        seen = {(0, 0)}
        while q:
            r, c, dist = q.popleft()
            if (r, c) == target:
                return dist
            for dr, dc in GridMaster.DIR.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) in world and world[(nr, nc)] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, dist + 1))
        return -1
