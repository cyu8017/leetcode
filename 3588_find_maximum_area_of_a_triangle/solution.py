# LeetCode 3588 - Find Maximum Area of a Triangle
# https://leetcode.com/problems/find-maximum-area-of-a-triangle/

from typing import List


def calc3588(coords: List[List[int]]) -> int:
    mn, mx = 10**9, 0
    f = {}
    g = {}
    for c in coords:
        x, y = c[0], c[1]
        mn = min(mn, x)
        mx = max(mx, x)
        if x in f:
            f[x] = min(f[x], y)
            g[x] = max(g[x], y)
        else:
            f[x] = y
            g[x] = y
    ans = 0
    for x, y in f.items():
        d = g[x] - y
        ans = max(ans, d * max(mx - x, x - mn))
    return ans


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        ans = calc3588(coords)
        for c in coords:
            c[0], c[1] = c[1], c[0]
        ans = max(ans, calc3588(coords))
        return ans if ans > 0 else -1
