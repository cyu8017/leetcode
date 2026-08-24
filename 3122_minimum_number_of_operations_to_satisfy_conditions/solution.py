# LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 1 << 29
        f = [[INF] * 10 for _ in range(n)]
        for i in range(n):
            cnt = [0] * 10
            for j in range(m):
                cnt[grid[j][i]] += 1
            if i == 0:
                for j in range(10):
                    f[i][j] = m - cnt[j]
            else:
                for j in range(10):
                    for k in range(10):
                        if j != k:
                            f[i][j] = min(f[i][j], f[i - 1][k] + m - cnt[j])
        ans = INF
        for j in range(10):
            ans = min(ans, f[n - 1][j])
        return ans
