// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool dfs_paren(char** grid, int m, int n, int r, int c, int bal, char* vis, int maxBal) {
    if (r >= m || c >= n) return false;
    if (grid[r][c] == '(') bal++;
    else bal--;
    if (bal < 0) return false;
    if (r == m - 1 && c == n - 1) return bal == 0;
    int idx = ((r * n + c) * (maxBal + 1) + bal);
    if (vis[idx]) return false;
    vis[idx] = 1;
    return dfs_paren(grid, m, n, r + 1, c, bal, vis, maxBal) ||
           dfs_paren(grid, m, n, r, c + 1, bal, vis, maxBal);
}

bool hasValidPath(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    if ((m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;
    int maxBal = m + n;
    char* vis = (char*)calloc((size_t)m * n * (maxBal + 1), 1);
    bool ok = dfs_paren(grid, m, n, 0, 0, 0, vis, maxBal);
    free(vis);
    return ok;
}
