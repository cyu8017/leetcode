// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

#include <stdlib.h>

int** restoreMatrix(int* rowSum, int rowSumSize, int* colSum, int colSumSize, int* returnSize, int** returnColumnSizes) {
    int** ans = (int**)malloc((size_t)rowSumSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)rowSumSize * sizeof(int));
    for (int i = 0; i < rowSumSize; i++) {
        ans[i] = (int*)calloc((size_t)colSumSize, sizeof(int));
        (*returnColumnSizes)[i] = colSumSize;
    }
    int i = 0, j = 0;
    while (i < rowSumSize && j < colSumSize) {
        int x = rowSum[i] < colSum[j] ? rowSum[i] : colSum[j];
        ans[i][j] = x;
        rowSum[i] -= x;
        colSum[j] -= x;
        if (rowSum[i] == 0) i++;
        if (colSum[j] == 0) j++;
    }
    *returnSize = rowSumSize;
    return ans;
}
