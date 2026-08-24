# LeetCode 3276 - Select Cells in Grid With Maximum Score
# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

from typing import Dict, List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        vals: Dict[int, List[int]] = {}
        for i in range(m):
            seen = set()
            for v in grid[i]:
                if v not in seen:
                    seen.add(v)
                    if v not in vals:
                        vals[v] = []
                    vals[v].append(i)
        arr = sorted(vals.keys(), reverse=True)
        N = 1 << m
        dp = [0] * N
        for v in arr:
            ndp = dp[:]
            for r in vals[v]:
                bit = 1 << r
                for mask in range(N):
                    if (mask & bit) != 0:
                        continue
                    cand = dp[mask] + v
                    nmask = mask | bit
                    if cand > ndp[nmask]:
                        ndp[nmask] = cand
            dp = ndp
        ans = 0
        for x in dp:
            ans = max(ans, x)
        return ans
