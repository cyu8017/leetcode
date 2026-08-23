// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

#include <algorithm>
#include <array>
#include <vector>

class Solution {
public:
    long long maximumProfit(std::vector<int>& prices, int k) {
        int n = (int)prices.size();
        std::vector<std::vector<std::array<long long, 3>>> f(n, std::vector<std::array<long long, 3>>(k + 1));
        for (int j = 1; j <= k; j++) {
            f[0][j][1] = -prices[0];
            f[0][j][2] = prices[0];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                f[i][j][0] = std::max({f[i - 1][j][0], f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]});
                f[i][j][1] = std::max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]);
                f[i][j][2] = std::max(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]);
            }
        }
        return f[n - 1][k][0];
    }
};
