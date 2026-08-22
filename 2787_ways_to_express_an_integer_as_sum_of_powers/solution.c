// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

#include <stdlib.h>

int numberOfWays(int n, int x) {
    const int mod = 1000000007;
    int powers[400], pcnt = 0;
    for (int i = 1; ; i++) {
        long long p = 1;
        for (int j = 0; j < x; j++) {
            p *= i;
            if (p > n) break;
        }
        if (p > n) break;
        powers[pcnt++] = (int)p;
    }
    int* dp = (int*)calloc(n + 1, sizeof(int));
    dp[0] = 1;
    for (int i = 0; i < pcnt; i++) {
        int p = powers[i];
        for (int s = n; s >= p; s--) dp[s] = (dp[s] + dp[s - p]) % mod;
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
