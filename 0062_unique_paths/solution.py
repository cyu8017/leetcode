# LeetCode 0062 - Unique Paths
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                row[col] += row[col - 1]

        return row[n - 1]
