// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

#include <stdlib.h>
#include <string.h>

static int gcd_i(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int distinctSequences(int n) {
    const int mod = 1000000007;
    int*** dp = (int***)malloc((size_t)(n + 1) * sizeof(int**));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int**)malloc(7 * sizeof(int*));
        for (int j = 0; j < 7; j++) dp[i][j] = (int*)calloc(7, sizeof(int));
    }
    for (int a = 1; a <= 6; a++) dp[1][a][0] = 1;
    for (int i = 2; i <= n; i++) {
        for (int prev = 1; prev <= 6; prev++) {
            for (int pprev = 0; pprev <= 6; pprev++) {
                if (dp[i - 1][prev][pprev] == 0) continue;
                for (int cur = 1; cur <= 6; cur++) {
                    if (cur == prev || cur == pprev || gcd_i(cur, prev) != 1) continue;
                    dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod;
                }
            }
        }
    }
    int ans = 0;
    for (int a = 1; a <= 6; a++)
        for (int b = 0; b <= 6; b++)
            ans = (ans + dp[n][a][b]) % mod;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j < 7; j++) free(dp[i][j]);
        free(dp[i]);
    }
    free(dp);
    return ans;
}
