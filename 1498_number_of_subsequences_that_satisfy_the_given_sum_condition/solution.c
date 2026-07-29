// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int numSubseq(int* nums, int numsSize, int target) {
    const int MOD = 1000000007;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int* powers = (int*)malloc((numsSize + 1) * sizeof(int));
    powers[0] = 1;
    for (int i = 1; i <= numsSize; i++) powers[i] = (powers[i - 1] * 2LL) % MOD;
    int left = 0, right = numsSize - 1, ans = 0;
    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            ans = (ans + powers[right - left]) % MOD;
            left++;
        } else right--;
    }
    free(powers);
    return ans;
}
