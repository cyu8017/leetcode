// LeetCode 0311 - Sparse Matrix Multiplication
// https://leetcode.com/problems/sparse-matrix-multiplication/

#include <stdlib.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** multiply(
    int** mat1,
    int mat1Size,
    int* mat1ColSize,
    int** mat2,
    int mat2Size,
    int* mat2ColSize,
    int* returnSize,
    int** returnColumnSizes
) {
    (void)mat2Size;
    int rows = mat1Size;
    int inner = mat1ColSize[0];
    int cols = mat2ColSize[0];
    int** result = (int**)malloc((size_t)rows * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)rows * sizeof(int));

    for (int row = 0; row < rows; row++) {
        result[row] = (int*)calloc((size_t)cols, sizeof(int));
        colSizes[row] = cols;
        for (int index = 0; index < inner; index++) {
            if (mat1[row][index] == 0) {
                continue;
            }
            for (int col = 0; col < cols; col++) {
                if (mat2[index][col] != 0) {
                    result[row][col] += mat1[row][index] * mat2[index][col];
                }
            }
        }
    }

    *returnSize = rows;
    *returnColumnSizes = colSizes;
    return result;
}
