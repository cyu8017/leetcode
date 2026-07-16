// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

#include <vector>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        bool rows[9][9] = {};
        bool cols[9][9] = {};
        bool boxes[9][9] = {};

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
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
};
