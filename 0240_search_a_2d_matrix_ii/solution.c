// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    if (matrixSize == 0 || matrixColSize[0] == 0) {
        return false;
    }
    int row = 0;
    int col = matrixColSize[0] - 1;
    while (row < matrixSize && col >= 0) {
        int value = matrix[row][col];
        if (value == target) {
            return true;
        }
        if (value > target) {
            col--;
        } else {
            row++;
        }
    }
    return false;
}
