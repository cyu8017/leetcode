# LeetCode 3776 - Minimum Moves to Balance Circular Array
# https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        total = sum(balance)
        if total < 0:
            return -1
        n = len(balance)
        mn, idx = balance[0], 0
        for i in range(1, n):
            if balance[i] < mn:
                mn = balance[i]
                idx = i
        if mn >= 0:
            return 0
        need = -mn
        ans = 0
        for j in range(1, n):
            a = balance[(idx - j + n) % n]
            b = balance[(idx + j) % n]
            c1 = min(a, need)
            need -= c1
            ans += c1 * j
            c2 = min(b, need)
            need -= c2
            ans += c2 * j
        return ans
