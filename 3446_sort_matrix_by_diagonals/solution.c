// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

#include <stdlib.h>

static int cmp_asc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int cmp_desc(const void* a, const void* b) { return *(const int*)b - *(const int*)a; }

int** sortMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int n = gridSize;
    int diagCount = 2 * n - 1;
    int** diags = (int**)malloc(diagCount * sizeof(int*));
    int* dlen = (int*)calloc(diagCount, sizeof(int));
    int* dcap = (int*)calloc(diagCount, sizeof(int));
    for (int i = 0; i < diagCount; i++) { dcap[i] = n; diags[i] = (int*)malloc(n * sizeof(int)); }
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
        int k = i - j + (n - 1);
        diags[k][dlen[k]++] = grid[i][j];
    }
    for (int k = 0; k < diagCount; k++) {
        int key = k - (n - 1);
        if (key >= 0) qsort(diags[k], dlen[k], sizeof(int), cmp_desc);
        else qsort(diags[k], dlen[k], sizeof(int), cmp_asc);
    }
    int* idx = (int*)calloc(diagCount, sizeof(int));
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
        int k = i - j + (n - 1);
        grid[i][j] = diags[k][idx[k]++];
    }
    for (int i = 0; i < diagCount; i++) free(diags[i]);
    free(diags); free(dlen); free(dcap); free(idx);
    *returnSize = n;
    *returnColumnSizes = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) (*returnColumnSizes)[i] = n;
    return grid;
}
