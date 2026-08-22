// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

#include <stdlib.h>
#include <string.h>

int minPathCost(int** grid, int gridSize, int* gridColSize, int** moveCost, int moveCostSize, int* moveCostColSize) {
    (void)moveCostSize; (void)moveCostColSize;
    int m = gridSize, n = gridColSize[0];
    int* dp = (int*)malloc((size_t)n * sizeof(int));
    memcpy(dp, grid[0], (size_t)n * sizeof(int));
    for (int r = 0; r < m - 1; r++) {
        int* next = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) next[j] = 1 << 30;
        for (int c = 0; c < n; c++) {
            int from = grid[r][c];
            for (int nc = 0; nc < n; nc++) {
                int cost = dp[c] + moveCost[from][nc] + grid[r + 1][nc];
                if (cost < next[nc]) next[nc] = cost;
            }
        }
        free(dp);
        dp = next;
    }
    int ans = dp[0];
    for (int i = 1; i < n; i++) if (dp[i] < ans) ans = dp[i];
    free(dp);
    return ans;
}
