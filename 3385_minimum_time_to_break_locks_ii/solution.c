// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

#include <stdlib.h>

long long findMinimumTime(int* strength, int strengthSize) {
    int n = strengthSize, N = 1 << n;
    const long long INF = 1000000000000000000LL;
    long long* dp = (long long*)malloc(N * sizeof(long long));
    for (int i = 0; i < N; i++) dp[i] = INF;
    dp[0] = 0;
    int k = 1;
    for (int mask = 0; mask < N; mask++) {
        if (dp[mask] == INF) continue;
        int opened = 0; for (int t = mask; t; t >>= 1) opened += t & 1;
        int x = 1 + opened * k;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
            long long t = (strength[i] + x - 1) / x;
            int nmask = mask | (1 << i);
            if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
        }
    }
    long long ans = dp[N - 1];
    free(dp);
    return ans;
}
