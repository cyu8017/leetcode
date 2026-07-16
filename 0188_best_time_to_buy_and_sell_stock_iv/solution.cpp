// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (n == 0 || k == 0) {
            return 0;
        }
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; ++i) {
                profit += max(prices[i] - prices[i - 1], 0);
            }
            return profit;
        }

        vector<int> buy(k + 1, INT_MAX);
        vector<int> sell(k + 1, 0);
        for (int price : prices) {
            for (int transaction = 1; transaction <= k; ++transaction) {
                buy[transaction] = min(buy[transaction], price - sell[transaction - 1]);
                sell[transaction] = max(sell[transaction], price - buy[transaction]);
            }
        }
        return sell[k];
    }
};