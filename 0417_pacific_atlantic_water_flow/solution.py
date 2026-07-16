# LeetCode 0417 - Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        def dfs(row: int, col: int, visited: set[tuple[int, int]], previous: int) -> None:
            if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if heights[row][col] < previous:
                return
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        pacific: set[tuple[int, int]] = set()
        atlantic: set[tuple[int, int]] = set()

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        return [[row, col] for row, col in pacific & atlantic]
