// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

#include <stdbool.h>

static bool check3824(int* nums, int n, int k) {
    long long t = 0;
    for (int i = 0; i < n; i++) t += (nums[i] + k - 1) / k;
    return t <= (long long)k * k;
}

int minimumK(int* nums, int numsSize) {
    int lo = 1, hi = 100000;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (check3824(nums, numsSize, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
