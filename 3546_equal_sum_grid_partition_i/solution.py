# LeetCode 3546 - Equal Sum Grid Partition I
# https://leetcode.com/problems/equal-sum-grid-partition-i/

from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(x for row in grid for x in row)
        if s % 2 != 0:
            return False
        m, n = len(grid), len(grid[0])
        pre = 0
        for i in range(m):
            for x in grid[i]:
                pre += x
            if pre * 2 == s and i + 1 < m:
                return True
        pre = 0
        for j in range(n):
            for i in range(m):
                pre += grid[i][j]
            if pre * 2 == s and j + 1 < n:
                return True
        return False
