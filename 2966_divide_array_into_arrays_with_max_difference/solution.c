// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

#include <stdlib.h>

static int cmp2966(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** divideArray(int* nums, int numsSize, int k, int* returnSize, int** returnColumnSizes) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) arr[i] = nums[i];
    qsort(arr, (size_t)numsSize, sizeof(int), cmp2966);
    int groups = numsSize / 3;
    int** ans = (int**)malloc((size_t)groups * sizeof(int*));
    int* cols = (int*)malloc((size_t)groups * sizeof(int));
    for (int i = 0; i < numsSize; i += 3) {
        if (arr[i + 2] - arr[i] > k) {
            for (int j = 0; j < i / 3; j++) free(ans[j]);
            free(ans);
            free(cols);
            free(arr);
            *returnSize = 0;
            *returnColumnSizes = NULL;
            return NULL;
        }
        int gi = i / 3;
        ans[gi] = (int*)malloc(3 * sizeof(int));
        ans[gi][0] = arr[i];
        ans[gi][1] = arr[i + 1];
        ans[gi][2] = arr[i + 2];
        cols[gi] = 3;
    }
    free(arr);
    *returnSize = groups;
    *returnColumnSizes = cols;
    return ans;
}
