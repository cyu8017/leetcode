// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    if (matrixSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    int total = matrixSize * matrixColSize[0];
    int* result = (int*)malloc((size_t)total * sizeof(int));
    int index = 0;

    int top = 0;
    int bottom = matrixSize - 1;
    int left = 0;
    int right = matrixColSize[0] - 1;

    while (top <= bottom && left <= right) {
        for (int col = left; col <= right; col++) {
            result[index++] = matrix[top][col];
        }
        top++;

        for (int row = top; row <= bottom; row++) {
            result[index++] = matrix[row][right];
        }
        right--;

        if (top <= bottom) {
            for (int col = right; col >= left; col--) {
                result[index++] = matrix[bottom][col];
            }
            bottom--;
        }

        if (left <= right) {
            for (int row = bottom; row >= top; row--) {
                result[index++] = matrix[row][left];
            }
            left++;
        }
    }

    *returnSize = index;
    return result;
}
