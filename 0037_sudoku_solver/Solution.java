// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

class Solution {
    private boolean[][] rows = new boolean[9][9];
    private boolean[][] cols = new boolean[9][9];
    private boolean[][] boxes = new boolean[9][9];
    private int[][] empty = new int[81][2];
    private int emptyCount;

    public void solveSudoku(char[][] board) {
        emptyCount = 0;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char value = board[r][c];
                if (value == '.') {
                    empty[emptyCount][0] = r;
                    empty[emptyCount][1] = c;
                    emptyCount++;
                    continue;
                }

                int digit = value - '1';
                int box = (r / 3) * 3 + c / 3;
                rows[r][digit] = true;
                cols[c][digit] = true;
                boxes[box][digit] = true;
            }
        }

        backtrack(board, 0);
    }

    private boolean backtrack(char[][] board, int index) {
        if (index == emptyCount) {
            return true;
        }

        int r = empty[index][0];
        int c = empty[index][1];
        int box = (r / 3) * 3 + c / 3;

        for (char digit = '1'; digit <= '9'; digit++) {
            int d = digit - '1';
            if (rows[r][d] || cols[c][d] || boxes[box][d]) {
                continue;
            }

            board[r][c] = digit;
            rows[r][d] = true;
            cols[c][d] = true;
            boxes[box][d] = true;

            if (backtrack(board, index + 1)) {
                return true;
            }

            board[r][c] = '.';
            rows[r][d] = false;
            cols[c][d] = false;
            boxes[box][d] = false;
        }

        return false;
    }
}
