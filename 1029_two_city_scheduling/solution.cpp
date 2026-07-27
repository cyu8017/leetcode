// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

#include <algorithm>
#include <vector>

class Solution {
public:
    int twoCitySchedCost(std::vector<std::vector<int>>& costs) {
        std::sort(costs.begin(), costs.end(), [](const auto& a, const auto& b) {
            return a[0] - a[1] < b[0] - b[1];
        });
        int n = static_cast<int>(costs.size()) / 2;
        int ans = 0;
        for (int i = 0; i < n; ++i) ans += costs[i][0];
        for (int i = n; i < 2 * n; ++i) ans += costs[i][1];
        return ans;
    }
};

