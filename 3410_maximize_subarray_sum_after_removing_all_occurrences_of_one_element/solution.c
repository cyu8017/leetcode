// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

#include <stdlib.h>

static long long kadane(int* a, int n) {
    long long best = -(1LL << 62), cur = 0, mx = a[0];
    int allNeg = 1;
    for (int i = 0; i < n; i++) {
        cur += a[i];
        if (cur > best) best = cur;
        if (cur < 0) cur = 0;
        if (a[i] > mx) mx = a[i];
        if (a[i] >= 0) allNeg = 0;
    }
    return allNeg ? mx : best;
}

long long maxSubarraySum(int* nums, int numsSize) {
    long long ans = kadane(nums, numsSize);
    int* neg = (int*)malloc(numsSize * sizeof(int)); int nn = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] < 0) {
        int f = 0; for (int j = 0; j < nn; j++) if (neg[j] == nums[i]) f = 1;
        if (!f) neg[nn++] = nums[i];
    }
    int* b = (int*)malloc(numsSize * sizeof(int));
    for (int vi = 0; vi < nn; vi++) {
        int bn = 0;
        for (int i = 0; i < numsSize; i++) if (nums[i] != neg[vi]) b[bn++] = nums[i];
        if (bn == 0) continue;
        long long cand = kadane(b, bn);
        if (cand > ans) ans = cand;
    }
    free(neg); free(b);
    return ans;
}
