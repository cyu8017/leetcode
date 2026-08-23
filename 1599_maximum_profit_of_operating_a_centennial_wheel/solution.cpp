// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minOperationsMaxProfit(std::vector<int>& customers, int boardingCost, int runningCost) {
        int waiting = 0;
        int profit = 0;
        int best = 0;
        int answer = 0;
        int rotation = 0;
        int i = 0;
        while (i < static_cast<int>(customers.size()) || waiting) {
            if (i < static_cast<int>(customers.size())) {
                waiting += customers[i];
            }
            const int boarded = std::min(4, waiting);
            waiting -= boarded;
            ++rotation;
            profit += boarded * boardingCost - runningCost;
            if (profit > best) {
                best = profit;
                answer = rotation;
            }
            ++i;
        }
        return best > 0 ? answer : -1;
    }
};
