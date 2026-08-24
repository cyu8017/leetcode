# LeetCode 3791 - Number of Balanced Integers in a Range
# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

from typing import List


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        BASE = 90
        num = ""
        f: List[List[int]] = []

        def dfs(pos: int, diff: int, lim: bool) -> int:
            if pos >= len(num):
                return 1 if diff == 0 else 0
            if not lim and f[pos][diff + BASE] != -1:
                return f[pos][diff + BASE]
            up = ord(num[pos]) - 48 if lim else 9
            res = 0
            for i in range(up + 1):
                if pos % 2 == 0:
                    res += dfs(pos + 1, diff + i, lim and i == up)
                else:
                    res += dfs(pos + 1, diff - i, lim and i == up)
            if not lim:
                f[pos][diff + BASE] = res
            return res

        if high < 11:
            return 0
        if low < 11:
            low = 11
        num = str(low - 1)
        f = [[-1] * 181 for _ in range(20)]
        a = dfs(0, 0, True)
        num = str(high)
        f = [[-1] * 181 for _ in range(20)]
        b = dfs(0, 0, True)
        return b - a
