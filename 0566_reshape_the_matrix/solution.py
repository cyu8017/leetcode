# LeetCode 0566 - Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c:
            return mat

        flat = [value for row in mat for value in row]
        return [flat[i * c : (i + 1) * c] for i in range(r)]
