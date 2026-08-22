// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

#include <stdbool.h>

bool satisfiesConditions(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i + 1 < m && grid[i][j] != grid[i + 1][j]) return false;
            if (j + 1 < n && grid[i][j] == grid[i][j + 1]) return false;
        }
    }
    return true;
}
