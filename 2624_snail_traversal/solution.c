// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** snail(int* nums, int numsSize, int rowsCount, int colsCount, int* returnSize, int** returnColumnSizes) {
    if (rowsCount * colsCount != numsSize) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int** ans = (int**)malloc((size_t)rowsCount * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)rowsCount * sizeof(int));
    for (int i = 0; i < rowsCount; i++) {
        ans[i] = (int*)malloc((size_t)colsCount * sizeof(int));
        (*returnColumnSizes)[i] = colsCount;
    }
    int idx = 0;
    for (int c = 0; c < colsCount; c++) {
        if (c % 2 == 0) {
            for (int r = 0; r < rowsCount; r++) ans[r][c] = nums[idx++];
        } else {
            for (int r = rowsCount - 1; r >= 0; r--) ans[r][c] = nums[idx++];
        }
    }
    *returnSize = rowsCount;
    return ans;
}
