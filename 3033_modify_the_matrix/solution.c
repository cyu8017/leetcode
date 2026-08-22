// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** modifiedMatrix(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    int m = matrixSize, n = matrixColSize[0];
    for (int j = 0; j < n; j++) {
        int mx = -1;
        for (int i = 0; i < m; i++) if (matrix[i][j] > mx) mx = matrix[i][j];
        for (int i = 0; i < m; i++) if (matrix[i][j] == -1) matrix[i][j] = mx;
    }
    *returnSize = m;
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) (*returnColumnSizes)[i] = n;
    return matrix;
}
