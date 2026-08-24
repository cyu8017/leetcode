# LeetCode 3519 - Count Numbers with Non-Decreasing Digits
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

from typing import List

MOD = 1000000007


def toDigits(s: str, b: int) -> List[int]:
    if s == "0":
        return [0]
    digs = []
    while not (len(s) == 1 and s[0] == "0"):
        rem = 0
        q = ""
        for c in s:
            cur = rem * 10 + (ord(c) - 48)
            d = cur // b
            rem = cur % b
            if len(q) > 0 or d != 0:
                q += str(d)
        digs.append(rem)
        s = "0" if len(q) == 0 else q
    digs.reverse()
    return digs


def dec(s: str) -> str:
    a = list(s)
    i = len(a) - 1
    while i >= 0 and a[i] == "0":
        a[i] = "9"
        i -= 1
    if i < 0:
        return "0"
    a[i] = str(ord(a[i]) - 49)
    t = "".join(a)
    p = 0
    while p + 1 < len(t) and t[p] == "0":
        p += 1
    return t[p:]


def countUpto(digs: List[int], b: int) -> int:
    m = len(digs)
    memo = {}

    def dfs(pos: int, last: int, tight: bool) -> int:
        if pos == m:
            return 1
        key = (pos, last, 1 if tight else 0)
        if key in memo:
            return memo[key]
        up = digs[pos] if tight else b - 1
        res = 0
        for d in range(last, up + 1):
            res = (res + dfs(pos + 1, d, tight and d == up)) % MOD
        memo[key] = res
        return res

    return dfs(0, 0, True)


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        rd = toDigits(r, b)
        ld = toDigits(dec(l), b)
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD
