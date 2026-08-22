// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

#include <stdlib.h>
#include <string.h>

static void append_result(
    int* subset,
    int subsetLen,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    if (*resultCount >= *capacity) {
        *capacity *= 2;
        *result = (int**)realloc(*result, (size_t)(*capacity) * sizeof(int*));
        *colSizes = (int*)realloc(*colSizes, (size_t)(*capacity) * sizeof(int));
    }
    (*result)[*resultCount] = (int*)malloc((size_t)subsetLen * sizeof(int));
    if (subsetLen > 0) {
        memcpy((*result)[*resultCount], subset, (size_t)subsetLen * sizeof(int));
    }
    (*colSizes)[*resultCount] = subsetLen;
    (*resultCount)++;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int count = 0;

    append_result(NULL, 0, &result, &count, &colSizes, &capacity);

    for (int n = 0; n < numsSize; n++) {
        int size = count;
        for (int i = 0; i < size; i++) {
            int subsetLen = colSizes[i];
            int* subset = (int*)malloc((size_t)(subsetLen + 1) * sizeof(int));
            if (subsetLen > 0) {
                memcpy(subset, result[i], (size_t)subsetLen * sizeof(int));
            }
            subset[subsetLen] = nums[n];
            append_result(subset, subsetLen + 1, &result, &count, &colSizes, &capacity);
            free(subset);
        }
    }

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
