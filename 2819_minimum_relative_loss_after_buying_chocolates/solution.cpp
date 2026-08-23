// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> minimumRelativeLosses(std::vector<int>& prices, std::vector<std::vector<int>>& queries) {
        std::sort(prices.begin(), prices.end());
        int n = (int)prices.size();
        std::vector<long long> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int k = queries[qi][0], m = queries[qi][1];
            std::vector<long long> losses(n);
            for (int i = 0; i < n; i++) {
                if (prices[i] <= k) losses[i] = prices[i];
                else losses[i] = 2LL * k - prices[i];
            }
            std::sort(losses.begin(), losses.end());
            long long sum = 0;
            for (int i = 0; i < m; i++) sum += losses[i];
            ans[qi] = sum;
        }
        return ans;
    }
};
