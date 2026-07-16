// LeetCode 0322 - Coin Change
// https://leetcode.com/problems/coin-change/

#include <limits.h>
#include <stdlib.h>

int coinChange(int* coins, int coinsSize, int amount) {
    const int maxValue = amount + 1;
    int* dp = (int*)malloc((size_t)(amount + 1) * sizeof(int));
    for (int value = 0; value <= amount; value++) {
        dp[value] = maxValue;
    }
    dp[0] = 0;
    for (int coinIndex = 0; coinIndex < coinsSize; coinIndex++) {
        int coin = coins[coinIndex];
        for (int value = coin; value <= amount; value++) {
            int candidate = dp[value - coin] + 1;
            if (candidate < dp[value]) {
                dp[value] = candidate;
            }
        }
    }
    int result = dp[amount] == maxValue ? -1 : dp[amount];
    free(dp);
    return result;
}
