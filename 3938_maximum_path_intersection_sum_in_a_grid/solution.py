# LeetCode 3938 - Maximum Path Intersection Sum in a Grid
# https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

from typing import Callable, List


def checkLine(length: int, value: Callable[[int], int]) -> int:
    answer = -2147483648
    best_ending = value(0) + value(1)
    if best_ending > answer:
        answer = best_ending
    for i in range(2, length):
        if value(i - 1) + value(i) > best_ending + value(i):
            best_ending = value(i - 1) + value(i)
        else:
            best_ending += value(i)
        if best_ending > answer:
            answer = best_ending
    return answer


class Solution:
    def maxPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        answer = -2147483648
        for row in range(rows):
            r = row
            answer = max(answer, checkLine(cols, lambda col, r=r: grid[r][col]))
        for col in range(cols):
            c = col
            answer = max(answer, checkLine(rows, lambda row, c=c: grid[row][c]))
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] > answer:
                    answer = grid[row][col]
        return answer
