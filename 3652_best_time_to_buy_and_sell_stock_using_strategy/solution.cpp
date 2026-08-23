// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxProfit(std::vector<int>& prices, std::vector<int>& strategy, int k) {
        int n = (int)prices.size();
        std::vector<long long> s(n + 1), t(n + 1);
        for (int i = 1; i <= n; i++) {
            s[i] = s[i - 1] + 1LL * prices[i - 1] * strategy[i - 1];
            t[i] = t[i - 1] + prices[i - 1];
        }
        long long ans = s[n];
        for (int i = k; i <= n; i++) ans = std::max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]));
        return ans;
    }
};
