// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices, std::vector<int>& profits) {
        int n = (int)prices.size(), ans = -1;
        for (int j = 0; j < n; j++) {
            int bestL = -1, bestR = -1;
            for (int i = 0; i < j; i++)
                if (prices[i] < prices[j] && profits[i] > bestL) bestL = profits[i];
            for (int k = j + 1; k < n; k++)
                if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
            if (bestL >= 0 && bestR >= 0) {
                int cand = bestL + profits[j] + bestR;
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
};
