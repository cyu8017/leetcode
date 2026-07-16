# LeetCode 0063 - Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        row = [0] * cols
        row[0] = 1

        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                row[0] = 0

            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else:
                    row[j] += row[j - 1]

        return row[cols - 1]
