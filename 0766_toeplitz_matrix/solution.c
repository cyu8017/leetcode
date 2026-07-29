// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

#include <stdbool.h>

bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize) {
    for (int r = 1; r < matrixSize; r++) {
        for (int c = 1; c < matrixColSize[0]; c++) {
            if (matrix[r][c] != matrix[r - 1][c - 1]) return false;
        }
    }
    return true;
}
