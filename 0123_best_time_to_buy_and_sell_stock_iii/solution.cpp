// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

#include <vector>
#include <algorithm>
class Solution { public: int maxProfit(std::vector<int>& prices) {
    int buy1 = 1e9, buy2 = 1e9, sell1 = 0, sell2 = 0;
    for (int price : prices) { buy1 = std::min(buy1, price); sell1 = std::max(sell1, price - buy1); buy2 = std::min(buy2, price - sell1); sell2 = std::max(sell2, price - buy2); }
    return sell2;
} };