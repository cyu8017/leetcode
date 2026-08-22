// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

#include <stdbool.h>

static int gm, gn;
static int** ggrid;

static bool dfs2556(int r, int c) {
    if (r == gm - 1 && c == gn - 1) return true;
    if (r >= gm || c >= gn || ggrid[r][c] == 0) return false;
    if (!(r == 0 && c == 0)) ggrid[r][c] = 0;
    return dfs2556(r + 1, c) || dfs2556(r, c + 1);
}

bool isPossibleToCutPath(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    gm = gridSize;
    gn = gridColSize[0];
    ggrid = grid;
    if (!dfs2556(0, 0)) return true;
    grid[0][0] = 1;
    return !dfs2556(0, 0);
}
