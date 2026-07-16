// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

#include <stdlib.h>

int change(int amount, int* coins, int coinsSize) {
    long long* dp = (long long*)calloc((size_t)amount + 1, sizeof(long long));
    dp[0] = 1;
    for (int coinIndex = 0; coinIndex < coinsSize; coinIndex++) {
        const int coin = coins[coinIndex];
        for (int value = coin; value <= amount; value++) {
            dp[value] += dp[value - coin];
        }
    }
    const int result = (int)dp[amount];
    free(dp);
    return result;
}
