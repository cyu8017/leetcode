# LeetCode 3033 - Modify the Matrix
# https://leetcode.com/problems/modify-the-matrix/

from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        for j in range(n):
            mx = -1
            for i in range(m):
                mx = max(mx, matrix[i][j])
            for i in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = mx
        return matrix
