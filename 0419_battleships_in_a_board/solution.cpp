// LeetCode 0419 - Battleships in a Board
// https://leetcode.com/problems/battleships-in-a-board/

#include <vector>

using namespace std;

class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int count = 0;
        int rows = (int)board.size();
        int cols = (int)board[0].size();

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (board[row][col] != 'X') {
                    continue;
                }
                if (row > 0 && board[row - 1][col] == 'X') {
                    continue;
                }
                if (col > 0 && board[row][col - 1] == 'X') {
                    continue;
                }
                ++count;
            }
        }

        return count;
    }
};
