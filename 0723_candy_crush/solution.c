// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

#include <stdlib.h>
#include <stdbool.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** candyCrush(int** board, int boardSize, int* boardColSize, int* returnSize, int** returnColumnSizes) {
    int m = boardSize, n = boardColSize[0];
    bool stable = false;
    while (!stable) {
        stable = true;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n - 2; j++) {
                int value = board[i][j] < 0 ? -board[i][j] : board[i][j];
                int a = board[i][j + 1] < 0 ? -board[i][j + 1] : board[i][j + 1];
                int b = board[i][j + 2] < 0 ? -board[i][j + 2] : board[i][j + 2];
                if (value && value == a && value == b) {
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -value;
                    stable = false;
                }
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m - 2; i++) {
                int value = board[i][j] < 0 ? -board[i][j] : board[i][j];
                int a = board[i + 1][j] < 0 ? -board[i + 1][j] : board[i + 1][j];
                int b = board[i + 2][j] < 0 ? -board[i + 2][j] : board[i + 2][j];
                if (value && value == a && value == b) {
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -value;
                    stable = false;
                }
            }
        }
        for (int j = 0; j < n; j++) {
            int write = m - 1;
            for (int i = m - 1; i >= 0; i--) {
                if (board[i][j] > 0) {
                    board[write--][j] = board[i][j];
                }
            }
            for (int i = write; i >= 0; i--) {
                board[i][j] = 0;
            }
        }
    }

    int** result = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        result[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) {
            result[i][j] = board[i][j];
        }
        (*returnColumnSizes)[i] = n;
    }
    *returnSize = m;
    return result;
}
