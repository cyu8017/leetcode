// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

#include <stdlib.h>

typedef struct {
    int** prefix;
    int rows;
    int cols;
} NumMatrix;

NumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {
    NumMatrix* obj = (NumMatrix*)malloc(sizeof(NumMatrix));
    obj->rows = matrixSize;
    obj->cols = matrixSize ? matrixColSize[0] : 0;
    obj->prefix = (int**)malloc((size_t)(obj->rows + 1) * sizeof(int*));
    for (int row = 0; row <= obj->rows; row++) {
        obj->prefix[row] = (int*)calloc((size_t)(obj->cols + 1), sizeof(int));
    }
    for (int row = 0; row < obj->rows; row++) {
        for (int col = 0; col < obj->cols; col++) {
            obj->prefix[row + 1][col + 1] = matrix[row][col]
                + obj->prefix[row][col + 1]
                + obj->prefix[row + 1][col]
                - obj->prefix[row][col];
        }
    }
    return obj;
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    int topLeft = obj->prefix[row1][col1];
    int topRight = obj->prefix[row1][col2 + 1];
    int bottomLeft = obj->prefix[row2 + 1][col1];
    int bottomRight = obj->prefix[row2 + 1][col2 + 1];
    return bottomRight - topRight - bottomLeft + topLeft;
}

void numMatrixFree(NumMatrix* obj) {
    if (!obj) {
        return;
    }
    for (int row = 0; row <= obj->rows; row++) {
        free(obj->prefix[row]);
    }
    free(obj->prefix);
    free(obj);
}
