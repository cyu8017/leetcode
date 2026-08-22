// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distinctDifferenceArray(int* nums, int numsSize, int* returnSize) {
    int* suf = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    bool seen[51];
    memset(seen, 0, sizeof(seen));
    int cnt = 0;
    for (int i = numsSize - 1; i >= 0; i--) {
        if (!seen[nums[i]]) { seen[nums[i]] = true; cnt++; }
        suf[i] = cnt;
    }
    memset(seen, 0, sizeof(seen));
    cnt = 0;
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        if (!seen[nums[i]]) { seen[nums[i]] = true; cnt++; }
        ans[i] = cnt - suf[i + 1];
    }
    free(suf);
    *returnSize = numsSize;
    return ans;
}
