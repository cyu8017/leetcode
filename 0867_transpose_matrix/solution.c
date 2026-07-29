// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

#include <stdlib.h>

int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    int m = matrixSize, n = matrixColSize[0];
    int** ans = (int**)malloc((size_t)n * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        ans[i] = (int*)malloc((size_t)m * sizeof(int));
        (*returnColumnSizes)[i] = m;
        for (int j = 0; j < m; j++) ans[i][j] = matrix[j][i];
    }
    *returnSize = n;
    return ans;
}
