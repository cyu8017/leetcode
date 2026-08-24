# LeetCode 3537 - Fill a Special Grid
# https://leetcode.com/problems/fill-a-special-grid/

from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        m = 1 << n
        ans = [[0] * m for _ in range(m)]
        val = 0

        def dfs(x: int, y: int, k: int) -> None:
            nonlocal val
            if k == 1:
                ans[x][y] = val
                val += 1
                return
            h = k >> 1
            dfs(x, y, h)
            dfs(x + h, y, h)
            dfs(x + h, y - h, h)
            dfs(x, y - h, h)

        dfs(0, m - 1, m)
        return ans
