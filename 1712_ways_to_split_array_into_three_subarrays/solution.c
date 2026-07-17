// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

#include <stdlib.h>

static int lowerBound(const long long* prefix, long long target, int lo, int hi) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (prefix[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

static int upperBound(const long long* prefix, long long target, int lo, int hi) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (prefix[mid] <= target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

int waysToSplit(int* nums, int numsSize) {
    const long long mod = 1000000007LL;
    long long* prefix = (long long*)malloc(numsSize * sizeof(long long));
    long long total = 0;
    for (int i = 0; i < numsSize; i++) {
        total += nums[i];
        prefix[i] = total;
    }
    long long ans = 0;
    for (int i = 0; i < numsSize - 2; i++) {
        long long left = prefix[i];
        int lo = lowerBound(prefix, 2 * left, i + 1, numsSize - 1);
        int hi = upperBound(prefix, (total + left) / 2, lo, numsSize - 1);
        ans = (ans + hi - lo) % mod;
    }
    free(prefix);
    return (int)ans;
}
