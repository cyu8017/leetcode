# LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        s1 = [[0] * (n + 2) for _ in range(m + 1)]
        s2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i, row in enumerate(grid, 1):
            for j, value in enumerate(row, 1):
                s1[i][j] = s1[i - 1][j - 1] + value
                s2[i][j] = s2[i - 1][j + 1] + value

        rhombus_sums = set()
        for i, row in enumerate(grid, 1):
            for j, value in enumerate(row, 1):
                limit = min(i - 1, m - i, j - 1, n - j)
                rhombus_sums.add(value)
                for k in range(1, limit + 1):
                    a = s1[i + k][j] - s1[i][j - k]
                    b = s1[i][j + k] - s1[i - k][j]
                    c = s2[i][j - k] - s2[i - k][j]
                    d = s2[i + k][j] - s2[i][j + k]
                    rhombus_sums.add(
                        a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
                    )

        return sorted(rhombus_sums, reverse=True)[:3]
