// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

#include <stdlib.h>

static int max4(int a, int b, int c, int d) {
    int m = a > b ? a : b;
    if (c > m) m = c;
    if (d > m) m = d;
    return m;
}

static int dpRec(int*** memo, int** grid, int n, int r1, int c1, int c2) {
    int r2 = r1 + c1 - c2;
    if (r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1) {
        return -1000000000;
    }
    if (memo[r1][c1][c2] != -2) {
        return memo[r1][c1][c2];
    }
    if (r1 == n - 1 && c1 == n - 1) {
        return memo[r1][c1][c2] = grid[r1][c1];
    }
    int cherries = grid[r1][c1];
    if (r1 != r2 || c1 != c2) {
        cherries += grid[r2][c2];
    }
    cherries += max4(
        dpRec(memo, grid, n, r1 + 1, c1, c2),
        dpRec(memo, grid, n, r1, c1 + 1, c2),
        dpRec(memo, grid, n, r1 + 1, c1, c2 + 1),
        dpRec(memo, grid, n, r1, c1 + 1, c2 + 1)
    );
    return memo[r1][c1][c2] = cherries;
}

int cherryPickup(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int n = gridSize;
    int*** memo = (int***)malloc((size_t)n * sizeof(int**));
    for (int i = 0; i < n; i++) {
        memo[i] = (int**)malloc((size_t)n * sizeof(int*));
        for (int j = 0; j < n; j++) {
            memo[i][j] = (int*)malloc((size_t)n * sizeof(int));
            for (int k = 0; k < n; k++) {
                memo[i][j][k] = -2;
            }
        }
    }
    int ans = dpRec(memo, grid, n, 0, 0, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            free(memo[i][j]);
        }
        free(memo[i]);
    }
    free(memo);
    return ans > 0 ? ans : 0;
}
