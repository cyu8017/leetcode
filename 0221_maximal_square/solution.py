# LeetCode 0221 - Maximal Square
# https://leetcode.com/problems/maximal-square/

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                temp = dp[col]
                if matrix[row - 1][col - 1] == "1":
                    dp[col] = min(dp[col], dp[col - 1], prev) + 1
                    max_side = max(max_side, dp[col])
                else:
                    dp[col] = 0
                prev = temp
        return max_side * max_side
