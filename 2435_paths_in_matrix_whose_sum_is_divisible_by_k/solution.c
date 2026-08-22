// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

#include <stdlib.h>
#include <string.h>

int numberOfPaths(int** grid, int gridSize, int* gridColSize, int k) {
    const int mod = 1000000007;
    int m = gridSize, n = gridColSize[0];
    int*** dp = (int***)malloc((size_t)m * sizeof(int**));
    for (int i = 0; i < m; i++) {
        dp[i] = (int**)malloc((size_t)n * sizeof(int*));
        for (int j = 0; j < n; j++) dp[i][j] = (int*)calloc((size_t)k, sizeof(int));
    }
    dp[0][0][grid[0][0] % k] = 1;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int r = 0; r < k; r++) {
                if (!dp[i][j][r]) continue;
                if (i + 1 < m) {
                    int nr = (r + grid[i + 1][j]) % k;
                    dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod;
                }
                if (j + 1 < n) {
                    int nr = (r + grid[i][j + 1]) % k;
                    dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod;
                }
            }
        }
    }
    int ans = dp[m - 1][n - 1][0];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) free(dp[i][j]);
        free(dp[i]);
    }
    free(dp);
    return ans;
}
