// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

#include <vector>

class Solution {
public:
    int minimumCoins(std::vector<int>& prices) {
        int n = (int)prices.size();
        std::vector<int> dp(n + 1, 1 << 30);
        dp[0] = 0;
        for (int i = 1; i <= n; i++)
            for (int j = i; j <= n && j <= i + i; j++) {
                int cand = dp[i - 1] + prices[i - 1];
                if (cand < dp[j]) dp[j] = cand;
            }
        return dp[n];
    }
};
