// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

#include <string>
#include <vector>

class Solution {
public:
    bool validTicTacToe(std::vector<std::string>& board) {
        std::string flat = board[0] + board[1] + board[2];
        int xCount = 0;
        int oCount = 0;
        for (char ch : flat) {
            if (ch == 'X') {
                ++xCount;
            } else if (ch == 'O') {
                ++oCount;
            }
        }
        if (oCount != xCount && oCount != xCount - 1) {
            return false;
        }
        bool xWin = win(board, 'X');
        bool oWin = win(board, 'O');
        if (xWin && oWin) {
            return false;
        }
        if (xWin && xCount != oCount + 1) {
            return false;
        }
        if (oWin && xCount != oCount) {
            return false;
        }
        return true;
    }

private:
    bool win(const std::vector<std::string>& board, char player) {
        std::string target(3, player);
        for (const std::string& row : board) {
            if (row == target) {
                return true;
            }
        }
        for (int c = 0; c < 3; ++c) {
            if (board[0][c] == player && board[1][c] == player && board[2][c] == player) {
                return true;
            }
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
            return true;
        }
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player) {
            return true;
        }
        return false;
    }
};
