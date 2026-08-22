// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

#include <stdlib.h>

static int min3(int a, int b, int c) {
    int m = a < b ? a : b;
    return m < c ? m : c;
}

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (!matrix || matrixSize == 0) {
        return 0;
    }
    int cols = matrixColSize[0];
    int* dp = (int*)calloc((size_t)cols + 1, sizeof(int));
    int maxSide = 0;
    int prev = 0;
    for (int row = 1; row <= matrixSize; ++row) {
        for (int col = 1; col <= cols; ++col) {
            int temp = dp[col];
            if (matrix[row - 1][col - 1] == '1') {
                dp[col] = min3(dp[col], dp[col - 1], prev) + 1;
                if (dp[col] > maxSide) {
                    maxSide = dp[col];
                }
            } else {
                dp[col] = 0;
            }
            prev = temp;
        }
    }
    free(dp);
    return maxSide * maxSide;
}
