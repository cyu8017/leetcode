# LeetCode 0562 - Longest Line of Consecutive One in Matrix
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        rows, cols = len(mat), len(mat[0])
        # 0: horizontal, 1: vertical, 2: diagonal, 3: anti-diagonal
        dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
        best = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    continue
                dp[r][c][0] = (dp[r][c - 1][0] if c > 0 else 0) + 1
                dp[r][c][1] = (dp[r - 1][c][1] if r > 0 else 0) + 1
                dp[r][c][2] = (dp[r - 1][c - 1][2] if r > 0 and c > 0 else 0) + 1
                dp[r][c][3] = (dp[r - 1][c + 1][3] if r > 0 and c + 1 < cols else 0) + 1
                best = max(best, max(dp[r][c]))

        return best
