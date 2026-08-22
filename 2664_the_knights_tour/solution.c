// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

#include <stdlib.h>

static const int dr2664[8] = {1, 1, -1, -1, 2, 2, -2, -2};
static const int dc2664[8] = {2, -2, 2, -2, 1, -1, 1, -1};

static int dfs2664(int** ans, int m, int n, int x, int y, int step) {
    ans[x][y] = step;
    if (step == m * n - 1) return 1;
    for (int d = 0; d < 8; d++) {
        int nx = x + dr2664[d], ny = y + dc2664[d];
        if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1) {
            if (dfs2664(ans, m, n, nx, ny, step + 1)) return 1;
        }
    }
    ans[x][y] = -1;
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** tourOfKnight(int m, int n, int r, int c, int* returnSize, int** returnColumnSizes) {
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)malloc((size_t)n * sizeof(int));
        (*returnColumnSizes)[i] = n;
        for (int j = 0; j < n; j++) ans[i][j] = -1;
    }
    dfs2664(ans, m, n, r, c, 0);
    *returnSize = m;
    return ans;
}
