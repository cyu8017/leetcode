// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

#include <stdlib.h>
#include <string.h>

int countPathsWithXorValue(int** grid, int gridSize, int* gridColSize, int k) {
    const int mod = 1000000007;
    int m = gridSize, n = gridColSize[0];
    int*** dp = (int***)malloc(m * sizeof(int**));
    for (int i = 0; i < m; i++) {
        dp[i] = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; j++) { dp[i][j] = (int*)calloc(16, sizeof(int)); }
    }
    dp[0][0][grid[0][0]] = 1;
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) for (int x = 0; x < 16; x++) {
        if (!dp[i][j][x]) continue;
        if (i + 1 < m) { int nx = x ^ grid[i + 1][j]; dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod; }
        if (j + 1 < n) { int nx = x ^ grid[i][j + 1]; dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod; }
    }
    int ans = dp[m - 1][n - 1][k];
    for (int i = 0; i < m; i++) { for (int j = 0; j < n; j++) free(dp[i][j]); free(dp[i]); }
    free(dp);
    return ans;
}
