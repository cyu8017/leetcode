// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

#include <algorithm>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int getNumberOfBacklogOrders(std::vector<std::vector<int>>& orders) {
        std::priority_queue<std::pair<int, int>> buy;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> sell;
        const int MOD = 1000000007;

        for (const auto& order : orders) {
            int price = order[0];
            int amount = order[1];
            int orderType = order[2];
            if (orderType == 0) {
                buy.push({price, amount});
            } else {
                sell.push({price, amount});
            }

            while (!buy.empty() && !sell.empty() && buy.top().first >= sell.top().first) {
                auto [buyPrice, buyAmount] = buy.top();
                buy.pop();
                auto [sellPrice, sellAmount] = sell.top();
                sell.pop();
                int matched = std::min(buyAmount, sellAmount);
                buyAmount -= matched;
                sellAmount -= matched;
                if (buyAmount) {
                    buy.push({buyPrice, buyAmount});
                }
                if (sellAmount) {
                    sell.push({sellPrice, sellAmount});
                }
            }
        }

        long long total = 0;
        while (!buy.empty()) {
            total = (total + buy.top().second) % MOD;
            buy.pop();
        }
        while (!sell.empty()) {
            total = (total + sell.top().second) % MOD;
            sell.pop();
        }
        return static_cast<int>(total);
    }
};
