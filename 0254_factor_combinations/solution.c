// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

#include <stdlib.h>
#include <string.h>

static void backtrack(
    int remain,
    int start,
    int* path,
    int pathLen,
    int*** result,
    int* resultCount,
    int** colSizes,
    int* capacity
) {
    if (start > remain) {
        if (pathLen > 1) {
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

    for (int factor = start; factor * factor <= remain; factor++) {
        if (remain % factor == 0) {
            path[pathLen] = factor;
            backtrack(remain / factor, factor, path, pathLen + 1, result, resultCount, colSizes, capacity);
        }
    }

    if (pathLen > 0) {
        path[pathLen] = remain;
        if (pathLen + 1 > 1) {
            if (*resultCount >= *capacity) {
                *capacity *= 2;
                *result = (int**)realloc(*result, (size_t)(*capacity) * sizeof(int*));
                *colSizes = (int*)realloc(*colSizes, (size_t)(*capacity) * sizeof(int));
            }
            (*result)[*resultCount] = (int*)malloc((size_t)(pathLen + 1) * sizeof(int));
            memcpy((*result)[*resultCount], path, (size_t)(pathLen + 1) * sizeof(int));
            (*colSizes)[*resultCount] = pathLen + 1;
            (*resultCount)++;
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 */
int** getFactors(int n, int* returnSize, int** returnColumnSizes) {
    int capacity = 16;
    int** result = (int**)malloc((size_t)capacity * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)capacity * sizeof(int));
    int path[32];
    int count = 0;

    backtrack(n, 2, path, 0, &result, &count, &colSizes, &capacity);

    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    result = (int**)realloc(result, (size_t)count * sizeof(int*));
    return result;
}
