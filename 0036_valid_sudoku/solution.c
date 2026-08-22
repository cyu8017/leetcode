// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

#include <stdbool.h>

bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    bool rows[9][9] = {false};
    bool cols[9][9] = {false};
    bool boxes[9][9] = {false};

    for (int r = 0; r < boardSize; r++) {
        for (int c = 0; c < boardColSize[r]; c++) {
            char value = board[r][c];
            if (value == '.') {
                continue;
            }

            int digit = value - '1';
            int box = (r / 3) * 3 + c / 3;
            if (rows[r][digit] || cols[c][digit] || boxes[box][digit]) {
                return false;
            }

            rows[r][digit] = true;
            cols[c][digit] = true;
            boxes[box][digit] = true;
        }
    }

    return true;
}
