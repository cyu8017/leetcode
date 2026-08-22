// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* resultArray(int* nums, int numsSize, int k, int* returnSize) {
    long long* ans = (long long*)calloc((size_t)k, sizeof(long long));
    long long* dp = (long long*)calloc((size_t)k, sizeof(long long));
    for (int t = 0; t < numsSize; t++) {
        long long* newDp = (long long*)calloc((size_t)k, sizeof(long long));
        int nm = nums[t] % k;
        newDp[nm] = 1;
        for (int i = 0; i < k; i++) newDp[(i * nm) % k] += dp[i];
        for (int i = 0; i < k; i++) ans[i] += newDp[i];
        free(dp);
        dp = newDp;
    }
    free(dp);
    *returnSize = k;
    return ans;
}
