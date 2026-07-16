# LeetCode 0883 - Projection Area of 3D Shapes
# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        top = sum(1 for i in range(n) for j in range(n) if grid[i][j])
        front = sum(max(row) for row in grid)
        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return top + front + side
