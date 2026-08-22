// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

#include <stdlib.h>
#include <string.h>

static int dfs_paths(int r, int c, int** grid, int m, int n, int** dp) {
    const int mod = 1000000007;
    if (dp[r][c] != 0) return dp[r][c];
    int res = 1;
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int i = 0; i < 4; i++) {
        int nr = r + dirs[i][0], nc = c + dirs[i][1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c]) {
            res = (res + dfs_paths(nr, nc, grid, m, n, dp)) % mod;
        }
    }
    dp[r][c] = res;
    return res;
}

int countPaths(int** grid, int gridSize, int* gridColSize) {
    const int mod = 1000000007;
    int m = gridSize, n = gridColSize[0];
    int** dp = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) dp[i] = (int*)calloc((size_t)n, sizeof(int));
    int ans = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            ans = (ans + dfs_paths(i, j, grid, m, n, dp)) % mod;
        }
    }
    for (int i = 0; i < m; i++) free(dp[i]);
    free(dp);
    return ans;
}
