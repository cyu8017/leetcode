// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

#include <stdlib.h>
#include <limits.h>

int minSpaceWastedKResizing(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long INF = LLONG_MAX / 4;
    long long** waste = (long long**)malloc((size_t)n * sizeof(long long*));
    for (int i = 0; i < n; i++) {
        waste[i] = (long long*)malloc((size_t)n * sizeof(long long));
        int mx = 0;
        long long total = 0;
        for (int j = i; j < n; j++) {
            if (nums[j] > mx) mx = nums[j];
            total += nums[j];
            waste[i][j] = (long long)mx * (j - i + 1) - total;
        }
    }
    int segments = k + 1;
    long long** dp = (long long**)malloc((size_t)(n + 1) * sizeof(long long*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (long long*)malloc((size_t)(segments + 1) * sizeof(long long));
        for (int s = 0; s <= segments; s++) dp[i][s] = INF;
    }
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int s = 1; s <= segments && s <= i; s++) {
            for (int p = s - 1; p < i; p++) {
                long long cand = dp[p][s - 1] + waste[p][i - 1];
                if (cand < dp[i][s]) dp[i][s] = cand;
            }
        }
    }
    long long ans = INF;
    for (int s = 1; s <= segments; s++) if (dp[n][s] < ans) ans = dp[n][s];
    for (int i = 0; i < n; i++) free(waste[i]);
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(waste); free(dp);
    return (int)ans;
}
