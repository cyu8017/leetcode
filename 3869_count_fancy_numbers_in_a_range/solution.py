# LeetCode 3869 - Count Fancy Numbers In A Range
# https://leetcode.com/problems/count-fancy-numbers-in-a-range/

from typing import List


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def check(s: int) -> bool:
            if s < 100:
                return s % 11 != 0
            mid = (s // 10) % 10
            last = s % 10
            return mid > 1 and mid < last

        num = ""
        n = 0
        f: List = []

        def dfs(pos: int, s: int, prev: int, st: int, lim: bool) -> int:
            if pos >= n:
                if st != 3:
                    return 1
                return 1 if check(s) else 0
            if not lim and f[pos][s][prev][st] != -1:
                return f[pos][s][prev][st]
            up = ord(num[pos]) - 48 if lim else 9
            res = 0
            for i in range(up + 1):
                nxt_st = st
                if st == 0:
                    if prev == 0:
                        nxt_st = 0
                    elif i > prev:
                        nxt_st = 1
                    elif i < prev:
                        nxt_st = 2
                    else:
                        nxt_st = 3
                elif st == 1:
                    nxt_st = 1 if i > prev else 3
                elif st == 2:
                    nxt_st = 2 if i < prev else 3
                else:
                    nxt_st = 3
                res += dfs(pos + 1, s + i, i, nxt_st, lim and i == up)
            if not lim:
                f[pos][s][prev][st] = res
            return res

        def calc(x: int) -> int:
            nonlocal num, n, f
            if x < 0:
                return 0
            num = str(x)
            n = len(num)
            f = [
                [[[-1] * 4 for _ in range(10)] for _ in range(9 * n + 1)]
                for _ in range(n)
            ]
            return dfs(0, 0, 0, 0, True)

        return calc(r) - calc(l - 1)
