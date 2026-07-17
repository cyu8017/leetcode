// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

#include <math.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* solve(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    const long long mod = 1000000007LL;
    int n = numsSize;
    int block = (int)sqrt((double)n) + 1;
    int* dp = (int*)calloc((size_t)block * n, sizeof(int));
    for (int step = 1; step < block; step++) {
        for (int i = n - 1; i >= 0; i--) {
            long long next = i + step < n ? dp[step * n + i + step] : 0;
            dp[step * n + i] = (int)((nums[i] + next) % mod);
        }
    }
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; q++) {
        int start = queries[q][0];
        int step = queries[q][1];
        if (step < block) {
            ans[q] = dp[step * n + start];
        } else {
            long long total = 0;
            for (int i = start; i < n; i += step) {
                total += nums[i];
            }
            ans[q] = (int)(total % mod);
        }
    }
    free(dp);
    *returnSize = queriesSize;
    return ans;
}
