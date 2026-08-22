// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

#include <stdlib.h>

int maxConsistentColumns(int** grid, int gridSize, int* gridColSize, int limit) {
    int m = gridSize, n = gridColSize[0];
    int* dp = (int*)malloc((size_t)n * sizeof(int));
    int ans = 1;
    for (int j = 0; j < n; j++) {
        dp[j] = 1;
        for (int i = 0; i < j; i++) {
            if (dp[i] + 1 <= dp[j]) continue;
            int ok = 1;
            for (int r = 0; r < m; r++) {
                int d = grid[r][j] - grid[r][i];
                if (d < 0) d = -d;
                if (d > limit) { ok = 0; break; }
            }
            if (ok) dp[j] = dp[i] + 1;
        }
        if (dp[j] > ans) ans = dp[j];
    }
    free(dp);
    return ans;
}
