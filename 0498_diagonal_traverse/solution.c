// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

#include <stdlib.h>

int* findDiagonalOrder(int** mat, int matSize, int* matColSize, int* returnSize) {
    if (matSize == 0 || matColSize[0] == 0) {
        *returnSize = 0;
        return NULL;
    }
    const int rows = matSize;
    const int cols = matColSize[0];
    int* result = (int*)malloc((size_t)(rows * cols) * sizeof(int));
    int row = 0;
    int col = 0;
    int upward = 1;
    int index = 0;

    while (index < rows * cols) {
        result[index++] = mat[row][col];
        if (upward) {
            if (col == cols - 1) {
                row++;
                upward = 0;
            } else if (row == 0) {
                col++;
                upward = 0;
            } else {
                row--;
                col++;
            }
        } else {
            if (row == rows - 1) {
                col++;
                upward = 1;
            } else if (col == 0) {
                row++;
                upward = 1;
            } else {
                row++;
                col--;
            }
        }
    }
    *returnSize = rows * cols;
    return result;
}
