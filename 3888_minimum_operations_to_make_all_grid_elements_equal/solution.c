// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

#include <stdlib.h>
#include <string.h>

static long long check3888(int** grid, int m, int n, int k, int target) {
    long long** diff = malloc((size_t)(m + 2) * sizeof(long long*));
    for (int i = 0; i < m + 2; i++) diff[i] = calloc((size_t)(n + 2), sizeof(long long));
    long long totalOps = 0;
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
            long long curVal = (long long)grid[i - 1][j - 1] + diff[i][j];
            if (curVal > target) {
                for (int x = 0; x < m + 2; x++) free(diff[x]);
                free(diff);
                return -1;
            }
            if (curVal < target) {
                if (i + k - 1 > m || j + k - 1 > n) {
                    for (int x = 0; x < m + 2; x++) free(diff[x]);
                    free(diff);
                    return -1;
                }
                long long needed = (long long)target - curVal;
                totalOps += needed;
                diff[i][j] += needed;
                diff[i + k][j] -= needed;
                diff[i][j + k] -= needed;
                diff[i + k][j + k] += needed;
            }
        }
    }
    for (int x = 0; x < m + 2; x++) free(diff[x]);
    free(diff);
    return totalOps;
}

long long minOperations(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize, n = gridColSize[0];
    int maxVal = grid[0][0];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (grid[i][j] > maxVal) maxVal = grid[i][j];
    for (int t = maxVal; t <= maxVal + 1; t++) {
        long long res = check3888(grid, m, n, k, t);
        if (res != -1) return res;
    }
    return -1;
}
