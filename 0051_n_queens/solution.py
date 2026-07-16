# LeetCode 0051 - N-Queens
# https://leetcode.com/problems/n-queens/

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result: List[List[str]] = []
        cols: set[int] = set()
        diag1: set[int] = set()
        diag2: set[int] = set()
        board = ["." * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                result.append(board[:])
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                row_chars = list(board[row])
                row_chars[col] = "Q"
                board[row] = "".join(row_chars)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                board[row] = "." * n

        backtrack(0)
        return result
