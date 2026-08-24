# LeetCode 3669 - Balanced K-Factor Decomposition
# https://leetcode.com/problems/balanced-k-factor-decomposition/

from typing import List


class Solution:
    _g = None

    def minDifference(self, n: int, k: int) -> List[int]:
        MX = 100001
        if Solution._g is None:
            g = [[] for _ in range(MX)]
            for i in range(1, MX):
                for j in range(i, MX, i):
                    g[j].append(i)
            Solution._g = g
        g = Solution._g
        cur = float("inf")
        ans = []
        path = [0] * k

        def dfs(i: int, x: int, mi: int, mx: int) -> None:
            nonlocal cur, ans
            if i == 0:
                d = max(mx, x) - min(mi, x)
                if d < cur:
                    cur = d
                    path[i] = x
                    ans = path[:]
                return
            for y in g[x]:
                path[i] = y
                dfs(i - 1, x // y, min(mi, y), max(mx, y))

        dfs(k - 1, n, 10**18, 0)
        return ans
