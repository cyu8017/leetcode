// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

#include <stdlib.h>

#define NEG3473 (-(1LL << 60))

int maxSum(int* nums, int numsSize, int k, int m) {
    int n = numsSize;
    long long* pref = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    long long** dp = (long long**)malloc((size_t)(k + 1) * sizeof(long long*));
    for (int i = 0; i <= k; i++) {
        dp[i] = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
        for (int j = 0; j <= n; j++) dp[i][j] = NEG3473;
    }
    for (int i = 0; i <= n; i++) dp[0][i] = 0;
    for (int t = 1; t <= k; t++) {
        long long best = NEG3473;
        for (int i = t * m; i <= n; i++) {
            int j = i - m;
            if (dp[t - 1][j] - pref[j] > best) best = dp[t - 1][j] - pref[j];
            dp[t][i] = best + pref[i];
        }
        for (int i = 1; i <= n; i++) {
            if (dp[t][i - 1] > dp[t][i]) dp[t][i] = dp[t][i - 1];
        }
    }
    int ans = (int)dp[k][n];
    for (int i = 0; i <= k; i++) free(dp[i]);
    free(dp);
    free(pref);
    return ans;
}
