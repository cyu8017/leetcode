// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {
    int rows = matSize;
    int cols = matColSize[0];
    if (rows * cols != r * c) {
        *returnSize = matSize;
        *returnColumnSizes = (int*)malloc((size_t)matSize * sizeof(int));
        int** result = (int**)malloc((size_t)matSize * sizeof(int*));
        for (int i = 0; i < matSize; i++) {
            (*returnColumnSizes)[i] = cols;
            result[i] = (int*)malloc((size_t)cols * sizeof(int));
            for (int j = 0; j < cols; j++) {
                result[i][j] = mat[i][j];
            }
        }
        return result;
    }

    *returnSize = r;
    *returnColumnSizes = (int*)malloc((size_t)r * sizeof(int));
    int** result = (int**)malloc((size_t)r * sizeof(int*));
    int index = 0;
    for (int i = 0; i < r; i++) {
        (*returnColumnSizes)[i] = c;
        result[i] = (int*)malloc((size_t)c * sizeof(int));
        for (int j = 0; j < c; j++) {
            result[i][j] = mat[index / cols][index % cols];
            index++;
        }
    }
    return result;
}
