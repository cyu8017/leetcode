// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

#include <stdlib.h>

int* sumEvenAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int even = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] % 2 == 0) even += nums[i];
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int val = queries[q][0], i = queries[q][1];
        if (nums[i] % 2 == 0) even -= nums[i];
        nums[i] += val;
        if (nums[i] % 2 == 0) even += nums[i];
        ans[q] = even;
    }
    *returnSize = queriesSize;
    return ans;
}
