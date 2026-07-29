// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

#include <stdlib.h>

int longestLine(int** mat, int matSize, int* matColSize) {
    if (matSize == 0 || matColSize[0] == 0) {
        return 0;
    }
    int rows = matSize;
    int cols = matColSize[0];
    int*** dp = (int***)malloc((size_t)rows * sizeof(int**));
    for (int r = 0; r < rows; r++) {
        dp[r] = (int**)malloc((size_t)cols * sizeof(int*));
        for (int c = 0; c < cols; c++) {
            dp[r][c] = (int*)calloc(4, sizeof(int));
        }
    }

    int best = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (mat[r][c] == 0) {
                continue;
            }
            dp[r][c][0] = (c > 0 ? dp[r][c - 1][0] : 0) + 1;
            dp[r][c][1] = (r > 0 ? dp[r - 1][c][1] : 0) + 1;
            dp[r][c][2] = (r > 0 && c > 0 ? dp[r - 1][c - 1][2] : 0) + 1;
            dp[r][c][3] = (r > 0 && c + 1 < cols ? dp[r - 1][c + 1][3] : 0) + 1;
            for (int k = 0; k < 4; k++) {
                if (dp[r][c][k] > best) {
                    best = dp[r][c][k];
                }
            }
        }
    }

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            free(dp[r][c]);
        }
        free(dp[r]);
    }
    free(dp);
    return best;
}
