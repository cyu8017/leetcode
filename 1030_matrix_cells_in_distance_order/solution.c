// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

#include <stdlib.h>

typedef struct { int r, c, d; } Cell;

static int cmp_cell(const void* a, const void* b) {
    return ((const Cell*)a)->d - ((const Cell*)b)->d;
}

int** allCellsDistOrder(int rows, int cols, int rCenter, int cCenter,
                        int* returnSize, int** returnColumnSizes) {
    int total = rows * cols;
    Cell* cells = (Cell*)malloc((size_t)total * sizeof(Cell));
    int idx = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            cells[idx].r = r;
            cells[idx].c = c;
            int dr = r - rCenter; if (dr < 0) dr = -dr;
            int dc = c - cCenter; if (dc < 0) dc = -dc;
            cells[idx].d = dr + dc;
            idx++;
        }
    }
    qsort(cells, (size_t)total, sizeof(Cell), cmp_cell);
    int** ans = (int**)malloc((size_t)total * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)total * sizeof(int));
    for (int i = 0; i < total; i++) {
        ans[i] = (int*)malloc(2 * sizeof(int));
        ans[i][0] = cells[i].r;
        ans[i][1] = cells[i].c;
        (*returnColumnSizes)[i] = 2;
    }
    *returnSize = total;
    free(cells);
    return ans;
}
