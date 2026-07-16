# LeetCode 0794 - Valid Tic-Tac-Toe State
# https://leetcode.com/problems/valid-tic-tac-toe-state/

from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        flat = "".join(board)
        x_count = flat.count("X")
        o_count = flat.count("O")
        if o_count not in {x_count, x_count - 1}:
            return False

        def win(player: str) -> bool:
            lines = board + ["".join(board[r][c] for r in range(3)) for c in range(3)]
            lines.append(board[0][0] + board[1][1] + board[2][2])
            lines.append(board[0][2] + board[1][1] + board[2][0])
            return any(line == player * 3 for line in lines)

        x_win, o_win = win("X"), win("O")
        if x_win and o_win:
            return False
        if x_win and x_count != o_count + 1:
            return False
        if o_win and x_count != o_count:
            return False
        return True
