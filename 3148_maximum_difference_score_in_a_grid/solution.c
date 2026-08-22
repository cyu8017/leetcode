// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

#include <stdlib.h>

int maxScore(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    const int INF = 1 << 30;
    int* f = malloc(m * n * sizeof(int));
    int ans = -INF;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int mi = INF;
            if (i > 0 && f[(i - 1) * n + j] < mi) mi = f[(i - 1) * n + j];
            if (j > 0 && f[i * n + (j - 1)] < mi) mi = f[i * n + (j - 1)];
            int x = grid[i][j];
            if (x - mi > ans) ans = x - mi;
            f[i * n + j] = x < mi ? x : mi;
        }
    }
    free(f);
    return ans;
}
