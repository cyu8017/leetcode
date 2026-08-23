// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long sellingWood(int m, int n, std::vector<std::vector<int>>& prices) {
        std::vector<std::vector<long long>> price(m + 1, std::vector<long long>(n + 1));
        std::vector<std::vector<long long>> dp(m + 1, std::vector<long long>(n + 1));
        for (auto& p : prices) price[p[0]][p[1]] = p[2];
        for (int h = 1; h <= m; ++h) {
            for (int w = 1; w <= n; ++w) {
                long long best = price[h][w];
                for (int i = 1; i < h; ++i) best = std::max(best, dp[i][w] + dp[h - i][w]);
                for (int j = 1; j < w; ++j) best = std::max(best, dp[h][j] + dp[h][w - j]);
                dp[h][w] = best;
            }
        }
        return dp[m][n];
    }
};
