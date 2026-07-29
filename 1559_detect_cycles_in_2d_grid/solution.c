// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

#include <stdlib.h>
#include <stdbool.h>

static bool dfs1559(char** grid, int m, int n, int r, int c, int pr, int pc, char** seen) {
    seen[r][c] = 1;
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int d = 0; d < 4; d++) {
        int nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
        if (grid[nr][nc] != grid[r][c]) continue;
        if (nr == pr && nc == pc) continue;
        if (seen[nr][nc] || dfs1559(grid, m, n, nr, nc, r, c, seen)) return true;
    }
    return false;
}

bool containsCycle(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    char** seen = (char**)malloc((size_t)m * sizeof(char*));
    for (int i = 0; i < m; i++) seen[i] = (char*)calloc((size_t)n, 1);
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (!seen[r][c] && dfs1559(grid, m, n, r, c, -1, -1, seen)) {
                for (int i = 0; i < m; i++) free(seen[i]);
                free(seen);
                return true;
            }
        }
    }
    for (int i = 0; i < m; i++) free(seen[i]);
    free(seen);
    return false;
}
