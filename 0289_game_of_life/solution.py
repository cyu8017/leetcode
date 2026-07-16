# LeetCode 0289 - Game of Life
# https://leetcode.com/problems/game-of-life/

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] & 1):
                            live_neighbors += 1
                if (board[row][col] & 1) and live_neighbors in (2, 3):
                    board[row][col] |= 2
                elif (board[row][col] & 1) == 0 and live_neighbors == 3:
                    board[row][col] |= 2
        for row in range(rows):
            for col in range(cols):
                board[row][col] >>= 1
