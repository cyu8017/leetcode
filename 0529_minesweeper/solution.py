# LeetCode 0529 - Minesweeper
# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        rows, cols = len(board), len(board[0])
        row, col = click[0], click[1]

        if board[row][col] == "M":
            board[row][col] = "X"
            return board

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def count_mines(r: int, c: int) -> int:
            total = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "M":
                    total += 1
            return total

        def reveal(r: int, c: int) -> None:
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "E":
                return
            mines = count_mines(r, c)
            board[r][c] = "B" if mines == 0 else str(mines)
            if mines == 0:
                for dr, dc in directions:
                    reveal(r + dr, c + dc)

        reveal(row, col)
        return board
