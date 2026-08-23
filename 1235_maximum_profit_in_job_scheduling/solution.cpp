// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

#include <algorithm>
#include <tuple>
#include <vector>

class Solution {
public:
    int jobScheduling(std::vector<int>& startTime, std::vector<int>& endTime, std::vector<int>& profit) {
        const int n = static_cast<int>(startTime.size());
        std::vector<std::tuple<int, int, int>> jobs;
        jobs.reserve(n);
        for (int i = 0; i < n; ++i) {
            jobs.emplace_back(endTime[i], startTime[i], profit[i]);
        }
        std::sort(jobs.begin(), jobs.end());
        std::vector<int> ends{0};
        std::vector<int> dp{0};
        for (const auto& [end, start, gain] : jobs) {
            int i = static_cast<int>(std::upper_bound(ends.begin(), ends.end(), start) - ends.begin()) - 1;
            ends.push_back(end);
            dp.push_back(std::max(dp.back(), dp[i] + gain));
        }
        return dp.back();
    }
};
