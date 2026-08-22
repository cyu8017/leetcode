// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int iabs(int x) { return x < 0 ? -x : x; }

int** minAbsDiff(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize, n = gridColSize[0];
    int rows = m - k + 1, cols = n - k + 1;
    int** ans = (int**)malloc((size_t)rows * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)rows * sizeof(int));
    for (int i = 0; i < rows; i++) {
        ans[i] = (int*)calloc((size_t)cols, sizeof(int));
        (*returnColumnSizes)[i] = cols;
    }
    int* nums = (int*)malloc((size_t)k * k * sizeof(int));
    for (int i = 0; i <= m - k; i++) {
        for (int j = 0; j <= n - k; j++) {
            int t = 0;
            for (int x = i; x < i + k; x++)
                for (int y = j; y < j + k; y++)
                    nums[t++] = grid[x][y];
            qsort(nums, (size_t)t, sizeof(int), cmp_int);
            int d = INT_MAX;
            for (int p = 1; p < t; p++) {
                if (nums[p] != nums[p - 1]) {
                    int diff = iabs(nums[p] - nums[p - 1]);
                    if (diff < d) d = diff;
                }
            }
            if (d != INT_MAX) ans[i][j] = d;
        }
    }
    free(nums);
    *returnSize = rows;
    return ans;
}
