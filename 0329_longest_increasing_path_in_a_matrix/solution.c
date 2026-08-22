// LeetCode 0329 - Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

#include <stdlib.h>

static int dfs(
    int** matrix,
    int matrixSize,
    int* matrixColSize,
    int** memo,
    int row,
    int col
) {
    if (memo[row][col] != 0) {
        return memo[row][col];
    }
    int best = 1;
    static const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int directionIndex = 0; directionIndex < 4; directionIndex++) {
        int nextRow = row + directions[directionIndex][0];
        int nextCol = col + directions[directionIndex][1];
        if (nextRow >= 0 && nextRow < matrixSize &&
            nextCol >= 0 && nextCol < matrixColSize[0] &&
            matrix[nextRow][nextCol] > matrix[row][col]) {
            int candidate = 1 + dfs(matrix, matrixSize, matrixColSize, memo, nextRow, nextCol);
            if (candidate > best) {
                best = candidate;
            }
        }
    }
    memo[row][col] = best;
    return best;
}

int longestIncreasingPath(int** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || matrixColSize[0] == 0) {
        return 0;
    }
    int cols = matrixColSize[0];
    int** memo = (int**)malloc((size_t)matrixSize * sizeof(int*));
    for (int row = 0; row < matrixSize; row++) {
        memo[row] = (int*)calloc((size_t)cols, sizeof(int));
    }

    int best = 0;
    for (int row = 0; row < matrixSize; row++) {
        for (int col = 0; col < cols; col++) {
            int candidate = dfs(matrix, matrixSize, matrixColSize, memo, row, col);
            if (candidate > best) {
                best = candidate;
            }
        }
    }

    for (int row = 0; row < matrixSize; row++) {
        free(memo[row]);
    }
    free(memo);
    return best;
}
