// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

#include <string>
#include <vector>

class Solution {
    static int countMines(const std::vector<std::vector<char>>& board, int row, int col) {
        static const int directions[8][2] = {
            {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1},
        };
        int total = 0;
        const int rows = static_cast<int>(board.size());
        const int cols = static_cast<int>(board[0].size());
        for (const auto& direction : directions) {
            const int nextRow = row + direction[0];
            const int nextCol = col + direction[1];
            if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
                board[nextRow][nextCol] == 'M') {
                ++total;
            }
        }
        return total;
    }

    static void reveal(std::vector<std::vector<char>>& board, int row, int col) {
        const int rows = static_cast<int>(board.size());
        const int cols = static_cast<int>(board[0].size());
        if (row < 0 || row >= rows || col < 0 || col >= cols || board[row][col] != 'E') {
            return;
        }
        const int mines = countMines(board, row, col);
        if (mines == 0) {
            board[row][col] = 'B';
            static const int directions[8][2] = {
                {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1},
            };
            for (const auto& direction : directions) {
                reveal(board, row + direction[0], col + direction[1]);
            }
        } else {
            board[row][col] = static_cast<char>('0' + mines);
        }
    }

public:
    std::vector<std::vector<char>> updateBoard(std::vector<std::vector<char>>& board,
                                                std::vector<int>& click) {
        const int row = click[0];
        const int col = click[1];
        if (board[row][col] == 'M') {
            board[row][col] = 'X';
            return board;
        }
        reveal(board, row, col);
        return board;
    }
};
