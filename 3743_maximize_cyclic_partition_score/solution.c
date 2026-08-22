// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

#include <stdlib.h>

long long maximumScore(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* a = (int*)malloc((size_t)(2 * n) * sizeof(int));
    for (int i = 0; i < n; i++) { a[i] = nums[i]; a[i + n] = nums[i]; }
    if (k > n) k = n;
    long long best = 0;
    long long NEG = -(1LL << 60);
    for (int start = 0; start < n; start++) {
        int* seg = a + start;
        long long** dp = (long long**)malloc((size_t)(n + 1) * sizeof(long long*));
        for (int i = 0; i <= n; i++) {
            dp[i] = (long long*)malloc((size_t)(k + 1) * sizeof(long long));
            for (int j = 0; j <= k; j++) dp[i][j] = NEG;
        }
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k && j <= i; j++) {
                long long mx = NEG;
                for (int t = i; t >= j; t--) {
                    if ((long long)seg[t - 1] > mx) mx = seg[t - 1];
                    if (dp[t - 1][j - 1] > NEG / 2) {
                        long long cand = dp[t - 1][j - 1] + mx;
                        if (cand > dp[i][j]) dp[i][j] = cand;
                    }
                }
            }
        }
        if (dp[n][k] > best) best = dp[n][k];
        for (int i = 0; i <= n; i++) free(dp[i]);
        free(dp);
    }
    free(a);
    return best;
}
