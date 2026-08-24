# LeetCode 2055 - Plates Between Candles
# https://leetcode.com/problems/plates-between-candles/

from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pref = [0] * (n + 1)
        left = [0] * n
        right = [0] * n
        last = -1
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (1 if ch == "*" else 0)
            if ch == "|":
                last = i
            left[i] = last
        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                last = i
            right[i] = last
        ans = [0] * len(queries)
        for i, (ql, qr) in enumerate(queries):
            l, r = right[ql], left[qr]
            if l != -1 and r != -1 and l < r:
                ans[i] = pref[r] - pref[l]
        return ans
