// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

#include <stdlib.h>

static int cmp2655(const void* a, const void* b) {
    int* const* aa = (int* const*)a;
    int* const* bb = (int* const*)b;
    if ((*aa)[0] != (*bb)[0]) return (*aa)[0] - (*bb)[0];
    return (*aa)[1] - (*bb)[1];
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** findMaximalUncoveredRanges(int n, int** ranges, int rangesSize, int* rangesColSize, int* returnSize, int** returnColumnSizes) {
    (void)rangesColSize;
    if (rangesSize > 0) qsort(ranges, (size_t)rangesSize, sizeof(int*), cmp2655);
    int cap = rangesSize + 2;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    int* cols = (int*)malloc((size_t)cap * sizeof(int));
    int sz = 0, cur = 0;
    for (int i = 0; i < rangesSize; i++) {
        if (ranges[i][0] > cur) {
            ans[sz] = (int*)malloc(2 * sizeof(int));
            ans[sz][0] = cur; ans[sz][1] = ranges[i][0] - 1;
            cols[sz++] = 2;
        }
        if (ranges[i][1] + 1 > cur) cur = ranges[i][1] + 1;
    }
    if (cur < n) {
        ans[sz] = (int*)malloc(2 * sizeof(int));
        ans[sz][0] = cur; ans[sz][1] = n - 1;
        cols[sz++] = 2;
    }
    *returnSize = sz;
    *returnColumnSizes = cols;
    return ans;
}
