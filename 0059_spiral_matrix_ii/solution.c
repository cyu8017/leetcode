// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** generateMatrix(int n, int* returnSize, int** returnColumnSizes) {
    int** matrix = (int**)malloc((size_t)n * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)n * sizeof(int));

    for (int i = 0; i < n; i++) {
        matrix[i] = (int*)calloc((size_t)n, sizeof(int));
        colSizes[i] = n;
    }

    int top = 0;
    int bottom = n - 1;
    int left = 0;
    int right = n - 1;
    int num = 1;

    while (top <= bottom && left <= right) {
        for (int col = left; col <= right; col++) {
            matrix[top][col] = num++;
        }
        top++;

        for (int row = top; row <= bottom; row++) {
            matrix[row][right] = num++;
        }
        right--;

        if (top <= bottom) {
            for (int col = right; col >= left; col--) {
                matrix[bottom][col] = num++;
            }
            bottom--;
        }

        if (left <= right) {
            for (int row = bottom; row >= top; row--) {
                matrix[row][left] = num++;
            }
            left++;
        }
    }

    *returnSize = n;
    *returnColumnSizes = colSizes;
    return matrix;
}
