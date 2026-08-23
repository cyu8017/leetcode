// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

#include <vector>

class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        std::vector<long long> dp(amount + 1, 0);
        dp[0] = 1;
        for (const int coin : coins) {
            for (int value = coin; value <= amount; ++value) {
                dp[value] += dp[value - coin];
            }
        }
        return static_cast<int>(dp[amount]);
    }
};
