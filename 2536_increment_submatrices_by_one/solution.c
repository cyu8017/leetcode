// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

#include <stdlib.h>
#include <string.h>

int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize, int** returnColumnSizes) {
    (void)queriesColSize;
    int** diff = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) diff[i] = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int r1 = queries[qi][0], c1 = queries[qi][1], r2 = queries[qi][2], c2 = queries[qi][3];
        diff[r1][c1]++;
        diff[r1][c2 + 1]--;
        diff[r2 + 1][c1]--;
        diff[r2 + 1][c2 + 1]++;
    }
    int** mat = (int**)malloc((size_t)n * sizeof(int*));
    int* cols = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        mat[i] = (int*)malloc((size_t)n * sizeof(int));
        cols[i] = n;
        for (int j = 0; j < n; j++) {
            int v = diff[i][j];
            if (i > 0) v += mat[i - 1][j];
            if (j > 0) v += mat[i][j - 1];
            if (i > 0 && j > 0) v -= mat[i - 1][j - 1];
            mat[i][j] = v;
        }
    }
    for (int i = 0; i <= n; i++) free(diff[i]);
    free(diff);
    *returnSize = n;
    *returnColumnSizes = cols;
    return mat;
}
