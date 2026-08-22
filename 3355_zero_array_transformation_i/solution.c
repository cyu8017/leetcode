// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

#include <stdlib.h>
#include <stdbool.h>

bool isZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    int n = numsSize;
    int* diff = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        diff[queries[i][0]]++;
        diff[queries[i][1] + 1]--;
    }
    int cur = 0;
    for (int i = 0; i < n; i++) {
        cur += diff[i];
        if (cur < nums[i]) { free(diff); return false; }
    }
    free(diff);
    return true;
}
