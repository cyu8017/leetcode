# LeetCode 3446 - Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/

from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = {}
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diags:
                    diags[key] = []
                diags[key].append(grid[i][j])
        for key, lst in diags.items():
            if key >= 0:
                lst.sort(reverse=True)
            else:
                lst.sort()
        idx = {}
        for i in range(n):
            for j in range(n):
                k = i - j
                pos = idx.get(k, 0)
                grid[i][j] = diags[k][pos]
                idx[k] = pos + 1
        return grid
