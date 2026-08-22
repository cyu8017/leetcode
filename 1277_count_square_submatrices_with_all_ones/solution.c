// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

#include <stdlib.h>

int countSquares(int** matrix, int matrixSize, int* matrixColSize) {
    int m = matrixSize, n = matrixColSize[0];
    int ans = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (matrix[r][c] && r && c) {
                int a = matrix[r - 1][c];
                int b = matrix[r][c - 1];
                int d = matrix[r - 1][c - 1];
                int mn = a < b ? a : b;
                if (d < mn) mn = d;
                matrix[r][c] = mn + 1;
            }
            ans += matrix[r][c];
        }
    }
    return ans;
}
