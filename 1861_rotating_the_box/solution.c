// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
char** rotateTheBox(char** boxGrid, int boxGridSize, int* boxGridColSize, int* returnSize,
                    int** returnColumnSizes) {
    int m = boxGridSize;
    int n = boxGridColSize[0];
    char** rotated = (char**)malloc((size_t)n * sizeof(char*));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        rotated[i] = (char*)malloc((size_t)m * sizeof(char));
        (*returnColumnSizes)[i] = m;
        for (int j = 0; j < m; j++) rotated[i][j] = '.';
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            rotated[i][j] = boxGrid[m - 1 - j][i];
        }
    }
    for (int col = 0; col < m; col++) {
        int row = n - 1;
        for (int i = n - 1; i >= 0; i--) {
            if (rotated[i][col] == '*') {
                row = i - 1;
            } else if (rotated[i][col] == '#') {
                rotated[i][col] = '.';
                rotated[row][col] = '#';
                row--;
            }
        }
    }
    *returnSize = n;
    return rotated;
}
