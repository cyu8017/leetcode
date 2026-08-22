// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int row = 0;
    int col = matrixColSize[0] - 1;

    while (row < matrixSize && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        }
        if (matrix[row][col] > target) {
            col--;
        } else {
            row++;
        }
    }

    return false;
}
