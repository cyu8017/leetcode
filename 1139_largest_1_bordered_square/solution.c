// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

#include <stdlib.h>

int largest1BorderedSquare(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* left = (int*)calloc((size_t)m * n, sizeof(int));
    int* up = (int*)calloc((size_t)m * n, sizeof(int));
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (!grid[r][c]) continue;
            left[r * n + c] = 1 + (c ? left[r * n + c - 1] : 0);
            up[r * n + c] = 1 + (r ? up[(r - 1) * n + c] : 0);
        }
    }
    int best = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (!grid[r][c]) continue;
            int limit = left[r * n + c] < up[r * n + c] ? left[r * n + c] : up[r * n + c];
            for (int size = limit; size > 0; size--) {
                if (left[(r - size + 1) * n + c] >= size && up[r * n + (c - size + 1)] >= size) {
                    if (size > best) best = size;
                    break;
                }
            }
        }
    }
    free(left); free(up);
    return best * best;
}
