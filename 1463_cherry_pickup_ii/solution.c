// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

#include <stdlib.h>
#include <string.h>

int cherryPickup(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* dp = (int*)malloc(n * n * sizeof(int));
    for (int i = 0; i < n * n; i++) dp[i] = -1;
    dp[0 * n + (n - 1)] = grid[0][0] + (n > 1 ? grid[0][n - 1] : 0);
    for (int r = 1; r < m; r++) {
        int* nxt = (int*)malloc(n * n * sizeof(int));
        for (int i = 0; i < n * n; i++) nxt[i] = -1;
        for (int a = 0; a < n; a++) for (int b = 0; b < n; b++) {
            if (dp[a * n + b] < 0) continue;
            for (int na = a - 1; na <= a + 1; na++)
                for (int nb = b - 1; nb <= b + 1; nb++) {
                    if (na < 0 || na >= n || nb < 0 || nb >= n) continue;
                    int val = dp[a * n + b] + grid[r][na] + (na != nb ? grid[r][nb] : 0);
                    if (val > nxt[na * n + nb]) nxt[na * n + nb] = val;
                }
        }
        free(dp); dp = nxt;
    }
    int ans = 0;
    for (int i = 0; i < n * n; i++) if (dp[i] > ans) ans = dp[i];
    free(dp);
    return ans;
}
