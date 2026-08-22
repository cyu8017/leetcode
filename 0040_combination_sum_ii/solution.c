// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

#include <stdlib.h>
#include <string.h>

static int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static void backtrack(
    int* candidates,
    int candidatesSize,
    int start,
    int remaining,
    int* path,
    int pathLen,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    if (remaining == 0) {
        if (*resultCount >= *capacity) {
            *capacity *= 2;
            *result = (int**)realloc(*result, (size_t)(*capacity) * sizeof(int*));
            *colSizes = (int*)realloc(*colSizes, (size_t)(*capacity) * sizeof(int));
        }
        (*result)[*resultCount] = (int*)malloc((size_t)pathLen * sizeof(int));
        memcpy((*result)[*resultCount], path, (size_t)pathLen * sizeof(int));
        (*colSizes)[*resultCount] = pathLen;
        (*resultCount)++;
        return;
    }
    if (remaining < 0) {
        return;
    }

    for (int i = start; i < candidatesSize; i++) {
        if (i > start && candidates[i] == candidates[i - 1]) {
            continue;
        }
        path[pathLen] = candidates[i];
        backtrack(
            candidates,
            candidatesSize,
            i + 1,
            remaining - candidates[i],
            path,
            pathLen + 1,
            result,
            resultCount,
            colSizes,
            capacity
        );
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    qsort(candidates, candidatesSize, sizeof(int), cmp);

    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int path[32];
    int count = 0;

    backtrack(candidates, candidatesSize, 0, target, path, 0, &result, &count, &colSizes, &capacity);

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
