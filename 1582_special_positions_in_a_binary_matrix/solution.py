from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]
        return sum(mat[i][j] == rows[i] == cols[j] == 1 for i in range(len(mat)) for j in range(len(mat[0])))
