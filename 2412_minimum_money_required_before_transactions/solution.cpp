// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minimumMoney(std::vector<std::vector<int>>& transactions) {
        long long totalLoss = 0, maxCashback = 0, maxCost = 0;
        for (auto& t : transactions) {
            long long cost = t[0], cashback = t[1];
            if (cost > cashback) {
                totalLoss += cost - cashback;
                maxCashback = std::max(maxCashback, cashback);
            } else {
                maxCost = std::max(maxCost, cost);
            }
        }
        return std::max(totalLoss + maxCashback, totalLoss + maxCost);
    }
};
