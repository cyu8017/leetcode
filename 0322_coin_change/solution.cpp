// LeetCode 0322 - Coin Change
// https://leetcode.com/problems/coin-change/

#include <algorithm>
#include <vector>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        const int maxValue = amount + 1;
        std::vector<int> dp(amount + 1, maxValue);
        dp[0] = 0;
        for (int coin : coins) {
            for (int value = coin; value <= amount; value++) {
                dp[value] = std::min(dp[value], dp[value - coin] + 1);
            }
        }
        return dp[amount] == maxValue ? -1 : dp[amount];
    }
};
