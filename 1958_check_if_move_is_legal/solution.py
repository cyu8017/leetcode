from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        opp = 'W' if color == 'B' else 'B'
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in dirs:
            r, c = rMove + dr, cMove + dc
            steps = 0
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opp:
                r += dr
                c += dc
                steps += 1
            if steps and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True
        return False
