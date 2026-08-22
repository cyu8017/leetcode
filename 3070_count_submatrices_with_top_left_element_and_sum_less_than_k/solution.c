// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

#include <stdlib.h>

int countSubmatrices(int** grid, int gridSize, int* gridColSize, int k) {
    int m = gridSize, n = gridColSize[0], ans = 0;
    int* prev = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < m; i++) {
        int row = 0;
        for (int j = 0; j < n; j++) {
            row += grid[i][j];
            int sum = prev[j + 1] + row;
            prev[j + 1] = sum;
            if (sum <= k) ans++;
        }
    }
    free(prev);
    return ans;
}
