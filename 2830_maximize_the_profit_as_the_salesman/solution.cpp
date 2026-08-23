// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximizeTheProfit(int n, std::vector<std::vector<int>>& offers) {
        std::vector<std::vector<std::vector<int>>> byEnd(n);
        for (auto& o : offers) byEnd[o[1]].push_back(o);
        std::vector<int> dp(n + 1, 0);
        for (int end = 0; end < n; end++) {
            dp[end + 1] = dp[end];
            for (auto& o : byEnd[end]) {
                dp[end + 1] = std::max(dp[end + 1], dp[o[0]] + o[2]);
            }
        }
        return dp[n];
    }
};
