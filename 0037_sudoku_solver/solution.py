# LeetCode 0037 - Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty: list[tuple[int, int]] = []

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    empty.append((r, c))
                    continue
                box = (r // 3) * 3 + c // 3
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        def backtrack(index: int) -> bool:
            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + c // 3
            for digit in map(str, range(1, 10)):
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    continue

                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

                if backtrack(index + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)

            return False

        backtrack(0)
