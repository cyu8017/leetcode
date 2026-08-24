# LeetCode 3623 - Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i/

from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1000000007
        cnt = {}
        for p in points:
            cnt[p[1]] = cnt.get(p[1], 0) + 1
        ans = 0
        pre = 0
        for c in cnt.values():
            lines = c * (c - 1) // 2
            ans = (ans + pre * lines) % MOD
            pre = (pre + lines) % MOD
        return ans
