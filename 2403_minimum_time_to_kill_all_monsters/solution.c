// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

#include <stdlib.h>

static int bitcount(int x) { int c = 0; while (x) { c += x & 1; x >>= 1; } return c; }

long long minimumTime(int* power, int powerSize) {
    int n = powerSize, N = 1 << n;
    long long* dp = (long long*)malloc((size_t)N * sizeof(long long));
    for (int i = 0; i < N; i++) dp[i] = 1LL << 60;
    dp[0] = 0;
    for (int mask = 0; mask < N; mask++) {
        long long gain = bitcount(mask) + 1;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
            long long need = (power[i] + gain - 1) / gain;
            int nm = mask | (1 << i);
            if (dp[mask] + need < dp[nm]) dp[nm] = dp[mask] + need;
        }
    }
    long long ans = dp[N - 1];
    free(dp);
    return ans;
}
