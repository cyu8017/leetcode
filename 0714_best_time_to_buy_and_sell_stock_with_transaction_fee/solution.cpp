// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices, int fee) {
        int hold = -prices[0];
        int cash = 0;
        for (size_t i = 1; i < prices.size(); ++i) {
            int price = prices[i];
            hold = std::max(hold, cash - price);
            cash = std::max(cash, hold + price - fee);
        }
        return cash;
    }
};
