// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

#include <stdbool.h>

bool canPartitionGrid(int** grid, int gridSize, int* gridColSize) {
    long long s = 0;
    int m = gridSize, n = gridColSize[0];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) s += grid[i][j];
    if (s % 2 != 0) return false;
    long long pre = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) pre += grid[i][j];
        if (pre * 2 == s && i + 1 < m) return true;
    }
    pre = 0;
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < m; i++) pre += grid[i][j];
        if (pre * 2 == s && j + 1 < n) return true;
    }
    return false;
}
