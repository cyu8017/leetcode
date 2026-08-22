// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

#include <stdlib.h>
#include <string.h>

static void backtrack(
    int n,
    int k,
    int start,
    int* path,
    int pathLen,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    if (pathLen == k) {
        if (*resultCount >= *capacity) {
            *capacity *= 2;
            *result = (int**)realloc(*result, (size_t)(*capacity) * sizeof(int*));
            *colSizes = (int*)realloc(*colSizes, (size_t)(*capacity) * sizeof(int));
        }
        (*result)[*resultCount] = (int*)malloc((size_t)k * sizeof(int));
        memcpy((*result)[*resultCount], path, (size_t)k * sizeof(int));
        (*colSizes)[*resultCount] = k;
        (*resultCount)++;
        return;
    }

    int remaining = k - pathLen;
    for (int i = start; i <= n - remaining + 1; i++) {
        path[pathLen] = i;
        backtrack(n, k, i + 1, path, pathLen + 1, result, resultCount, colSizes, capacity);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced by caller.
 */
int** combine(int n, int k, int* returnSize, int** returnColumnSizes) {
    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int* path = (int*)malloc((size_t)k * sizeof(int));
    int count = 0;

    backtrack(n, k, 1, path, 0, &result, &count, &colSizes, &capacity);

    free(path);

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
