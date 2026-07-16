from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = sum(grid, [])
        k %= len(flat)
        flat = flat[-k:] + flat[:-k] if k else flat
        return [flat[i * n:(i + 1) * n] for i in range(m)]
