// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> findRightInterval(std::vector<std::vector<int>>& intervals) {
        std::vector<std::pair<int, int>> indexed;
        indexed.reserve(intervals.size());
        for (int index = 0; index < static_cast<int>(intervals.size()); ++index) {
            indexed.push_back({intervals[index][0], index});
        }
        std::sort(indexed.begin(), indexed.end());

        std::vector<int> starts;
        starts.reserve(indexed.size());
        for (const auto& entry : indexed) {
            starts.push_back(entry.first);
        }

        std::vector<int> result;
        result.reserve(intervals.size());
        for (const auto& interval : intervals) {
            int end = interval[1];
            auto position = std::lower_bound(starts.begin(), starts.end(), end);
            if (position == starts.end()) {
                result.push_back(-1);
            } else {
                result.push_back(indexed[position - starts.begin()].second);
            }
        }
        return result;
    }
};
