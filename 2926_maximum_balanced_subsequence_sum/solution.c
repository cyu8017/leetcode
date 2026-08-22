// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

long long maxBalancedSubsequenceSum(int* nums, int numsSize) {
    int n = numsSize;
    int* keys = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) keys[i] = nums[i] - i;
    int* sorted = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) sorted[i] = keys[i];
    qsort(sorted, n, sizeof(int), cmp_int);
    int* uniq = (int*)malloc(n * sizeof(int));
    int un = 0;
    for (int i = 0; i < n; i++) if (un == 0 || uniq[un - 1] != sorted[i]) uniq[un++] = sorted[i];
    long long* bit = (long long*)malloc((un + 2) * sizeof(long long));
    const long long negInf = -(1LL << 60);
    for (int i = 0; i < un + 2; i++) bit[i] = negInf;
    long long ans = negInf;
    for (int i = 0; i < n; i++) {
        /* binary search idx */
        int lo = 0, hi = un - 1, id = 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (uniq[mid] == keys[i]) { id = mid + 1; break; }
            if (uniq[mid] < keys[i]) lo = mid + 1; else hi = mid - 1;
        }
        long long best = negInf;
        for (int t = id; t > 0; t -= t & -t) if (bit[t] > best) best = bit[t];
        long long cur = nums[i];
        if (best > negInf / 2) {
            long long cand = best + nums[i];
            if (cand > cur) cur = cand;
        }
        for (int t = id; t < un + 2; t += t & -t) if (cur > bit[t]) bit[t] = cur;
        if (cur > ans) ans = cur;
    }
    free(keys); free(sorted); free(uniq); free(bit);
    return ans;
}
