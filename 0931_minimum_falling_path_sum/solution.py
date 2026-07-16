# LeetCode 0931 - Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = matrix[0][:]
        for r in range(1, len(matrix)):
            ndp = [0] * len(dp)
            for c in range(len(dp)):
                best = dp[c]
                if c:
                    best = min(best, dp[c - 1])
                if c + 1 < len(dp):
                    best = min(best, dp[c + 1])
                ndp[c] = matrix[r][c] + best
            dp = ndp
        return min(dp)
