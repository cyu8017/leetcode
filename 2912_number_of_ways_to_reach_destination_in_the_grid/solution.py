# LeetCode 2912 - Number of Ways to Reach Destination in the Grid
# https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

from typing import List


class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        mod = 1000000007
        sx, sy = source[0], source[1]
        tx, ty = dest[0], dest[1]
        same = row = col = other = 0
        if sx == tx and sy == ty:
            same = 1
        elif sx == tx:
            row = 1
        elif sy == ty:
            col = 1
        else:
            other = 1
        for _ in range(k):
            ns = (row + col) % mod
            nr = (same * (m - 1) + row * (m - 2) + other) % mod
            nc = (same * (n - 1) + col * (n - 2) + other) % mod
            no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4)) % mod
            same, row, col, other = ns, nr, nc, no
        return same
