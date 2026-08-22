// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int deleteGreatestValue(int** grid, int gridSize, int* gridColSize) {
    int n = gridColSize[0];
    for (int i = 0; i < gridSize; i++) qsort(grid[i], (size_t)n, sizeof(int), cmp_int);
    int ans = 0;
    for (int c = 0; c < n; c++) {
        int mx = 0;
        for (int r = 0; r < gridSize; r++) if (grid[r][c] > mx) mx = grid[r][c];
        ans += mx;
    }
    return ans;
}
