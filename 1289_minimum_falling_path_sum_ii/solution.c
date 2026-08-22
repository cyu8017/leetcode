// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

#include <stdlib.h>

int minFallingPathSum(int** grid, int gridSize, int* gridColSize) {
    int n = gridColSize[0];
    int* dp = (int*)malloc((size_t)n * sizeof(int));
    for (int c = 0; c < n; c++) dp[c] = grid[0][c];
    for (int r = 1; r < gridSize; r++) {
        int first = 0, second = n > 1 ? 1 : 0;
        if (dp[second] < dp[first]) {
            int tmp = first;
            first = second;
            second = tmp;
        }
        for (int c = 0; c < n; c++) {
            if (c == first) continue;
            if (dp[c] < dp[second]) second = c;
        }
        int* ndp = (int*)malloc((size_t)n * sizeof(int));
        for (int c = 0; c < n; c++) {
            ndp[c] = grid[r][c] + (c == first ? dp[second] : dp[first]);
        }
        free(dp);
        dp = ndp;
    }
    int ans = dp[0];
    for (int c = 1; c < n; c++) if (dp[c] < ans) ans = dp[c];
    free(dp);
    return ans;
}
