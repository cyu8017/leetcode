# LeetCode 2718 - Sum of Matrix After Queries
# https://leetcode.com/problems/sum-of-matrix-after-queries/

from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_done = [False] * n
        col_done = [False] * n
        rows_left, cols_left = n, n
        ans = 0
        for i in range(len(queries) - 1, -1, -1):
            typ, idx, val = queries[i]
            if typ == 0:
                if not row_done[idx]:
                    ans += val * cols_left
                    row_done[idx] = True
                    rows_left -= 1
            else:
                if not col_done[idx]:
                    ans += val * rows_left
                    col_done[idx] = True
                    cols_left -= 1
        return ans
