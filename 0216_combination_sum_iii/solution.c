// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

#include <stdlib.h>
#include <string.h>

static void backtrack(
    int start,
    int k,
    int remaining,
    int* path,
    int pathLen,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    if (pathLen == k) {
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
        }
        return;
    }
    if (remaining <= 0 || pathLen >= k) {
        return;
    }

    for (int num = start; num <= 9; num++) {
        if (num > remaining) {
            break;
        }
        path[pathLen] = num;
        backtrack(
            num + 1,
            k,
            remaining - num,
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
 */
int** combinationSum3(int k, int n, int* returnSize, int** returnColumnSizes) {
    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int path[16];
    int count = 0;

    backtrack(1, k, n, path, 0, &result, &count, &colSizes, &capacity);

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
