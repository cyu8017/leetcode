// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** chunk(int* arr, int arrSize, int size, int* returnSize, int** returnColumnSizes) {
    int n = size <= 0 ? 0 : (arrSize + size - 1) / size;
    *returnSize = n;
    if (n == 0) { *returnColumnSizes = NULL; return NULL; }
    int** ans = (int**)malloc((size_t)n * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0, idx = 0; i < arrSize; i += size, idx++) {
        int end = i + size;
        if (end > arrSize) end = arrSize;
        int len = end - i;
        (*returnColumnSizes)[idx] = len;
        ans[idx] = (int*)malloc((size_t)len * sizeof(int));
        for (int j = 0; j < len; j++) ans[idx][j] = arr[i + j];
    }
    return ans;
}
