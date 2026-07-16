# LeetCode 0296 - Best Meeting Point
# https://leetcode.com/problems/best-meeting-point/

from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows: list[int] = []
        cols: list[int] = []
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if value == 1:
                    rows.append(row_index)
                    cols.append(col_index)
        cols.sort()
        row_median = rows[len(rows) // 2]
        col_median = cols[len(cols) // 2]
        return sum(abs(row - row_median) for row in rows) + sum(
            abs(col - col_median) for col in cols
        )
