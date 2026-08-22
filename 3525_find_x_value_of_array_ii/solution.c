// LeetCode 3525 - Find X Value Of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultArray(int* nums, int numsSize, int k, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3];
        nums[idx] = val;
        int prod = 1, cnt = 0;
        for (int i = start; i < numsSize; i++) {
            prod = prod * (nums[i] % k) % k;
            if (prod == x) cnt++;
        }
        ans[qi] = cnt;
    }
    *returnSize = queriesSize;
    return ans;
}
