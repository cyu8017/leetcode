// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });

        std::vector<std::vector<int>> merged;
        merged.push_back(intervals[0]);

        for (int i = 1; i < static_cast<int>(intervals.size()); ++i) {
            const auto& current = intervals[i];
            auto& last = merged.back();

            if (current[0] <= last[1]) {
                last[1] = std::max(last[1], current[1]);
            } else {
                merged.push_back(current);
            }
        }

        return merged;
    }
};
