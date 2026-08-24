# LeetCode 2536 - Increment Submatrices by One
# https://leetcode.com/problems/increment-submatrices-by-one/

from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for q in queries:
            r1, c1, r2, c2 = q[0], q[1], q[2], q[3]
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                v = diff[i][j]
                if i > 0:
                    v += mat[i - 1][j]
                if j > 0:
                    v += mat[i][j - 1]
                if i > 0 and j > 0:
                    v -= mat[i - 1][j - 1]
                mat[i][j] = v
        return mat
