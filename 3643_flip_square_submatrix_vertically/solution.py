# LeetCode 3643 - Flip Square Submatrix Vertically
# https://leetcode.com/problems/flip-square-submatrix-vertically/

from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x, x + k // 2):
            i2 = x + k - 1 - (i - x)
            for j in range(y, y + k):
                grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]
        return grid
