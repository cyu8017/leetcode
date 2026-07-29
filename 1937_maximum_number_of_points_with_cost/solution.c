// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

#include <stdlib.h>

long long maxPoints(int** points, int pointsSize, int* pointsColSize) {
    int m = pointsSize, n = pointsColSize[0];
    long long* dp = (long long*)malloc((size_t)n * sizeof(long long));
    long long* left = (long long*)malloc((size_t)n * sizeof(long long));
    long long* right = (long long*)malloc((size_t)n * sizeof(long long));
    for (int c = 0; c < n; c++) dp[c] = points[0][c];
    for (int r = 1; r < m; r++) {
        left[0] = dp[0];
        for (int c = 1; c < n; c++) {
            long long v = left[c - 1] - 1;
            left[c] = v > dp[c] ? v : dp[c];
        }
        right[n - 1] = dp[n - 1];
        for (int c = n - 2; c >= 0; c--) {
            long long v = right[c + 1] - 1;
            right[c] = v > dp[c] ? v : dp[c];
        }
        for (int c = 0; c < n; c++) {
            long long best = left[c] > right[c] ? left[c] : right[c];
            dp[c] = points[r][c] + best;
        }
    }
    long long ans = dp[0];
    for (int c = 1; c < n; c++) if (dp[c] > ans) ans = dp[c];
    free(dp); free(left); free(right);
    return ans;
}
