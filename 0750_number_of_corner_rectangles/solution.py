# LeetCode 0750 - Number Of Corner Rectangles
# https://leetcode.com/problems/number-of-corner-rectangles/

from typing import List


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(i + 1, m):
                count = 0
                for c in range(n):
                    if grid[i][c] and grid[j][c]:
                        count += 1
                ans += count * (count - 1) // 2
        return ans
