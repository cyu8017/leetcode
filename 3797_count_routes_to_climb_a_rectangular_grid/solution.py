# LeetCode 3797 - Count Routes to Climb a Rectangular Grid
# https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

from typing import List


class Solution:
    def countRoutes(self, grid: List[List[str]], d: int) -> int:
        MOD = 1000000007
        n, m = len(grid), len(grid[0])
        upRadius = 0
        while (upRadius + 1) * (upRadius + 1) + 1 <= d * d:
            upRadius += 1
        arrived = [0] * m
        for c in range(m):
            if grid[n - 1][c] == ".":
                arrived[c] = 1
        for r in range(n - 1, -1, -1):
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = (pref[i] + arrived[i]) % MOD
            horizontal = [0] * m
            for c in range(m):
                if grid[r][c] == "#":
                    continue
                l = max(0, c - d)
                rr = min(m - 1, c + d)
                horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % MOD
                if horizontal[c] < 0:
                    horizontal[c] += MOD
            if r == 0:
                ans = 0
                for c in range(m):
                    ans = (ans + arrived[c] + horizontal[c]) % MOD
                return ans
            pref2 = [0] * (m + 1)
            for c in range(m):
                pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % MOD
            nxt = [0] * m
            for c in range(m):
                if grid[r - 1][c] == "#":
                    continue
                l = max(0, c - upRadius)
                rr = min(m - 1, c + upRadius)
                nxt[c] = pref2[rr + 1] - pref2[l]
                if nxt[c] < 0:
                    nxt[c] += MOD
            arrived = nxt
        return 0
