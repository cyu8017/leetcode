from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            board[r][c] = 1 if i % 2 == 0 else -1
        lines = board + [list(col) for col in zip(*board)]
        lines += [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
        for line in lines:
            if abs(sum(line)) == 3:
                return "A" if sum(line) == 3 else "B"
        return "Draw" if len(moves) == 9 else "Pending"
