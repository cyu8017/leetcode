// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

#include <stdlib.h>
#include <string.h>

int maxMoves(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* dp = (int*)calloc((size_t)m, sizeof(int));
    for (int c = n - 2; c >= 0; c--) {
        int* ndp = (int*)calloc((size_t)m, sizeof(int));
        for (int r = 0; r < m; r++) {
            int best = 0;
            for (int dr = -1; dr <= 1; dr++) {
                int nr = r + dr;
                if (nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c]) {
                    int cand = 1 + dp[nr];
                    if (cand > best) best = cand;
                }
            }
            ndp[r] = best;
        }
        free(dp);
        dp = ndp;
    }
    int ans = 0;
    for (int i = 0; i < m; i++) if (dp[i] > ans) ans = dp[i];
    free(dp);
    return ans;
}
