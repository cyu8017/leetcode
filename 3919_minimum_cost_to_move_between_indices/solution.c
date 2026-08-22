// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

#include <stdlib.h>

int* minCost(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = numsSize;
    int* s1 = calloc((size_t)n, sizeof(int));
    int* s2 = calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) {
        int c1 = 1;
        if (i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]) c1 = nums[i] - nums[i - 1];
        int c2 = 1;
        if (i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]) c2 = nums[i] - nums[i - 1];
        s1[i] = s1[i - 1] + c1;
        s2[i] = s2[i - 1] + c2;
    }
    int* ans = malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int l = queries[i][0], r = queries[i][1];
        ans[i] = (l < r) ? (s1[r] - s1[l]) : (s2[l] - s2[r]);
    }
    free(s1); free(s2);
    *returnSize = queriesSize;
    return ans;
}
