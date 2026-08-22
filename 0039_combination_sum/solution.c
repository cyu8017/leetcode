// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

#include <stdlib.h>
#include <string.h>

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
        path[pathLen] = candidates[i];
        backtrack(
            candidates,
            candidatesSize,
            i,
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
int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
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
