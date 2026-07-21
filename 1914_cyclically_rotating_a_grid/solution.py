from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            vals = []
            for c in range(layer, n - layer):
                vals.append(grid[layer][c])
            for r in range(layer + 1, m - layer):
                vals.append(grid[r][n - layer - 1])
            if m - 2 * layer > 1:
                for c in range(n - layer - 2, layer - 1, -1):
                    vals.append(grid[m - layer - 1][c])
            if n - 2 * layer > 1:
                for r in range(m - layer - 2, layer, -1):
                    vals.append(grid[r][layer])
            shift = k % len(vals)
            vals = vals[shift:] + vals[:shift]
            idx = 0
            for c in range(layer, n - layer):
                grid[layer][c] = vals[idx]
                idx += 1
            for r in range(layer + 1, m - layer):
                grid[r][n - layer - 1] = vals[idx]
                idx += 1
            if m - 2 * layer > 1:
                for c in range(n - layer - 2, layer - 1, -1):
                    grid[m - layer - 1][c] = vals[idx]
                    idx += 1
            if n - 2 * layer > 1:
                for r in range(m - layer - 2, layer, -1):
                    grid[r][layer] = vals[idx]
                    idx += 1
        return grid
