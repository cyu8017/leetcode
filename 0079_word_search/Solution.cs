// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

public class Solution {
    public bool Exist(char[][] board, string word) {
        int rows = board.Length;
        int cols = board[0].Length;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (Dfs(board, word, row, col, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

    private bool Dfs(char[][] board, string word, int row, int col, int index) {
        if (index == word.Length) {
            return true;
        }
        if (
            row < 0
            || col < 0
            || row >= board.Length
            || col >= board[0].Length
            || board[row][col] != word[index]
        ) {
            return false;
        }

        char temp = board[row][col];
        board[row][col] = '#';

        bool found = Dfs(board, word, row + 1, col, index + 1)
            || Dfs(board, word, row - 1, col, index + 1)
            || Dfs(board, word, row, col + 1, index + 1)
            || Dfs(board, word, row, col - 1, index + 1);

        board[row][col] = temp;
        return found;
    }
}
