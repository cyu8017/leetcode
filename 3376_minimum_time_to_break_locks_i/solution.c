// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

#include <stdlib.h>

int findMinimumTime(int* strength, int strengthSize, int k) {
    int n = strengthSize, N = 1 << n, INF = 1000000000;
    int* dp = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) dp[i] = INF;
    dp[0] = 0;
    for (int mask = 0; mask < N; mask++) {
        if (dp[mask] == INF) continue;
        int opened = 0; for (int t = mask; t; t >>= 1) opened += t & 1;
        int x = 1 + opened * k;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
            int t = (strength[i] + x - 1) / x;
            int nmask = mask | (1 << i);
            if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
        }
    }
    int ans = dp[N - 1];
    free(dp);
    return ans;
}
