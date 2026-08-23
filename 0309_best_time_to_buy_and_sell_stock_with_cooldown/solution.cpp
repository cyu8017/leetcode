// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        }
        int free = 0;
        int hold = -prices[0];
        int cooldown = 0;
        for (size_t index = 1; index < prices.size(); index++) {
            int price = prices[index];
            int nextFree = std::max(free, cooldown);
            int nextHold = std::max(hold, free - price);
            int nextCooldown = hold + price;
            free = nextFree;
            hold = nextHold;
            cooldown = nextCooldown;
        }
        return std::max(free, cooldown);
    }
};
