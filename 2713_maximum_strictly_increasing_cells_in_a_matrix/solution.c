// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

#include <stdlib.h>
#include <string.h>

typedef struct { int v, r, c; } Cell2713;
static int cmp2713(const void* a, const void* b) {
    return ((const Cell2713*)a)->v - ((const Cell2713*)b)->v;
}

int maxIncreasingCells(int** mat, int matSize, int* matColSize) {
    int m = matSize, n = matColSize[0];
    Cell2713* cells = (Cell2713*)malloc((size_t)m * n * sizeof(Cell2713));
    int cn = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cells[cn++] = (Cell2713){mat[i][j], i, j};
    qsort(cells, (size_t)cn, sizeof(Cell2713), cmp2713);
    int* rowMax = (int*)calloc((size_t)m, sizeof(int));
    int* colMax = (int*)calloc((size_t)n, sizeof(int));
    int ans = 0;
    for (int i = 0; i < cn; ) {
        int j = i;
        while (j < cn && cells[j].v == cells[i].v) j++;
        typedef struct { int r, c, val; } Upd;
        Upd* buf = (Upd*)malloc((size_t)(j - i) * sizeof(Upd));
        int bsz = 0;
        for (int k = i; k < j; k++) {
            int r = cells[k].r, c = cells[k].c;
            int best = rowMax[r];
            if (colMax[c] > best) best = colMax[c];
            int val = best + 1;
            if (val > ans) ans = val;
            buf[bsz++] = (Upd){r, c, val};
        }
        for (int k = 0; k < bsz; k++) {
            if (buf[k].val > rowMax[buf[k].r]) rowMax[buf[k].r] = buf[k].val;
            if (buf[k].val > colMax[buf[k].c]) colMax[buf[k].c] = buf[k].val;
        }
        free(buf);
        i = j;
    }
    free(cells); free(rowMax); free(colMax);
    return ans;
}
