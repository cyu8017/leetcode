# LeetCode 0130 - Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def mark(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "E"
            mark(r + 1, c)
            mark(r - 1, c)
            mark(r, c + 1)
            mark(r, c - 1)

        for r in range(rows):
            mark(r, 0)
            mark(r, cols - 1)
        for c in range(cols):
            mark(0, c)
            mark(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
