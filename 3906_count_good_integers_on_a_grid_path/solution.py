# LeetCode 3906 - Count Good Integers On A Grid Path
# https://leetcode.com/problems/count-good-integers-on-a-grid-path/

from typing import List


class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        key = [False] * 16
        row = 0
        col = 0
        key[0] = True
        for c in directions:
            if c == "D":
                row += 1
            else:
                col += 1
            key[row * 4 + col] = True
        s = ""
        f: List[List[int]] = []

        def dfs(pos: int, last: int, lim: bool) -> int:
            if pos == 16:
                return 1
            if not lim and f[pos][last] != -1:
                return f[pos][last]
            res = 0
            start = last if key[pos] else 0
            end = ord(s[pos]) - 48 if lim else 9
            for i in range(start, end + 1):
                next_last = i if key[pos] else last
                res += dfs(pos + 1, next_last, lim and (i == end))
            if not lim:
                f[pos][last] = res
            return res

        def calc(x: int) -> int:
            nonlocal s, f
            if x < 0:
                return 0
            t = str(x)
            s = "0" * (16 - len(t)) + t
            f = [[-1] * 10 for _ in range(16)]
            return dfs(0, 0, True)

        return calc(r) - calc(l - 1)
