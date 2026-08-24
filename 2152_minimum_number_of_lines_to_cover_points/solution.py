# LeetCode 2152 - Minimum Number of Lines to Cover Points
# https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

from typing import List
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return 1
        colinear = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
        inf = n
        dp = [inf] * (1 << n)
        dp[0] = 0
        for mask in range((1 << n)):
            if dp[mask] == inf:
                continue
            i = 0
            while i < n and (mask & (1 << i)) != 0:
                i += 1
            if i == n:
                continue
            nm = mask | (1 << i)
            dp[nm] = min(dp[nm], dp[mask] + 1)
            for j in range(i + 1, n):
                if (mask & (1 << j)) != 0:
                    continue
                nm = mask | (1 << i) | (1 << j)
                for k in range(n):
                    if (nm & (1 << k)) == 0 and colinear(points[i], points[j], points[k]):
                        nm |= 1 << k
                dp[nm] = min(dp[nm], dp[mask] + 1)
        return dp[(1 << n) - 1]
