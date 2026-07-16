// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

#include <stdlib.h>
#include <string.h>

static int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static void append_result(
    int* path,
    int pathLen,
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
    (*result)[*resultCount] = (int*)malloc((size_t)pathLen * sizeof(int));
    if (pathLen > 0) {
        memcpy((*result)[*resultCount], path, (size_t)pathLen * sizeof(int));
    }
    (*colSizes)[*resultCount] = pathLen;
    (*resultCount)++;
}

static void backtrack(
    int* nums,
    int numsSize,
    int start,
    int* path,
    int pathLen,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    append_result(path, pathLen, result, resultCount, colSizes, capacity);
    for (int i = start; i < numsSize; i++) {
        if (i > start && nums[i] == nums[i - 1]) {
            continue;
        }
        path[pathLen] = nums[i];
        backtrack(nums, numsSize, i + 1, path, pathLen + 1, result, resultCount, colSizes, capacity);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** subsetsWithDup(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp);

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int* path = (int*)malloc((size_t)numsSize * sizeof(int));
    int count = 0;

    backtrack(nums, numsSize, 0, path, 0, &result, &count, &colSizes, &capacity);
    free(path);

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
