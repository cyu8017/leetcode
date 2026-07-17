# LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        current = mat
        for _ in range(4):
            if current == target:
                return True
            n = len(current)
            current = [[current[n - 1 - row][col] for row in range(n)] for col in range(n)]
        return False
