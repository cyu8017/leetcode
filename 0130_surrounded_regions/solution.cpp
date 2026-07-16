// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

#include <vector>
class Solution {
    void mark(std::vector<std::vector<char>>& board, int row, int col) {
        if (row < 0 || col < 0 || row == (int)board.size() || col == (int)board[0].size() || board[row][col] != 'O') return;
        board[row][col] = 'E'; mark(board, row + 1, col); mark(board, row - 1, col); mark(board, row, col + 1); mark(board, row, col - 1);
    }
public:
    void solve(std::vector<std::vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        int rows = board.size(), cols = board[0].size();
        for (int row = 0; row < rows; ++row) { mark(board, row, 0); mark(board, row, cols - 1); }
        for (int col = 0; col < cols; ++col) { mark(board, 0, col); mark(board, rows - 1, col); }
        for (auto& row : board) for (char& cell : row) cell = cell == 'E' ? 'O' : cell == 'O' ? 'X' : cell;
    }
};