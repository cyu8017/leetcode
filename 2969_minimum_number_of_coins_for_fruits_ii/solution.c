// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

#include <stdlib.h>

int minimumCoins(int* prices, int pricesSize) {
    int n = pricesSize;
    int* dp = (int*)malloc((size_t)(n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) dp[i] = 1 << 30;
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n && j <= 2 * i; j++) {
            int cand = dp[i - 1] + prices[i - 1];
            if (cand < dp[j]) dp[j] = cand;
        }
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
