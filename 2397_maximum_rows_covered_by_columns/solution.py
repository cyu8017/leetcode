# LeetCode 2397 - Maximum Rows Covered by Columns
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        def dfs(col: int, chosen: int, mask: int) -> None:
            nonlocal ans
            if chosen == numSelect:
                covered = 0
                for i in range(m):
                    ok = True
                    for j in range(n):
                        if matrix[i][j] == 1 and ((mask >> j) & 1) == 0:
                            ok = False
                            break
                    if ok:
                        covered += 1
                ans = max(ans, covered)
                return
            if col == n:
                return
            dfs(col + 1, chosen + 1, mask | (1 << col))
            dfs(col + 1, chosen, mask)

        dfs(0, 0, 0)
        return ans
