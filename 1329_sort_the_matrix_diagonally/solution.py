# LeetCode 1329 - Sort The Matrix Diagonally

from collections import defaultdict
from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        for r, row in enumerate(mat):
            for c, value in enumerate(row):
                diagonals[r-c].append(value)
        for values in diagonals.values():
            values.sort(reverse=True)
        for r, row in enumerate(mat):
            for c in range(len(row)):
                mat[r][c] = diagonals[r-c].pop()
        return mat
