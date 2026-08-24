# LeetCode 3363 - Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
        neg = -(1 << 30)
        dp2 = [[neg] * n for _ in range(n)]
        dp3 = [[neg] * n for _ in range(n)]
        dp2[0][n - 1] = fruits[0][n - 1]
        for i in range(n):
            for j in range(n):
                if dp2[i][j] == neg:
                    continue
                for dj in (-1, 0, 1):
                    ni, nj = i + 1, j + dj
                    if ni < n and 0 <= nj < n and nj > ni:
                        v = dp2[i][j] + fruits[ni][nj]
                        if v > dp2[ni][nj]:
                            dp2[ni][nj] = v
        dp3[n - 1][0] = fruits[n - 1][0]
        for j in range(n):
            for i in range(n):
                if dp3[i][j] == neg:
                    continue
                for di in (-1, 0, 1):
                    ni, nj = i + di, j + 1
                    if 0 <= ni < n and nj < n and ni > nj:
                        v = dp3[i][j] + fruits[ni][nj]
                        if v > dp3[ni][nj]:
                            dp3[ni][nj] = v
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
        return ans
