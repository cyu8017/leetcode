// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

#include <stdlib.h>
#include <string.h>

static int min3(int a, int b, int c) {
    int m = a < b ? a : b;
    return m < c ? m : c;
}

static int count2088(int** g, int m, int n) {
    int** dp = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        dp[i] = (int*)malloc((size_t)n * sizeof(int));
        memcpy(dp[i], g[i], (size_t)n * sizeof(int));
    }
    int ans = 0;
    for (int i = m - 2; i >= 0; i--) {
        for (int j = 1; j < n - 1; j++) {
            if (g[i][j] == 1) {
                dp[i][j] = 1 + min3(dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]);
                ans += dp[i][j] - 1;
            }
        }
    }
    for (int i = 0; i < m; i++) free(dp[i]);
    free(dp);
    return ans;
}

int countPyramids(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int ans = count2088(grid, m, n);
    int** rev = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) rev[i] = grid[m - 1 - i];
    ans += count2088(rev, m, n);
    free(rev);
    return ans;
}
