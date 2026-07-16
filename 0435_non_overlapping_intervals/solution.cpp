// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(),
                  [](const std::vector<int>& left, const std::vector<int>& right) {
                      return left[1] < right[1];
                  });

        int removed = 0;
        int end = INT_MIN;
        for (const auto& interval : intervals) {
            if (interval[0] < end) {
                ++removed;
            } else {
                end = interval[1];
            }
        }
        return removed;
    }
};
