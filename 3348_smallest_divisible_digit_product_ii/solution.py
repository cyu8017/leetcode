# LeetCode 3348 - Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

from typing import List


def dfs(res: List[str], i: int, tight: bool, sameLen: bool, num: str, t: int) -> bool:
    if i == len(res):
        prod = 1
        for c in res:
            prod *= ord(c) - 48
            if prod == 0:
                break
        return prod % t == 0 and prod > 0
    start = "1" if i == 0 else "0"
    if tight and sameLen and i < len(num):
        start = num[i]
    for cc in range(ord(start), 58):
        c = chr(cc)
        res[i] = c
        nt = tight and sameLen and i < len(num) and c == num[i]
        if dfs(res, i + 1, nt, sameLen, num, t):
            return True
    return False


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        tt = t
        for d in range(9, 1, -1):
            while tt % d == 0:
                tt //= d
        if tt > 1:
            return "-1"
        for extra in range(61):
            L = len(num) + extra
            res = [""] * L
            if dfs(res, 0, True, extra == 0, num, t):
                return "".join(res)
        return "-1"
