// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

#include <stdlib.h>

static int width(int x) {
    if (x == 0) return 1;
    int w = 0;
    if (x < 0) { w++; x = -x; }
    while (x > 0) { w++; x /= 10; }
    return w;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findColumnWidth(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int n = gridColSize[0];
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < n; j++) {
            int w = width(grid[i][j]);
            if (w > ans[j]) ans[j] = w;
        }
    }
    *returnSize = n;
    return ans;
}
