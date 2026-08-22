// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

#include <stdbool.h>
#include <string.h>

static bool dfs(char** board, int boardSize, int* boardColSize, char* word, int row, int col, int index) {
    if (word[index] == '\0') {
        return true;
    }
    if (
        row < 0
        || col < 0
        || row >= boardSize
        || col >= boardColSize[row]
        || board[row][col] != word[index]
    ) {
        return false;
    }

    char temp = board[row][col];
    board[row][col] = '#';

    bool found = dfs(board, boardSize, boardColSize, word, row + 1, col, index + 1)
        || dfs(board, boardSize, boardColSize, word, row - 1, col, index + 1)
        || dfs(board, boardSize, boardColSize, word, row, col + 1, index + 1)
        || dfs(board, boardSize, boardColSize, word, row, col - 1, index + 1);

    board[row][col] = temp;
    return found;
}

bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardColSize[row]; col++) {
            if (dfs(board, boardSize, boardColSize, word, row, col, 0)) {
                return true;
            }
        }
    }

    return false;
}
