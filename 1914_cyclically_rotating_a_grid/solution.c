// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

#include <stdlib.h>

int** rotateGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    int layers = (m < n ? m : n) / 2;
    for (int layer = 0; layer < layers; layer++) {
        int cap = 2 * (m + n);
        int* vals = (int*)malloc((size_t)cap * sizeof(int));
        int sz = 0;
        for (int c = layer; c < n - layer; c++) vals[sz++] = grid[layer][c];
        for (int r = layer + 1; r < m - layer; r++) vals[sz++] = grid[r][n - layer - 1];
        if (m - 2 * layer > 1) {
            for (int c = n - layer - 2; c >= layer; c--) vals[sz++] = grid[m - layer - 1][c];
        }
        if (n - 2 * layer > 1) {
            for (int r = m - layer - 2; r > layer; r--) vals[sz++] = grid[r][layer];
        }
        int shift = k % sz;
        int* rotated = (int*)malloc((size_t)sz * sizeof(int));
        for (int i = 0; i < sz; i++) rotated[i] = vals[(i + shift) % sz];
        int idx = 0;
        for (int c = layer; c < n - layer; c++) grid[layer][c] = rotated[idx++];
        for (int r = layer + 1; r < m - layer; r++) grid[r][n - layer - 1] = rotated[idx++];
        if (m - 2 * layer > 1) {
            for (int c = n - layer - 2; c >= layer; c--) grid[m - layer - 1][c] = rotated[idx++];
        }
        if (n - 2 * layer > 1) {
            for (int r = m - layer - 2; r > layer; r--) grid[r][layer] = rotated[idx++];
        }
        free(vals);
        free(rotated);
    }
    *returnSize = m;
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) (*returnColumnSizes)[i] = n;
    return grid;
}
