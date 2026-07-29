// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> employeeFreeTime(std::vector<std::vector<std::vector<int>>>& schedule) {
        std::vector<std::vector<int>> intervals;
        for (const auto& employee : schedule) {
            for (const auto& item : employee) {
                intervals.push_back({item[0], item[1]});
            }
        }
        std::sort(intervals.begin(), intervals.end());
        std::vector<std::vector<int>> merged;
        for (const auto& iv : intervals) {
            if (merged.empty() || merged.back()[1] < iv[0]) {
                merged.push_back(iv);
            } else {
                merged.back()[1] = std::max(merged.back()[1], iv[1]);
            }
        }
        std::vector<std::vector<int>> result;
        for (size_t i = 1; i < merged.size(); ++i) {
            result.push_back({merged[i - 1][1], merged[i][0]});
        }
        return result;
    }
};
