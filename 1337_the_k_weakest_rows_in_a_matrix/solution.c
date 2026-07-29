// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

#include <stdlib.h>

typedef struct { int soldiers, idx; } Row;

static int cmp_row(const void* a, const void* b) {
    const Row* x = (const Row*)a;
    const Row* y = (const Row*)b;
    if (x->soldiers != y->soldiers) return x->soldiers - y->soldiers;
    return x->idx - y->idx;
}

int* kWeakestRows(int** mat, int matSize, int* matColSize, int k, int* returnSize) {
    Row* rows = (Row*)malloc(matSize * sizeof(Row));
    for (int i = 0; i < matSize; i++) {
        int s = 0;
        for (int j = 0; j < matColSize[i]; j++) s += mat[i][j];
        rows[i].soldiers = s;
        rows[i].idx = i;
    }
    qsort(rows, matSize, sizeof(Row), cmp_row);
    int* ans = (int*)malloc(k * sizeof(int));
    for (int i = 0; i < k; i++) ans[i] = rows[i].idx;
    free(rows);
    *returnSize = k;
    return ans;
}
