// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    int removeCoveredIntervals(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[0] != b[0]) {
                return a[0] < b[0];
            }
            return a[1] > b[1];
        });
        int answer = 0, farthest = -1;
        for (const auto& interval : intervals) {
            if (interval[1] > farthest) {
                ++answer;
                farthest = interval[1];
            }
        }
        return answer;
    }
};
