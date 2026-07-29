// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int lowest = prices.empty() ? 0 : prices[0];
        int best = 0;
        for (int price : prices) {
            lowest = std::min(lowest, price);
            best = std::max(best, price - lowest);
        }
        return best;
    }
};
