// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

#include <stdlib.h>

int** largestLocal(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    (void)gridColSize;
    int n = gridSize;
    int** ans = (int**)malloc((size_t)(n - 2) * sizeof(int*));
    int* cols = (int*)malloc((size_t)(n - 2) * sizeof(int));
    for (int i = 0; i < n - 2; i++) {
        ans[i] = (int*)malloc((size_t)(n - 2) * sizeof(int));
        cols[i] = n - 2;
        for (int j = 0; j < n - 2; j++) {
            int mx = 0;
            for (int r = i; r < i + 3; r++)
                for (int c = j; c < j + 3; c++)
                    if (grid[r][c] > mx) mx = grid[r][c];
            ans[i][j] = mx;
        }
    }
    *returnSize = n - 2; *returnColumnSizes = cols;
    return ans;
}
