// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

#include <stdlib.h>
#include <string.h>

static int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static void backtrack(
    int* nums,
    int numsSize,
    int* path,
    int pathLen,
    int* used,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    if (pathLen == numsSize) {
        if (*resultCount >= *capacity) {
            *capacity *= 2;
            *result = (int**)realloc(*result, (size_t)(*capacity) * sizeof(int*));
            *colSizes = (int*)realloc(*colSizes, (size_t)(*capacity) * sizeof(int));
        }
        (*result)[*resultCount] = (int*)malloc((size_t)numsSize * sizeof(int));
        memcpy((*result)[*resultCount], path, (size_t)numsSize * sizeof(int));
        (*colSizes)[*resultCount] = numsSize;
        (*resultCount)++;
        return;
    }

    for (int i = 0; i < numsSize; i++) {
        if (used[i]) {
            continue;
        }
        if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
            continue;
        }
        used[i] = 1;
        path[pathLen] = nums[i];
        backtrack(nums, numsSize, path, pathLen + 1, used, result, resultCount, colSizes, capacity);
        used[i] = 0;
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), cmp);

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int* path = (int*)malloc((size_t)numsSize * sizeof(int));
    int* used = (int*)calloc((size_t)numsSize, sizeof(int));
    int count = 0;

    backtrack(nums, numsSize, path, 0, used, &result, &count, &colSizes, &capacity);

    free(path);
    free(used);

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
