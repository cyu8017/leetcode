// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

#include <stdlib.h>
#include <string.h>

int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize) {
    (void)matrixColSize;
    int n = matrixSize;
    int* dp = (int*)malloc((size_t)n * sizeof(int));
    for (int c = 0; c < n; c++) dp[c] = matrix[0][c];
    for (int r = 1; r < n; r++) {
        int* ndp = (int*)malloc((size_t)n * sizeof(int));
        for (int c = 0; c < n; c++) {
            int best = dp[c];
            if (c) best = best < dp[c - 1] ? best : dp[c - 1];
            if (c + 1 < n) best = best < dp[c + 1] ? best : dp[c + 1];
            ndp[c] = matrix[r][c] + best;
        }
        free(dp);
        dp = ndp;
    }
    int ans = dp[0];
    for (int c = 1; c < n; c++) if (dp[c] < ans) ans = dp[c];
    free(dp);
    return ans;
}
