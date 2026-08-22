// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

#include <stdlib.h>

long long maxSubarraySum(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long* pref = (long long*)malloc((n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    long long BIG = 1LL << 62;
    long long* best = (long long*)malloc(k * sizeof(long long));
    for (int i = 0; i < k; i++) best[i] = BIG;
    best[0] = 0;
    long long ans = -(1LL << 62);
    for (int i = 1; i <= n; i++) {
        int r = i % k;
        if (best[r] != BIG) {
            long long cand = pref[i] - best[r];
            if (cand > ans) ans = cand;
        }
        if (pref[i] < best[r]) best[r] = pref[i];
    }
    free(pref); free(best);
    return ans;
}
