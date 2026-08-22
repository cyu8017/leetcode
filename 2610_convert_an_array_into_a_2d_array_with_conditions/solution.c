// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

#include <stdlib.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findMatrix(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int freq[201];
    memset(freq, 0, sizeof(freq));
    int** ans = (int**)malloc((size_t)numsSize * sizeof(int*));
    int* caps = (int*)calloc((size_t)numsSize, sizeof(int));
    int* sizes = (int*)calloc((size_t)numsSize, sizeof(int));
    int rows = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int f = freq[x];
        if (f == rows) {
            ans[rows] = (int*)malloc((size_t)numsSize * sizeof(int));
            caps[rows] = numsSize;
            sizes[rows] = 0;
            rows++;
        }
        ans[f][sizes[f]++] = x;
        freq[x]++;
    }
    *returnSize = rows;
    *returnColumnSizes = (int*)malloc((size_t)rows * sizeof(int));
    for (int i = 0; i < rows; i++) (*returnColumnSizes)[i] = sizes[i];
    free(caps); free(sizes);
    return ans;
}
