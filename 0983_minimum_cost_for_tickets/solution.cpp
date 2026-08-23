// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int mincostTickets(std::vector<int>& days, std::vector<int>& costs) {
        std::unordered_set<int> dayset(days.begin(), days.end());
        int last = days.back();
        std::vector<int> dp(last + 1, 0);
        for (int d = 1; d <= last; d++) {
            if (!dayset.count(d)) dp[d] = dp[d - 1];
            else {
                dp[d] = std::min({
                    dp[d - 1] + costs[0],
                    dp[std::max(0, d - 7)] + costs[1],
                    dp[std::max(0, d - 30)] + costs[2]
                });
            }
        }
        return dp[last];
    }
};
