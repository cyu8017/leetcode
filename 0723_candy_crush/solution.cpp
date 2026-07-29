// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> candyCrush(std::vector<std::vector<int>>& board) {
        int m = static_cast<int>(board.size());
        int n = static_cast<int>(board[0].size());
        bool stable = false;
        while (!stable) {
            stable = true;
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n - 2; ++j) {
                    int value = std::abs(board[i][j]);
                    if (value && value == std::abs(board[i][j + 1]) && value == std::abs(board[i][j + 2])) {
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -value;
                        stable = false;
                    }
                }
            }
            for (int j = 0; j < n; ++j) {
                for (int i = 0; i < m - 2; ++i) {
                    int value = std::abs(board[i][j]);
                    if (value && value == std::abs(board[i + 1][j]) && value == std::abs(board[i + 2][j])) {
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -value;
                        stable = false;
                    }
                }
            }
            for (int j = 0; j < n; ++j) {
                int write = m - 1;
                for (int i = m - 1; i >= 0; --i) {
                    if (board[i][j] > 0) {
                        board[write--][j] = board[i][j];
                    }
                }
                for (int i = write; i >= 0; --i) {
                    board[i][j] = 0;
                }
            }
        }
        return board;
    }
};
