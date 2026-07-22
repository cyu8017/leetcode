// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

#include <stdlib.h>

int waysToDistribute(int n, int k) {
    const int MOD = 1000000007;
    long long* dp = (long long*)calloc((size_t)k + 1, sizeof(long long));
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = (i < k ? i : k); j >= 1; j--) {
            dp[j] = (dp[j - 1] + j * dp[j]) % MOD;
        }
        dp[0] = 0;
    }
    int ans = (int)dp[k];
    free(dp);
    return ans;
}
