# LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        max_val = grid[0][0]
        for row in grid:
            for x in row:
                max_val = max(max_val, x)

        def check(target: int) -> int:
            diff = [[0] * (n + 2) for _ in range(m + 2)]
            total_ops = 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                    cur_val = grid[i - 1][j - 1] + diff[i][j]
                    if cur_val > target:
                        return -1
                    if cur_val < target:
                        if i + k - 1 > m or j + k - 1 > n:
                            return -1
                        needed = target - cur_val
                        total_ops += needed
                        diff[i][j] += needed
                        diff[i + k][j] -= needed
                        diff[i][j + k] -= needed
                        diff[i + k][j + k] += needed
            return total_ops

        for t in range(max_val, max_val + 2):
            res = check(t)
            if res != -1:
                return res
        return -1
