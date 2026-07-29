// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int** diagonalSort(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes) {
    int m = matSize, n = matColSize[0];
    int diagCount = m + n;
    int** diags = (int**)malloc(diagCount * sizeof(int*));
    int* dsize = (int*)calloc(diagCount, sizeof(int));
    int* dcap = (int*)calloc(diagCount, sizeof(int));
    for (int i = 0; i < diagCount; i++) { dcap[i] = 8; diags[i] = (int*)malloc(8 * sizeof(int)); }
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++) {
            int id = r - c + n;
            if (dsize[id] == dcap[id]) { dcap[id] *= 2; diags[id] = (int*)realloc(diags[id], dcap[id] * sizeof(int)); }
            diags[id][dsize[id]++] = mat[r][c];
        }
    for (int i = 0; i < diagCount; i++) qsort(diags[i], dsize[i], sizeof(int), cmp_int);
    int* idx = (int*)calloc(diagCount, sizeof(int));
    int** ans = (int**)malloc(m * sizeof(int*));
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int r = 0; r < m; r++) {
        ans[r] = (int*)malloc(n * sizeof(int));
        (*returnColumnSizes)[r] = n;
        for (int c = 0; c < n; c++) {
            int id = r - c + n;
            ans[r][c] = diags[id][idx[id]++];
        }
    }
    for (int i = 0; i < diagCount; i++) free(diags[i]);
    free(diags); free(dsize); free(dcap); free(idx);
    *returnSize = m;
    return ans;
}
