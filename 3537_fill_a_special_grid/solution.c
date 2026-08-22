// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

#include <stdlib.h>

static int** ans3537;
static int val3537;

static void dfs3537(int x, int y, int k) {
    if (k == 1) {
        ans3537[x][y] = val3537++;
        return;
    }
    int h = k / 2;
    dfs3537(x, y, h);
    dfs3537(x + h, y, h);
    dfs3537(x + h, y - h, h);
    dfs3537(x, y - h, h);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** specialGrid(int n, int* returnSize, int** returnColumnSizes) {
    int m = 1 << n;
    ans3537 = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans3537[i] = (int*)calloc((size_t)m, sizeof(int));
        (*returnColumnSizes)[i] = m;
    }
    val3537 = 0;
    dfs3537(0, m - 1, m);
    *returnSize = m;
    return ans3537;
}
