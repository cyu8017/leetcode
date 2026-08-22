// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

long long minOperationsToMakeMedianK(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int m = numsSize >> 1;
    long long ans = llabs((long long)nums[m] - k);
    if (nums[m] > k) {
        for (int i = m - 1; i >= 0 && nums[i] > k; i--) ans += (long long)nums[i] - k;
    } else {
        for (int i = m + 1; i < numsSize && nums[i] < k; i++) ans += (long long)k - nums[i];
    }
    return ans;
}
