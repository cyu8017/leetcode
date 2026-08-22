// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

#include <stdlib.h>

static int modPow(long long a, long long e, int mod) {
    long long r = 1; a %= mod;
    while (e > 0) { if (e & 1) r = r * a % mod; a = a * a % mod; e >>= 1; }
    return (int)r;
}

int numberOfWays(int n, int x, int y) {
    const int mod = 1000000007;
    int** dp = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) dp[i] = (int*)calloc((size_t)(x + 1), sizeof(int));
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= x && j <= i; j++)
            dp[i][j] = (int)((dp[i - 1][j - 1] + (long long)j * dp[i - 1][j]) % mod);
    int* fact = (int*)malloc((size_t)(x + 1) * sizeof(int));
    fact[0] = 1;
    for (int i = 1; i <= x; i++) fact[i] = (int)((long long)fact[i - 1] * i % mod);
    int ans = 0, ypow = 1;
    for (int k = 1; k <= x && k <= n; k++) {
        ypow = (int)((long long)ypow * y % mod);
        int perm = (int)((long long)fact[x] * modPow(fact[x - k], mod - 2, mod) % mod);
        ans = (int)((ans + (long long)dp[n][k] * perm % mod * ypow) % mod);
    }
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(dp); free(fact);
    return ans;
}
