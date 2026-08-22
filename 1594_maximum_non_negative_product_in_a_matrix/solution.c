// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

#include <stdlib.h>

int maxProductPath(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    long long** high = (long long**)malloc((size_t)m * sizeof(long long*));
    long long** low = (long long**)malloc((size_t)m * sizeof(long long*));
    for (int i = 0; i < m; i++) {
        high[i] = (long long*)malloc((size_t)n * sizeof(long long));
        low[i] = (long long*)malloc((size_t)n * sizeof(long long));
    }
    high[0][0] = low[0][0] = grid[0][0];
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (r == 0 && c == 0) continue;
            long long vals[4];
            int vs = 0;
            if (r) {
                vals[vs++] = high[r - 1][c] * grid[r][c];
                vals[vs++] = low[r - 1][c] * grid[r][c];
            }
            if (c) {
                vals[vs++] = high[r][c - 1] * grid[r][c];
                vals[vs++] = low[r][c - 1] * grid[r][c];
            }
            long long mx = vals[0], mn = vals[0];
            for (int i = 1; i < vs; i++) {
                if (vals[i] > mx) mx = vals[i];
                if (vals[i] < mn) mn = vals[i];
            }
            high[r][c] = mx;
            low[r][c] = mn;
        }
    }
    long long ans = high[m - 1][n - 1];
    for (int i = 0; i < m; i++) { free(high[i]); free(low[i]); }
    free(high); free(low);
    if (ans < 0) return -1;
    return (int)(ans % 1000000007LL);
}
