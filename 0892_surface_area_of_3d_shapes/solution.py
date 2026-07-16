# LeetCode 0892 - Surface Area of 3D Shapes
# https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += grid[i][j] * 4 + 2
                    if i:
                        area -= min(grid[i][j], grid[i - 1][j]) * 2
                    if j:
                        area -= min(grid[i][j], grid[i][j - 1]) * 2
        return area
