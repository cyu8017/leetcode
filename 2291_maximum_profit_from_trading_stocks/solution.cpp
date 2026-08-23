// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumProfit(std::vector<int>& present, std::vector<int>& future, int budget) {
        int n = (int)present.size();
        std::vector<int> dp(budget + 1);
        for (int i = 0; i < n; ++i) {
            int profit = future[i] - present[i];
            if (profit <= 0) continue;
            int cost = present[i];
            for (int b = budget; b >= cost; --b)
                dp[b] = std::max(dp[b], dp[b - cost] + profit);
        }
        return dp[budget];
    }
};
