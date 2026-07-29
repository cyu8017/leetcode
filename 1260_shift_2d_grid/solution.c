// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

#include <stdlib.h>

int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    int total = m * n;
    k %= total;
    int* flat = (int*)malloc((size_t)total * sizeof(int));
    for (int i = 0; i < total; i++) flat[i] = grid[i / n][i % n];
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int r = 0; r < m; r++) {
        ans[r] = (int*)malloc((size_t)n * sizeof(int));
        (*returnColumnSizes)[r] = n;
        for (int c = 0; c < n; c++) {
            int idx = (r * n + c - k + total) % total;
            ans[r][c] = flat[idx];
        }
    }
    free(flat);
    *returnSize = m;
    return ans;
}
