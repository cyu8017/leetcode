// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

#include <stdlib.h>

typedef struct { int v, r, c; } Cell;
static int cmpCell(const void* a, const void* b) { return ((const Cell*)a)->v - ((const Cell*)b)->v; }

int** minScore(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    Cell* arr = (Cell*)malloc((size_t)m * n * sizeof(Cell));
    int idx = 0;
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) arr[idx++] = (Cell){grid[i][j], i, j};
    qsort(arr, (size_t)(m * n), sizeof(Cell), cmpCell);
    int* rowMax = (int*)calloc((size_t)m, sizeof(int));
    int* colMax = (int*)calloc((size_t)n, sizeof(int));
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    int* cols = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) { ans[i] = (int*)calloc((size_t)n, sizeof(int)); cols[i] = n; }
    for (int t = 0; t < m * n; t++) {
        int val = rowMax[arr[t].r];
        if (colMax[arr[t].c] > val) val = colMax[arr[t].c];
        val++;
        ans[arr[t].r][arr[t].c] = val;
        rowMax[arr[t].r] = val;
        colMax[arr[t].c] = val;
    }
    free(arr); free(rowMax); free(colMax);
    *returnSize = m; *returnColumnSizes = cols;
    return ans;
}
