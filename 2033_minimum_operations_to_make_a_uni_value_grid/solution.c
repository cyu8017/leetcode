// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minOperations(int** grid, int gridSize, int* gridColSize, int x) {
    int m = gridSize, n = gridColSize[0];
    int* vals = (int*)malloc((size_t)m * n * sizeof(int));
    int vn = 0;
    int base = grid[0][0] % x;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] % x != base) { free(vals); return -1; }
            vals[vn++] = grid[i][j];
        }
    }
    qsort(vals, (size_t)vn, sizeof(int), cmpInt);
    int median = vals[vn / 2], ans = 0;
    for (int i = 0; i < vn; i++) {
        int diff = vals[i] - median;
        if (diff < 0) diff = -diff;
        ans += diff / x;
    }
    free(vals);
    return ans;
}
