# LeetCode 3193 - Count the Number of Inversions
# https://leetcode.com/problems/count-the-number-of-inversions/

from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        req = [-1] * n
        for r in requirements:
            req[r[0]] = r[1]
        if req[0] > 0:
            return 0
        req[0] = 0
        m = 0
        for v in req:
            m = max(m, v)
        mod = 1000000007
        f = [[0] * (m + 1) for _ in range(n)]
        f[0][0] = 1
        for i in range(1, n):
            l, r = 0, m
            if req[i] >= 0:
                l = r = req[i]
            for j in range(l, r + 1):
                for k in range(min(i, j) + 1):
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
        return f[n - 1][req[n - 1]]
