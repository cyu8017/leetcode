// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

#include <stdlib.h>

int countServers(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    int* rows = (int*)calloc((size_t)m, sizeof(int));
    int* cols = (int*)calloc((size_t)n, sizeof(int));
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c]) {
                rows[r]++;
                cols[c]++;
            }
        }
    }
    int ans = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] && (rows[r] > 1 || cols[c] > 1)) ans++;
        }
    }
    free(rows);
    free(cols);
    return ans;
}
