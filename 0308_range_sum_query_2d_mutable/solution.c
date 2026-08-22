// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

#include <stdlib.h>

typedef struct {
    int** matrix;
    int rows;
    int cols;
    int** tree;
} NumMatrix;

static void add(NumMatrix* obj, int row, int col, int delta) {
    for (int rowIndex = row; rowIndex <= obj->rows; rowIndex += rowIndex & -rowIndex) {
        for (int colIndex = col; colIndex <= obj->cols; colIndex += colIndex & -colIndex) {
            obj->tree[rowIndex][colIndex] += delta;
        }
    }
}

static int prefix(const NumMatrix* obj, int row, int col) {
    int total = 0;
    for (int rowIndex = row; rowIndex > 0; rowIndex -= rowIndex & -rowIndex) {
        for (int colIndex = col; colIndex > 0; colIndex -= colIndex & -colIndex) {
            total += obj->tree[rowIndex][colIndex];
        }
    }
    return total;
}

NumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {
    NumMatrix* obj = (NumMatrix*)malloc(sizeof(NumMatrix));
    obj->rows = matrixSize;
    obj->cols = matrixSize ? matrixColSize[0] : 0;
    obj->matrix = matrix;
    obj->tree = (int**)malloc((size_t)(obj->rows + 1) * sizeof(int*));
    for (int row = 0; row <= obj->rows; row++) {
        obj->tree[row] = (int*)calloc((size_t)(obj->cols + 1), sizeof(int));
    }
    for (int row = 0; row < obj->rows; row++) {
        for (int col = 0; col < obj->cols; col++) {
            add(obj, row + 1, col + 1, matrix[row][col]);
        }
    }
    return obj;
}

void numMatrixUpdate(NumMatrix* obj, int row, int col, int val) {
    int delta = val - obj->matrix[row][col];
    obj->matrix[row][col] = val;
    add(obj, row + 1, col + 1, delta);
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    return prefix(obj, row2 + 1, col2 + 1) - prefix(obj, row1, col2 + 1)
        - prefix(obj, row2 + 1, col1) + prefix(obj, row1, col1);
}

void numMatrixFree(NumMatrix* obj) {
    if (!obj) {
        return;
    }
    for (int row = 0; row <= obj->rows; row++) {
        free(obj->tree[row]);
    }
    free(obj->tree);
    free(obj);
}
