# LeetCode 0085 - Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            max_area = max(max_area, self._largest_histogram(heights))

        return max_area

    def _largest_histogram(self, heights: List[int]) -> int:
        stack: List[int] = []
        max_area = 0
        extended = heights + [0]

        for i, height in enumerate(extended):
            while stack and extended[stack[-1]] > height:
                h = extended[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        return max_area
