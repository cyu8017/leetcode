# LeetCode 3242 - Design Neighbor Sum Service
# https://leetcode.com/problems/design-neighbor-sum-service/

from typing import Dict, List, Tuple


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.d: Dict[int, Tuple[int, int]] = {}
        self.dirs = [
            [-1, 0, 1, 0, -1],
            [-1, 1, 1, -1, -1],
        ]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.d[grid[i][j]] = (i, j)

    def cal(self, value: int, k: int) -> int:
        p = self.d[value]
        s = 0
        for q in range(4):
            x = p[0] + self.dirs[k][q]
            y = p[1] + self.dirs[k][q + 1]
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
                s += self.grid[x][y]
        return s

    def adjacentSum(self, value: int) -> int:
        return self.cal(value, 0)

    def diagonalSum(self, value: int) -> int:
        return self.cal(value, 1)
