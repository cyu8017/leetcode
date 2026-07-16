from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        best = 0
        for r in range(m):
            for c in range(n):
                heights[c] = heights[c] + 1 if matrix[r][c] else 0
            for width, height in enumerate(sorted(heights, reverse=True), 1):
                best = max(best, width * height)
        return best
