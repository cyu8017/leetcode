// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

#include <stdlib.h>

typedef struct { int val; int i; int j; } Cell;

static int cmpCell(const void* a, const void* b) {
    return ((const Cell*)a)->val - ((const Cell*)b)->val;
}

static int findRoot(int* parent, int x) {
    if (parent[x] != x) parent[x] = findRoot(parent, parent[x]);
    return parent[x];
}

int** matrixRankTransform(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {
    int m = matrixSize, n = matrixColSize[0];
    Cell* cells = (Cell*)malloc((size_t)m * n * sizeof(Cell));
    int idx = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            cells[idx].val = matrix[i][j];
            cells[idx].i = i;
            cells[idx].j = j;
            idx++;
        }
    qsort(cells, (size_t)(m * n), sizeof(Cell), cmpCell);

    int* rank = (int*)calloc((size_t)(m + n), sizeof(int));
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)calloc((size_t)n, sizeof(int));
        (*returnColumnSizes)[i] = n;
    }

    int p = 0;
    while (p < m * n) {
        int q = p;
        while (q < m * n && cells[q].val == cells[p].val) q++;
        int* parent = (int*)malloc((size_t)(m + n) * sizeof(int));
        int* best = (int*)calloc((size_t)(m + n), sizeof(int));
        for (int i = 0; i < m + n; i++) parent[i] = i;
        for (int t = p; t < q; t++) {
            int a = findRoot(parent, cells[t].i);
            int b = findRoot(parent, m + cells[t].j);
            parent[a] = b;
        }
        for (int t = p; t < q; t++) {
            int r = findRoot(parent, cells[t].i);
            int cand = rank[cells[t].i] > rank[m + cells[t].j] ? rank[cells[t].i] : rank[m + cells[t].j];
            if (cand > best[r]) best[r] = cand;
        }
        for (int t = p; t < q; t++) {
            int r = findRoot(parent, cells[t].i) ;
            ans[cells[t].i][cells[t].j] = best[r] + 1;
        }
        for (int t = p; t < q; t++) {
            int v = ans[cells[t].i][cells[t].j];
            if (v > rank[cells[t].i]) rank[cells[t].i] = v;
            if (v > rank[m + cells[t].j]) rank[m + cells[t].j] = v;
        }
        free(parent); free(best);
        p = q;
    }
    free(cells); free(rank);
    *returnSize = m;
    return ans;
}
