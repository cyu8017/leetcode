# LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = []
        bas = grid[0][0] % x
        for row in grid:
            for v in row:
                if v % x != bas:
                    return -1
                vals.append(v)
        vals.sort()
        median = vals[len(vals) // 2]
        return sum(abs(v - median) // x for v in vals)
