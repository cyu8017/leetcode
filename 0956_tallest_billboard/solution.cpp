// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int tallestBillboard(std::vector<int>& rods) {
        std::unordered_map<int, int> dp;
        dp[0] = 0;
        for (int rod : rods) {
            auto cur = dp;
            for (auto [diff, taller] : cur) {
                dp[diff + rod] = std::max(dp.count(diff + rod) ? dp[diff + rod] : 0, taller + rod);
                int nd = std::abs(diff - rod);
                int nt = diff >= rod ? taller : taller - diff + rod;
                dp[nd] = std::max(dp.count(nd) ? dp[nd] : 0, nt);
            }
        }
        return dp.count(0) ? dp[0] : 0;
    }
};
