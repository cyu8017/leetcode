// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

#include <stdlib.h>
static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
long long maximumMedianSum(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    long long ans = 0;
    for (int i = numsSize / 3; i < numsSize; i += 2) ans += nums[i];
    return ans;
}
