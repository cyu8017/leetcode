// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

#include <stdlib.h>
#include <string.h>

int** onesMinusZeros(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    int* row = (int*)calloc((size_t)m, sizeof(int));
    int* col = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            row[i] += grid[i][j];
            col[j] += grid[i][j];
        }
    int** ans = (int**)malloc((size_t)m * sizeof(int*));
    int* cols = (int*)malloc((size_t)m * sizeof(int));
    for (int i = 0; i < m; i++) {
        ans[i] = (int*)malloc((size_t)n * sizeof(int));
        cols[i] = n;
        for (int j = 0; j < n; j++)
            ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j]);
    }
    free(row); free(col);
    *returnSize = m;
    *returnColumnSizes = cols;
    return ans;
}
