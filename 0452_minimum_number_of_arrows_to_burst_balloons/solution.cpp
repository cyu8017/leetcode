// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to_burst_balloons/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        if (points.empty()) {
            return 0;
        }

        std::sort(points.begin(), points.end(),
                  [](const std::vector<int>& left, const std::vector<int>& right) {
                      return left[1] < right[1];
                  });

        int arrows = 1;
        int end = points[0][1];
        for (size_t index = 1; index < points.size(); ++index) {
            if (points[index][0] > end) {
                ++arrows;
                end = points[index][1];
            }
        }
        return arrows;
    }
};
