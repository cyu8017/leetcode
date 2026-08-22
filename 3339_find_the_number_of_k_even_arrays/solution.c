// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

#include <stdlib.h>
#include <string.h>

int countOfArrays(int n, int m, int k) {
    const int mod = 1000000007;
    int even = m / 2, odd = m - even;
    int*** dp = (int***)malloc((size_t)(n + 1) * sizeof(int**));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int**)malloc((size_t)(k + 1) * sizeof(int*));
        for (int j = 0; j <= k; j++) dp[i][j] = (int*)calloc(2, sizeof(int));
    }
    dp[1][0][0] = odd;
    dp[1][0][1] = even;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= k; j++) {
            dp[i + 1][j][0] = (dp[i + 1][j][0] + (int)(((long long)(dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod)) % mod;
            dp[i + 1][j][1] = (dp[i + 1][j][1] + (int)((long long)dp[i][j][0] * even % mod)) % mod;
            if (j < k)
                dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + (int)((long long)dp[i][j][1] * even % mod)) % mod;
        }
    }
    int ans = (dp[n][k][0] + dp[n][k][1]) % mod;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= k; j++) free(dp[i][j]);
        free(dp[i]);
    }
    free(dp);
    return ans;
}
