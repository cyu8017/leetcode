// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minGroups(std::vector<std::vector<int>>& intervals) {
        std::vector<std::pair<int, int>> events;
        events.reserve(intervals.size() * 2);
        for (auto& it : intervals) {
            events.push_back({it[0], 1});
            events.push_back({it[1] + 1, -1});
        }
        std::sort(events.begin(), events.end());
        int cur = 0, ans = 0;
        for (auto& [_, d] : events) {
            cur += d;
            ans = std::max(ans, cur);
        }
        return ans;
    }
};
