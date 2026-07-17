# LeetCode 1810 - Minimum Path Cost in a Hidden Grid
# https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

import heapq


class Solution:
    _DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    _OPP = {"U": "D", "D": "U", "L": "R", "R": "L"}

    def findShortestPath(self, master) -> int:
        move_cost: dict[tuple[int, int], int] = {(0, 0): 0}
        target: tuple[int, int] | None = None

        if master.isTarget():
            return 0

        def dfs(r: int, c: int) -> None:
            nonlocal target
            for direction, (dr, dc) in self._DIRS.items():
                if not master.canMove(direction):
                    continue
                cost = master.move(direction)
                nr, nc = r + dr, c + dc
                if (nr, nc) not in move_cost:
                    move_cost[(nr, nc)] = cost
                    if master.isTarget():
                        target = (nr, nc)
                    dfs(nr, nc)
                master.move(self._OPP[direction])

        dfs(0, 0)
        if target is None:
            return -1

        best: dict[tuple[int, int], int] = {(0, 0): 0}
        heap: list[tuple[int, int, int]] = [(0, 0, 0)]

        while heap:
            dist, r, c = heapq.heappop(heap)
            if (r, c) == target:
                return dist
            if dist > best.get((r, c), float("inf")):
                continue
            for dr, dc in self._DIRS.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) not in move_cost:
                    continue
                nd = dist + move_cost[(nr, nc)]
                if nd < best.get((nr, nc), float("inf")):
                    best[(nr, nc)] = nd
                    heapq.heappush(heap, (nd, nr, nc))
        return -1
