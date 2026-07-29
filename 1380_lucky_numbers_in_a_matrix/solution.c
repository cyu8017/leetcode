// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

#include <stdlib.h>

int* luckyNumbers(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    int m = matrixSize, n = matrixColSize[0];
    int* rowMin = (int*)malloc(m * sizeof(int));
    int* colMax = (int*)malloc(n * sizeof(int));
    for (int c = 0; c < n; c++) colMax[c] = matrix[0][c];
    for (int r = 0; r < m; r++) {
        rowMin[r] = matrix[r][0];
        for (int c = 0; c < n; c++) {
            if (matrix[r][c] < rowMin[r]) rowMin[r] = matrix[r][c];
            if (matrix[r][c] > colMax[c]) colMax[c] = matrix[r][c];
        }
    }
    int* ans = (int*)malloc(m * sizeof(int));
    int an = 0;
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++)
            if (matrix[r][c] == rowMin[r] && matrix[r][c] == colMax[c])
                ans[an++] = matrix[r][c];
    free(rowMin); free(colMax);
    *returnSize = an;
    return ans;
}
