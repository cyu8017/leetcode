# LeetCode 3933 - Largest Local Values in a Matrix II
# https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

from typing import List


class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        positions: List[List[List[int]]] = [[] for _ in range(201)]
        for row in range(rows):
            for col in range(cols):
                value = matrix[row][col]
                if value > 0:
                    positions[value].append([row, col])
        answer = 0
        for value in range(1, 201):
            if not positions[value]:
                continue
            prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
            for row in range(rows):
                for col in range(cols):
                    add = 1 if matrix[row][col] > value else 0
                    prefix[row + 1][col + 1] = (
                        prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
                    )
            for pos in positions[value]:
                row, col = pos[0], pos[1]
                top = max(0, row - value)
                bottom = min(rows - 1, row + value)
                left = max(0, col - value)
                right = min(cols - 1, col + value)
                greater = (
                    prefix[bottom + 1][right + 1]
                    - prefix[top][right + 1]
                    - prefix[bottom + 1][left]
                    + prefix[top][left]
                )
                for dr in (-value, value):
                    for dc in (-value, value):
                        rr = row + dr
                        cc = col + dc
                        if 0 <= rr < rows and 0 <= cc < cols and matrix[rr][cc] > value:
                            greater -= 1
                if greater == 0:
                    answer += 1
        return answer
