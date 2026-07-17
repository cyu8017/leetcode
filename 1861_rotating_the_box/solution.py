# LeetCode 1861 - Rotating the Box
# https://leetcode.com/problems/rotating-the-box/

from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        rotated = [["."] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                rotated[i][j] = boxGrid[m - 1 - j][i]

        for col in range(m):
            row = n - 1
            for i in range(n - 1, -1, -1):
                if rotated[i][col] == "*":
                    row = i - 1
                elif rotated[i][col] == "#":
                    rotated[i][col] = "."
                    rotated[row][col] = "#"
                    row -= 1

        return rotated
