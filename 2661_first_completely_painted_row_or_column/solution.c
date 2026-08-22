// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

#include <stdlib.h>

int firstCompleteIndex(int* arr, int arrSize, int** mat, int matSize, int* matColSize) {
    int m = matSize, n = matColSize[0];
    int* posR = (int*)malloc((size_t)(m * n + 1) * sizeof(int));
    int* posC = (int*)malloc((size_t)(m * n + 1) * sizeof(int));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            posR[mat[i][j]] = i;
            posC[mat[i][j]] = j;
        }
    int* rowCnt = (int*)calloc((size_t)m, sizeof(int));
    int* colCnt = (int*)calloc((size_t)n, sizeof(int));
    int ans = -1;
    for (int i = 0; i < arrSize; i++) {
        int r = posR[arr[i]], c = posC[arr[i]];
        rowCnt[r]++;
        colCnt[c]++;
        if (rowCnt[r] == n || colCnt[c] == m) { ans = i; break; }
    }
    free(posR); free(posC); free(rowCnt); free(colCnt);
    return ans;
}
