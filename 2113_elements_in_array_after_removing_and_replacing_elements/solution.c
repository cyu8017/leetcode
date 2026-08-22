// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

#include <stdlib.h>

int* elementInNums(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int n = numsSize;
    for (int i = 0; i < queriesSize; i++) {
        int t = queries[i][0], idx = queries[i][1];
        int cycle = t % (2 * n);
        int size, offset;
        if (cycle < n) {
            size = n - cycle;
            offset = cycle;
        } else {
            size = cycle - n;
            offset = 0;
        }
        ans[i] = (idx >= size) ? -1 : nums[offset + idx];
    }
    *returnSize = queriesSize;
    return ans;
}
