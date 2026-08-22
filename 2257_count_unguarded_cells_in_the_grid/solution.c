// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

#include <stdlib.h>
#include <string.h>

int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize, int** walls, int wallsSize, int* wallsColSize) {
    (void)guardsColSize; (void)wallsColSize;
    int** grid = (int**)malloc((size_t)m * sizeof(int*));
    for (int i = 0; i < m; i++) grid[i] = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < wallsSize; i++) grid[walls[i][0]][walls[i][1]] = 2;
    for (int i = 0; i < guardsSize; i++) grid[guards[i][0]][guards[i][1]] = 2;
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int g = 0; g < guardsSize; g++) {
        for (int d = 0; d < 4; d++) {
            int r = guards[g][0] + dirs[d][0], c = guards[g][1] + dirs[d][1];
            while (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != 2) {
                grid[r][c] = 1;
                r += dirs[d][0];
                c += dirs[d][1];
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) if (grid[i][j] == 0) ans++;
        free(grid[i]);
    }
    free(grid);
    return ans;
}
