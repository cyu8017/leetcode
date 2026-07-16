# LeetCode 0782 - Transform to Chessboard
# https://leetcode.com/problems/transform-to-chessboard/

from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        row_sum = sum(board[0])
        col_sum = sum(row[0] for row in board)
        if not n // 2 <= row_sum <= (n + 1) // 2:
            return -1
        if not n // 2 <= col_sum <= (n + 1) // 2:
            return -1

        row_swap = sum(board[0][i] != i % 2 for i in range(n))
        col_swap = sum(board[i][0] != i % 2 for i in range(n))
        if n % 2:
            if row_swap % 2:
                row_swap = n - row_swap
            if col_swap % 2:
                col_swap = n - col_swap
        else:
            row_swap = min(row_swap, n - row_swap)
            col_swap = min(col_swap, n - col_swap)
        return (row_swap + col_swap) // 2
