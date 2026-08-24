# LeetCode 2732 - Find a Good Subset of the Matrix
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

from typing import List


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        first = {}
        for i, row in enumerate(grid):
            mask = 0
            for j in range(n):
                if row[j] == 1:
                    mask |= 1 << j
            if mask == 0:
                return [i]
            for pm, idx in first.items():
                if (pm & mask) == 0:
                    return [idx, i] if idx < i else [i, idx]
            if mask not in first:
                first[mask] = i
        return []
