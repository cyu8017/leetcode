// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

#include <string>
#include <vector>

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
        int rows = static_cast<int>(board.size());
        int cols = static_cast<int>(board[0].size());

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (dfs(board, word, row, col, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

private:
    bool dfs(
        std::vector<std::vector<char>>& board,
        const std::string& word,
        int row,
        int col,
        int index
    ) {
        if (index == static_cast<int>(word.size())) {
            return true;
        }
        if (
            row < 0
            || col < 0
            || row >= static_cast<int>(board.size())
            || col >= static_cast<int>(board[0].size())
            || board[row][col] != word[index]
        ) {
            return false;
        }

        char temp = board[row][col];
        board[row][col] = '#';

        bool found = dfs(board, word, row + 1, col, index + 1)
            || dfs(board, word, row - 1, col, index + 1)
            || dfs(board, word, row, col + 1, index + 1)
            || dfs(board, word, row, col - 1, index + 1);

        board[row][col] = temp;
        return found;
    }
};
