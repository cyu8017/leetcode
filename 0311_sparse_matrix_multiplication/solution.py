# LeetCode 0311 - Sparse Matrix Multiplication
# https://leetcode.com/problems/sparse-matrix-multiplication/

from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rows = len(mat1)
        inner = len(mat1[0])
        cols = len(mat2[0])
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for index in range(inner):
                if mat1[row][index] == 0:
                    continue
                for col in range(cols):
                    if mat2[index][col] != 0:
                        result[row][col] += mat1[row][index] * mat2[index][col]
        return result
