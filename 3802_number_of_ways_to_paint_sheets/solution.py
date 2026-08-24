# LeetCode 3802 - Number of Ways to Paint Sheets
# https://leetcode.com/problems/number-of-ways-to-paint-sheets/

from typing import List


class Solution:
    def numberOfWays(self, n: int, limit: List[int]) -> int:
        MOD = 1000000007
        limit = sorted(limit)
        points = [1, n]
        for x in limit:
            if x + 1 > 1 and x + 1 < n:
                points.append(x + 1)
            if n - x > 1 and n - x < n:
                points.append(n - x)
        points.sort()
        u = 0
        for i in range(len(points)):
            if u == 0 or points[i] != points[u - 1]:
                points[u] = points[i]
                u += 1
        points = points[:u]

        def countGE(lim: List[int], x: int) -> int:
            lo, hi = 0, len(lim)
            while lo < hi:
                mid = (lo + hi) >> 1
                if lim[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return len(lim) - lo

        ans = 0
        for i in range(len(points) - 1):
            x = points[i]
            a = countGE(limit, x)
            b = countGE(limit, n - x)
            same = countGE(limit, max(x, n - x))
            ways = (a * b - same) % MOD
            length = points[i + 1] - x
            ans = (ans + ways * length) % MOD
        if ans < 0:
            ans += MOD
        return ans
