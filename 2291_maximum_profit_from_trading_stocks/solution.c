// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

#include <stdlib.h>

int maximumProfit(int* present, int presentSize, int* future, int futureSize, int budget) {
    (void)futureSize;
    int* dp = (int*)calloc((size_t)(budget + 1), sizeof(int));
    for (int i = 0; i < presentSize; i++) {
        int profit = future[i] - present[i];
        if (profit <= 0) continue;
        int cost = present[i];
        for (int b = budget; b >= cost; b--) {
            if (dp[b - cost] + profit > dp[b]) {
                dp[b] = dp[b - cost] + profit;
            }
        }
    }
    int ans = dp[budget];
    free(dp);
    return ans;
}
