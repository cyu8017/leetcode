// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int m2510, n2510, target2510;
static int** grid2510;
static char* memo2510; /* 0 unset, 1 false, 2 true */
static int maxBal2510;

static bool dfs2510(int r, int c, int bal) {
    if (r >= m2510 || c >= n2510) return false;
    bal += grid2510[r][c];
    if (bal > target2510 || bal + (m2510 - 1 - r) + (n2510 - 1 - c) < target2510) return false;
    if (r == m2510 - 1 && c == n2510 - 1) return bal == target2510;
    int key = (r * n2510 + c) * (maxBal2510 + 1) + bal;
    if (memo2510[key]) return memo2510[key] == 2;
    bool ok = dfs2510(r + 1, c, bal) || dfs2510(r, c + 1, bal);
    memo2510[key] = ok ? 2 : 1;
    return ok;
}

bool isThereAPath(int** grid, int gridSize, int* gridColSize) {
    m2510 = gridSize;
    n2510 = gridColSize[0];
    if ((m2510 + n2510 - 1) % 2 != 0) return false;
    target2510 = (m2510 + n2510 - 1) / 2;
    maxBal2510 = m2510 + n2510;
    grid2510 = grid;
    int cells = m2510 * n2510 * (maxBal2510 + 1);
    memo2510 = (char*)calloc((size_t)cells, 1);
    bool ans = dfs2510(0, 0, 0);
    free(memo2510);
    return ans;
}
