# LeetCode 2661 - First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos_r = [0] * (m * n + 1)
        pos_c = [0] * (m * n + 1)
        for i in range(m):
            for j in range(n):
                pos_r[mat[i][j]] = i
                pos_c[mat[i][j]] = j
        row_cnt = [0] * m
        col_cnt = [0] * n
        for i, val in enumerate(arr):
            r, c = pos_r[val], pos_c[val]
            row_cnt[r] += 1
            col_cnt[c] += 1
            if row_cnt[r] == n or col_cnt[c] == m:
                return i
        return -1
