// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

#include <stdlib.h>

static int dfs(int** grid, int rows, int cols, int r, int c) {
    int gold = grid[r][c];
    grid[r][c] = 0;
    int best = 0;
    const int dr[4] = {1, -1, 0, 0};
    const int dc[4] = {0, 0, 1, -1};
    for (int d = 0; d < 4; d++) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] > 0) {
            int cur = dfs(grid, rows, cols, nr, nc);
            if (cur > best) best = cur;
        }
    }
    grid[r][c] = gold;
    return gold + best;
}

int getMaximumGold(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    int rows = gridSize;
    int cols = gridColSize[0];
    int ans = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] > 0) {
                int cur = dfs(grid, rows, cols, r, c);
                if (cur > ans) ans = cur;
            }
        }
    }
    return ans;
}
