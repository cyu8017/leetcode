// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

public class Solution {
    public void SolveSudoku(char[][] board) {
        var rows = new HashSet<char>[9];
        var cols = new HashSet<char>[9];
        var boxes = new HashSet<char>[9];
        var empty = new List<(int r, int c)>();

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<char>();
            cols[i] = new HashSet<char>();
            boxes[i] = new HashSet<char>();
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char value = board[r][c];
                if (value == '.') {
                    empty.Add((r, c));
                    continue;
                }

                int box = (r / 3) * 3 + c / 3;
                rows[r].Add(value);
                cols[c].Add(value);
                boxes[box].Add(value);
            }
        }

        Backtrack(board, rows, cols, boxes, empty, 0);
    }

    private bool Backtrack(
        char[][] board,
        HashSet<char>[] rows,
        HashSet<char>[] cols,
        HashSet<char>[] boxes,
        List<(int r, int c)> empty,
        int index
    ) {
        if (index == empty.Count) {
            return true;
        }

        var (r, c) = empty[index];
        int box = (r / 3) * 3 + c / 3;

        for (char digit = '1'; digit <= '9'; digit++) {
            if (rows[r].Contains(digit) || cols[c].Contains(digit) || boxes[box].Contains(digit)) {
                continue;
            }

            board[r][c] = digit;
            rows[r].Add(digit);
            cols[c].Add(digit);
            boxes[box].Add(digit);

            if (Backtrack(board, rows, cols, boxes, empty, index + 1)) {
                return true;
            }

            board[r][c] = '.';
            rows[r].Remove(digit);
            cols[c].Remove(digit);
            boxes[box].Remove(digit);
        }

        return false;
    }
}
