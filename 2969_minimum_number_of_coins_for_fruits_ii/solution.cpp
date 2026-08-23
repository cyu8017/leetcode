// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    int minimumCoins(std::vector<int>& prices) {
        int n = (int)prices.size();
        std::vector<int> dp(n + 1, 1 << 30);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n && j <= 2 * i; j++) {
                dp[j] = std::min(dp[j], dp[i - 1] + prices[i - 1]);
            }
        }
        return dp[n];
    }
};
