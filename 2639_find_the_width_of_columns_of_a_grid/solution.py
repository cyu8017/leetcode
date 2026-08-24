# LeetCode 2639 - Find the Width of Columns of a Grid
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [0] * n

        def width(x: int) -> int:
            if x == 0:
                return 1
            w = 0
            if x < 0:
                w += 1
                x = -x
            while x > 0:
                w += 1
                x //= 10
            return w

        for row in grid:
            for j in range(n):
                ans[j] = max(ans[j], width(row[j]))
        return ans
