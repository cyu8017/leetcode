// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

#include <stdlib.h>

static void dfs(int** image, int m, int n, int r, int c, int original, int color) {
    if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != original) {
        return;
    }
    image[r][c] = color;
    dfs(image, m, n, r + 1, c, original, color);
    dfs(image, m, n, r - 1, c, original, color);
    dfs(image, m, n, r, c + 1, original, color);
    dfs(image, m, n, r, c - 1, original, color);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {
    int m = imageSize, n = imageColSize[0];
    int original = image[sr][sc];
    if (original != color) {
        dfs(image, m, n, sr, sc, original, color);
    }
    int** result = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        result[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) {
            result[i][j] = image[i][j];
        }
        (*returnColumnSizes)[i] = n;
    }
    *returnSize = m;
    return result;
}
