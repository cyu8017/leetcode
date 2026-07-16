# LeetCode 0348 - Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        add = 1 if player == 1 else -1

        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diag += add
        if row + col == self.n - 1:
            self.anti_diag += add

        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diag) == self.n
            or abs(self.anti_diag) == self.n
        ):
            return player

        return 0
