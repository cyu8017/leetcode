# LeetCode 0723 - Candy Crush
# https://leetcode.com/problems/candy-crush/

from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        stable = False
        while not stable:
            stable = True
            for i in range(m):
                for j in range(n - 2):
                    value = abs(board[i][j])
                    if (
                        value
                        and value == abs(board[i][j + 1]) == abs(board[i][j + 2])
                    ):
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -value
                        stable = False
            for j in range(n):
                for i in range(m - 2):
                    value = abs(board[i][j])
                    if (
                        value
                        and value == abs(board[i + 1][j]) == abs(board[i + 2][j])
                    ):
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -value
                        stable = False

            for j in range(n):
                write = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[write][j] = board[i][j]
                        write -= 1
                for i in range(write, -1, -1):
                    board[i][j] = 0
        return board
