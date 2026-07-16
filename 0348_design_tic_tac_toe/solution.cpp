// LeetCode 0348 - Design Tic-Tac-Toe
// https://leetcode.com/problems/design-tic-tac-toe/

#include <cstdlib>
#include <vector>

class TicTacToe {
    int n_;
    std::vector<int> rows_;
    std::vector<int> cols_;
    int diag_ = 0;
    int antiDiag_ = 0;

public:
    TicTacToe(int n) : n_(n), rows_(n, 0), cols_(n, 0) {}

    int move(int row, int col, int player) {
        int add = player == 1 ? 1 : -1;

        rows_[row] += add;
        cols_[col] += add;
        if (row == col) {
            diag_ += add;
        }
        if (row + col == n_ - 1) {
            antiDiag_ += add;
        }

        if (std::abs(rows_[row]) == n_
            || std::abs(cols_[col]) == n_
            || std::abs(diag_) == n_
            || std::abs(antiDiag_) == n_) {
            return player;
        }

        return 0;
    }
};
