// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

#include <stdbool.h>

static bool backtrack(
    char** board,
    int (*empty)[2],
    int emptyCount,
    int index,
    bool rows[9][9],
    bool cols[9][9],
    bool boxes[9][9]
) {
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

        if (backtrack(board, empty, emptyCount, index + 1, rows, cols, boxes)) {
            return true;
        }

        board[r][c] = '.';
        rows[r][d] = false;
        cols[c][d] = false;
        boxes[box][d] = false;
    }

    return false;
}

void solveSudoku(char** board, int boardSize, int* boardColSize) {
    bool rows[9][9] = {false};
    bool cols[9][9] = {false};
    bool boxes[9][9] = {false};
    int empty[81][2];
    int emptyCount = 0;

    for (int r = 0; r < boardSize; r++) {
        for (int c = 0; c < boardColSize[r]; c++) {
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

    backtrack(board, empty, emptyCount, 0, rows, cols, boxes);
}
