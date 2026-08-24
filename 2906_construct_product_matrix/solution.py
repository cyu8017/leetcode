# LeetCode 2906 - Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        pref = 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = pref
                pref = (pref * (grid[i][j] % mod)) % mod
        suf = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = (ans[i][j] * suf) % mod
                suf = (suf * (grid[i][j] % mod)) % mod
        return ans
