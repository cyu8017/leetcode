// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

#include <utility>
#include <vector>

class Solution {
public:
    void solveSudoku(std::vector<std::vector<char>>& board) {
        bool rows[9][9] = {};
        bool cols[9][9] = {};
        bool boxes[9][9] = {};
        std::vector<std::pair<int, int>> empty;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char value = board[r][c];
                if (value == '.') {
                    empty.emplace_back(r, c);
                    continue;
                }

                int digit = value - '1';
                int box = (r / 3) * 3 + c / 3;
                rows[r][digit] = true;
                cols[c][digit] = true;
                boxes[box][digit] = true;
            }
        }

        backtrack(board, empty, 0, rows, cols, boxes);
    }

private:
    bool backtrack(
        std::vector<std::vector<char>>& board,
        const std::vector<std::pair<int, int>>& empty,
        int index,
        bool rows[9][9],
        bool cols[9][9],
        bool boxes[9][9]
    ) {
        if (index == static_cast<int>(empty.size())) {
            return true;
        }

        int r = empty[index].first;
        int c = empty[index].second;
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

            if (backtrack(board, empty, index + 1, rows, cols, boxes)) {
                return true;
            }

            board[r][c] = '.';
            rows[r][d] = false;
            cols[c][d] = false;
            boxes[box][d] = false;
        }

        return false;
    }
};
