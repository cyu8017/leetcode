# LeetCode 2946 - Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            if i % 2 == 0:
                shift = n - (k % n)
                if shift == n:
                    shift = 0
            else:
                shift = k % n
            for j in range(n):
                if mat[i][j] != mat[i][(j + shift) % n]:
                    return False
        return True
